# -*- coding: utf-8 -*-
__name__ = 'coordCatalog'
__version__ = '0.1'
__author__ = 'Filippov Vladislav'

#from pydev import pydevd
import math
from common import *
from qgis.core import QGis


class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Measure():
# Измерение дирекционного угла и горизонтального проложения
	def __init__(self, point1, point2):
		self.point1 = point1
		self.point2 = point2
		self.ddx = self.point2.x - self.point1.x
		self.ddy = self.point2.y - self.point1.y
		self.ang = -1
		self.len = -1
		self.angle = ''
		self.lenght = ''
		self.calclenght()
		self.calcangle()

	def calclenght(self):
		a = math.pow(self.ddx, 2)
		b = math.pow(self.ddy, 2)
		self.len = math.sqrt(a + b)
		self.lenght = round(self.len, 2)

	def calcangle(self):
		if self.ddx == 0:
			if self.ddy < 0:
				self.angle = u'270°0,0\''
			else:
				self.angle = u'90°0,0\''
		else:
			alfa = math.fabs(math.atan(self.ddy / self.ddx) \
			                 * (180 / math.pi))
			if (self.ddx > 0) and (self.ddy > 0):
				self.ang = alfa
				self.calcdegmin()
			elif (self.ddx < 0) and (self.ddy > 0):
				self.ang = 180 - alfa
				self.calcdegmin()
			elif (self.ddx < 0) and (self.ddy < 0):
				self.ang = 180 + alfa
				self.calcdegmin()
			elif (self.ddx > 0) and (self.ddy < 0):
				self.ang = 360 - alfa
				self.calcdegmin()
			elif (self.ddx > 0) and (self.ddy == 0):
				self.angle = u'0°0\''
			elif (self.ddx < 0) and (self.ddy == 0):
				self.angle = u'180°0\''

	def calcdegmin(self):
		a = int(self.ang)
		minute = (self.ang - a) * 60
		self.angle = unicode(a) + u'°' + unicode('{0:.1f}'.format(minute)) + u'\''


class CatalogData():
	def __init__(self, features, is_new_point, is_ziped, font_size):
		self.features = features
		self.fontsize = u'xx-small'
		if font_size == 2:
			self.fontsize = u'small'
		elif font_size == 3:
			self.fontsize = u'medium'
		elif font_size == 4:
			self.fontsize = u'large'
		self.is_ziped = is_ziped
		self.list_contours = []  # 1 (если полигон) или N конутуров мультполигона
		self.list_ring = []  # контуры текущего полигона
		self.catalog = u'<HEAD><meta http-equiv=\"Content-type\" ' \
		               u'content=\"text/html;charset=UTF-8\"><style>table { font-size: '+self\
			.fontsize+u'; font-family: Arial;} p { font-size: '+self.fontsize+u'; font-family: Arial;}</style><HEAD/>'
		self.multi = False
		self.area = 0
		self.perimeter = 0
		self.is_new_point = is_new_point
		self.prepare_data()
		self.calculate()

	def prepare_data(self):
		# используется принцип openland - мультиполигоны не используются
		# многоконтурные ЗУ собираются по ID из простых полиногов
		if len(self.features) > 1:
			self.multi = True
			for feat in self.features:
				geom = feat.geometry()
				self.area += round(geom.area(), 0)
				self.perimeter += round(geom.length(), 2)
				self.parse_polygon(geom.asPolygon())
				#self.number_contours += 1
		else:
			geom = self.features[0].geometry()
			self.area = round(geom.area(), 0)
			self.perimeter = round(geom.length(), 2)
			self.parse_polygon(geom.asPolygon())

	# полигон может содержать один внешний и от нуля до N внутренних контуров (дырок)
	def parse_polygon(self, polygon):
		#self.list_ring = []
		for ring in polygon:
			list_ponts = []
			for node in ring:
				# Тут происходит переход к геодезической СК
				x = round(node.y(), 2)
				y = round(node.x(), 2)
				list_ponts.append([x, y])
			self.list_ring.append(list_ponts)
		self.list_contours.append(self.list_ring)

	def calculate(self):
		iter_c = 0
		iter_r = 0
		number = 1
		first_num = 1
		table = u''
		table_val = []
		#idParcel = self.feature.attributes()[self.layerUc.fieldNameIndex('id')]
		catalog_data = u''
		for polygon in self.list_contours:
			if self.multi and len(self.list_contours) > 1:
				catalog_data += u'<h3>Контур ' + unicode(iter_c + 1) + u'</h3>'
			table += u'<TABLE CELLSPACING=\"0\" COLS=\"5\" BORDER=\"0\"><COLGROUP SPAN=\"5\" WIDTH=\"120\"></COLGROUP>{0}</TABLE>'
			empty = u'<TD STYLE=\"border-top: 1px solid #000000; border-bottom: 1px solid #000000; ' \
			        u'border-left: 1px solid #000000; border-right: 1px solid #000000\" HEIGHT=\"17\" ALIGN=\"CENTER\">{0}</TD>'
			header = empty.format(u'№')
			header += empty.format(u'X, м')
			header += empty.format(u'Y, м')
			header += empty.format(u'Дирекционный угол')
			header += empty.format(u'Расстояние, м')
			catalog_data += u'<TR>{0}</TR>'.format(header)
			for ring in polygon:
				iter_n = 0
				for point in ring:
					if self.is_new_point:
						point_num = u'н' + unicode(number)
						first_pt_num = u'н' + unicode(first_num)
					else:
						point_num = unicode(number)
						first_pt_num = unicode(first_num)

					if iter_n > 0 and iter_n < len(ring) - 1:
						point1 = Point(ring[iter_n - 1][0],
						               ring[iter_n - 1][1])
						point2 = Point(ring[iter_n][0],
						               ring[iter_n][1])
						measure = Measure(point1, point2)
						catalog_data += self.decorate_value_html(
							[point_num, unicode(ring[iter_n - 1][0]),
							 unicode(ring[iter_n - 1][1]), measure.angle,
							 unicode(measure.lenght)])
						#table_val.append(point_num)
						number += 1

					elif iter_n == len(ring) - 1:
						point1 = Point(ring[iter_n - 1][0], ring[iter_n - 1][1])
						point2 = Point(ring[0][0], ring[0][1])
						measure = Measure(point1, point2)

						catalog_data += self.decorate_value_html(
							[point_num, unicode(ring[iter_n - 1][0]),
							 unicode(ring[iter_n - 1][1]), measure.angle,
							 unicode(measure.lenght)])
						catalog_data += self.decorate_value_html(
							[first_pt_num, unicode(ring[0][0]), unicode(ring[0][1]), u'', u''], True)

						#table_val.append(first_pt_num)
						number += 1

					iter_n += 1
				iter_r += 1
				first_num = iter_n  # номер первой точки внутреннего контура
				if len(ring) > 1 and iter_r != len(ring):
					catalog_data += empty.format('--')+empty.format('--')+\
					                empty.format('--')+empty.format('--')+empty.format('--')

			iter_c += 1
			iter_r = 0
			first_num = 1
			number = 1

		self.catalog += table.format(catalog_data)
		self.catalog += u'<p>Площадь: {0} кв.м; Периметр: {1} м</p>'.format(self.area, self.perimeter)

	def decorate_value_html(self, value, last=False):
		row1 = u'<TR>{0}</TR>'
		row2 = u'<TR>{0}</TR>'
		empty = u'<TD STYLE=\"border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: ' \
		        u'1px solid #000000; border-right: 1px solid #000000\" HEIGHT=\"17\" ALIGN=\"CENTER\">{0}</TD>'
		num = empty.format(value[0])
		x = empty.format(value[1])
		y = empty.format(value[2])
		a = empty.format(value[3])
		l = empty.format(value[4])
		data1 = num + x + y + empty.format('<BR>') + empty.format('<BR>')
		data2 = empty.format('<BR>') + empty.format('<BR>') + empty.format('<BR>') + a + l
		if not last:
			return row1.format(data1) + row2.format(data2)
		else:
			return row1.format(data1)
