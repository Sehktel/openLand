# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'geodesicbase.ui'
#
# Created: Mon Oct 28 11:22:25 2013
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogGeodesicBase(object):
    def setupUi(self, DialogGeodesicBase):
        DialogGeodesicBase.setObjectName(_fromUtf8("DialogGeodesicBase"))
        DialogGeodesicBase.resize(420, 420)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/geoshema.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogGeodesicBase.setWindowIcon(icon)
        DialogGeodesicBase.setSizeGripEnabled(True)
        DialogGeodesicBase.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(DialogGeodesicBase)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.treeWidget = QtGui.QTreeWidget(DialogGeodesicBase)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.verticalLayout.addWidget(self.treeWidget)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(DialogGeodesicBase)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEditPName = QtGui.QLineEdit(DialogGeodesicBase)
        self.lineEditPName.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEditPName.setInputMask(_fromUtf8(""))
        self.lineEditPName.setObjectName(_fromUtf8("lineEditPName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditPName)
        self.label_2 = QtGui.QLabel(DialogGeodesicBase)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditPKind = QtGui.QLineEdit(DialogGeodesicBase)
        self.lineEditPKind.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEditPKind.setObjectName(_fromUtf8("lineEditPKind"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditPKind)
        self.label_3 = QtGui.QLabel(DialogGeodesicBase)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEditPKlass = QtGui.QLineEdit(DialogGeodesicBase)
        self.lineEditPKlass.setInputMask(_fromUtf8(""))
        self.lineEditPKlass.setObjectName(_fromUtf8("lineEditPKlass"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditPKlass)
        self.label_4 = QtGui.QLabel(DialogGeodesicBase)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEditOrdX = QtGui.QLineEdit(DialogGeodesicBase)
        self.lineEditOrdX.setObjectName(_fromUtf8("lineEditOrdX"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEditOrdX)
        self.label_5 = QtGui.QLabel(DialogGeodesicBase)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEditOrdY = QtGui.QLineEdit(DialogGeodesicBase)
        self.lineEditOrdY.setObjectName(_fromUtf8("lineEditOrdY"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEditOrdY)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonSelect = QtGui.QPushButton(DialogGeodesicBase)
        self.pushButtonSelect.setEnabled(False)
        self.pushButtonSelect.setStatusTip(_fromUtf8(""))
        self.pushButtonSelect.setWhatsThis(_fromUtf8(""))
        self.pushButtonSelect.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/symbol_check.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSelect.setIcon(icon1)
        self.pushButtonSelect.setAutoDefault(False)
        self.pushButtonSelect.setDefault(True)
        self.pushButtonSelect.setObjectName(_fromUtf8("pushButtonSelect"))
        self.horizontalLayout.addWidget(self.pushButtonSelect)
        self.pushButtonAdd = QtGui.QPushButton(DialogGeodesicBase)
        self.pushButtonAdd.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/symbol_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAdd.setIcon(icon2)
        self.pushButtonAdd.setAutoDefault(False)
        self.pushButtonAdd.setObjectName(_fromUtf8("pushButtonAdd"))
        self.horizontalLayout.addWidget(self.pushButtonAdd)
        self.pushButtonEdit = QtGui.QPushButton(DialogGeodesicBase)
        self.pushButtonEdit.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonEdit.setIcon(icon3)
        self.pushButtonEdit.setAutoDefault(False)
        self.pushButtonEdit.setObjectName(_fromUtf8("pushButtonEdit"))
        self.horizontalLayout.addWidget(self.pushButtonEdit)
        self.pushButtonDel = QtGui.QPushButton(DialogGeodesicBase)
        self.pushButtonDel.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/symbol_remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDel.setIcon(icon4)
        self.pushButtonDel.setAutoDefault(False)
        self.pushButtonDel.setObjectName(_fromUtf8("pushButtonDel"))
        self.horizontalLayout.addWidget(self.pushButtonDel)
        self.pushButtonSave = QtGui.QPushButton(DialogGeodesicBase)
        self.pushButtonSave.setEnabled(False)
        self.pushButtonSave.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSave.setIcon(icon5)
        self.pushButtonSave.setAutoDefault(False)
        self.pushButtonSave.setObjectName(_fromUtf8("pushButtonSave"))
        self.horizontalLayout.addWidget(self.pushButtonSave)
        self.pushButtonRefresh = QtGui.QPushButton(DialogGeodesicBase)
        self.pushButtonRefresh.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRefresh.setIcon(icon6)
        self.pushButtonRefresh.setAutoDefault(False)
        self.pushButtonRefresh.setObjectName(_fromUtf8("pushButtonRefresh"))
        self.horizontalLayout.addWidget(self.pushButtonRefresh)
        self.pushButtonClose = QtGui.QPushButton(DialogGeodesicBase)
        self.pushButtonClose.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonClose.setIcon(icon7)
        self.pushButtonClose.setAutoDefault(False)
        self.pushButtonClose.setObjectName(_fromUtf8("pushButtonClose"))
        self.horizontalLayout.addWidget(self.pushButtonClose)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.labelMessage = QtGui.QLabel(DialogGeodesicBase)
        self.labelMessage.setText(_fromUtf8(""))
        self.labelMessage.setObjectName(_fromUtf8("labelMessage"))
        self.verticalLayout.addWidget(self.labelMessage)

        self.retranslateUi(DialogGeodesicBase)
        QtCore.QMetaObject.connectSlotsByName(DialogGeodesicBase)
        DialogGeodesicBase.setTabOrder(self.treeWidget, self.lineEditPName)
        DialogGeodesicBase.setTabOrder(self.lineEditPName, self.lineEditPKind)
        DialogGeodesicBase.setTabOrder(self.lineEditPKind, self.lineEditPKlass)
        DialogGeodesicBase.setTabOrder(self.lineEditPKlass, self.lineEditOrdX)
        DialogGeodesicBase.setTabOrder(self.lineEditOrdX, self.lineEditOrdY)
        DialogGeodesicBase.setTabOrder(self.lineEditOrdY, self.pushButtonSelect)
        DialogGeodesicBase.setTabOrder(self.pushButtonSelect, self.pushButtonAdd)
        DialogGeodesicBase.setTabOrder(self.pushButtonAdd, self.pushButtonEdit)
        DialogGeodesicBase.setTabOrder(self.pushButtonEdit, self.pushButtonDel)
        DialogGeodesicBase.setTabOrder(self.pushButtonDel, self.pushButtonSave)
        DialogGeodesicBase.setTabOrder(self.pushButtonSave, self.pushButtonRefresh)
        DialogGeodesicBase.setTabOrder(self.pushButtonRefresh, self.pushButtonClose)

    def retranslateUi(self, DialogGeodesicBase):
        DialogGeodesicBase.setWindowTitle(QtGui.QApplication.translate("DialogGeodesicBase", "Сведения о геодезической основе", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("DialogGeodesicBase", "Название пункта", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("DialogGeodesicBase", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("DialogGeodesicBase", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogGeodesicBase", "Название пункта<br />геодезической сети", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogGeodesicBase", "Тип пункта<br />геодезической сети", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DialogGeodesicBase", "Класс<br />геодезической сети", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DialogGeodesicBase", "Координата Х", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DialogGeodesicBase", "Координата Y", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSelect.setToolTip(QtGui.QApplication.translate("DialogGeodesicBase", "Выбрать пункт геодезической сети", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAdd.setToolTip(QtGui.QApplication.translate("DialogGeodesicBase", "Добавить пункт геодезической сети", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEdit.setToolTip(QtGui.QApplication.translate("DialogGeodesicBase", "Редактировать атрибуты пункта геодезической сети", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDel.setToolTip(QtGui.QApplication.translate("DialogGeodesicBase", "Удалить пункт геодезической сети", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSave.setToolTip(QtGui.QApplication.translate("DialogGeodesicBase", "Сохранить атрибуты пункта геодезической сети", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonRefresh.setToolTip(QtGui.QApplication.translate("DialogGeodesicBase", "Обновить атрибуты пункта геодезической сети", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonClose.setToolTip(QtGui.QApplication.translate("DialogGeodesicBase", "Закрыть окно", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
