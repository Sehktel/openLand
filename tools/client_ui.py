# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created: Mon Oct 28 11:22:20 2013
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogClient(object):
    def setupUi(self, DialogClient):
        DialogClient.setObjectName(_fromUtf8("DialogClient"))
        DialogClient.resize(420, 420)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/attributes.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogClient.setWindowIcon(icon)
        DialogClient.setSizeGripEnabled(True)
        DialogClient.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(DialogClient)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.comboBoxClientType = QtGui.QComboBox(DialogClient)
        self.comboBoxClientType.setObjectName(_fromUtf8("comboBoxClientType"))
        self.comboBoxClientType.addItem(_fromUtf8(""))
        self.comboBoxClientType.addItem(_fromUtf8(""))
        self.comboBoxClientType.addItem(_fromUtf8(""))
        self.comboBoxClientType.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBoxClientType)
        self.treeWidget = QtGui.QTreeWidget(DialogClient)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.verticalLayout.addWidget(self.treeWidget)
        self.tabWidget = QtGui.QTabWidget(DialogClient)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabPerson = QtGui.QWidget()
        self.tabPerson.setObjectName(_fromUtf8("tabPerson"))
        self.formLayout_2 = QtGui.QFormLayout(self.tabPerson)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label = QtGui.QLabel(self.tabPerson)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEditSurname = QtGui.QLineEdit(self.tabPerson)
        self.lineEditSurname.setObjectName(_fromUtf8("lineEditSurname"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditSurname)
        self.label_2 = QtGui.QLabel(self.tabPerson)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditFirst = QtGui.QLineEdit(self.tabPerson)
        self.lineEditFirst.setObjectName(_fromUtf8("lineEditFirst"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditFirst)
        self.label_3 = QtGui.QLabel(self.tabPerson)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEditPatronymic = QtGui.QLineEdit(self.tabPerson)
        self.lineEditPatronymic.setObjectName(_fromUtf8("lineEditPatronymic"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditPatronymic)
        self.tabWidget.addTab(self.tabPerson, _fromUtf8(""))
        self.tabOrganization = QtGui.QWidget()
        self.tabOrganization.setEnabled(False)
        self.tabOrganization.setObjectName(_fromUtf8("tabOrganization"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tabOrganization)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_4 = QtGui.QLabel(self.tabOrganization)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEditOrganization = QtGui.QLineEdit(self.tabOrganization)
        self.lineEditOrganization.setObjectName(_fromUtf8("lineEditOrganization"))
        self.gridLayout_2.addWidget(self.lineEditOrganization, 0, 1, 1, 1)
        self.comboBoxAgent = QtGui.QComboBox(self.tabOrganization)
        self.comboBoxAgent.setObjectName(_fromUtf8("comboBoxAgent"))
        self.gridLayout_2.addWidget(self.comboBoxAgent, 2, 1, 1, 1)
        self.lineEditCountry = QtGui.QLineEdit(self.tabOrganization)
        self.lineEditCountry.setObjectName(_fromUtf8("lineEditCountry"))
        self.gridLayout_2.addWidget(self.lineEditCountry, 1, 1, 1, 1)
        self.pushButtonAgent = QtGui.QPushButton(self.tabOrganization)
        self.pushButtonAgent.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAgent.setIcon(icon1)
        self.pushButtonAgent.setObjectName(_fromUtf8("pushButtonAgent"))
        self.gridLayout_2.addWidget(self.pushButtonAgent, 2, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.tabOrganization)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.tabOrganization)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.tabOrganization)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.lineEditAppointment = QtGui.QLineEdit(self.tabOrganization)
        self.lineEditAppointment.setObjectName(_fromUtf8("lineEditAppointment"))
        self.gridLayout_2.addWidget(self.lineEditAppointment, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tabOrganization, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonSelect = QtGui.QPushButton(DialogClient)
        self.pushButtonSelect.setEnabled(False)
        self.pushButtonSelect.setStatusTip(_fromUtf8(""))
        self.pushButtonSelect.setWhatsThis(_fromUtf8(""))
        self.pushButtonSelect.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/symbol_check.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSelect.setIcon(icon2)
        self.pushButtonSelect.setAutoDefault(False)
        self.pushButtonSelect.setDefault(True)
        self.pushButtonSelect.setObjectName(_fromUtf8("pushButtonSelect"))
        self.horizontalLayout.addWidget(self.pushButtonSelect)
        self.pushButtonAdd = QtGui.QPushButton(DialogClient)
        self.pushButtonAdd.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/symbol_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAdd.setIcon(icon3)
        self.pushButtonAdd.setAutoDefault(False)
        self.pushButtonAdd.setObjectName(_fromUtf8("pushButtonAdd"))
        self.horizontalLayout.addWidget(self.pushButtonAdd)
        self.pushButtonEdit = QtGui.QPushButton(DialogClient)
        self.pushButtonEdit.setText(_fromUtf8(""))
        self.pushButtonEdit.setIcon(icon1)
        self.pushButtonEdit.setAutoDefault(False)
        self.pushButtonEdit.setObjectName(_fromUtf8("pushButtonEdit"))
        self.horizontalLayout.addWidget(self.pushButtonEdit)
        self.pushButtonDel = QtGui.QPushButton(DialogClient)
        self.pushButtonDel.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/symbol_remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDel.setIcon(icon4)
        self.pushButtonDel.setAutoDefault(False)
        self.pushButtonDel.setObjectName(_fromUtf8("pushButtonDel"))
        self.horizontalLayout.addWidget(self.pushButtonDel)
        self.pushButtonSave = QtGui.QPushButton(DialogClient)
        self.pushButtonSave.setEnabled(False)
        self.pushButtonSave.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSave.setIcon(icon5)
        self.pushButtonSave.setAutoDefault(False)
        self.pushButtonSave.setObjectName(_fromUtf8("pushButtonSave"))
        self.horizontalLayout.addWidget(self.pushButtonSave)
        self.pushButtonRefresh = QtGui.QPushButton(DialogClient)
        self.pushButtonRefresh.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRefresh.setIcon(icon6)
        self.pushButtonRefresh.setAutoDefault(False)
        self.pushButtonRefresh.setObjectName(_fromUtf8("pushButtonRefresh"))
        self.horizontalLayout.addWidget(self.pushButtonRefresh)
        self.pushButtonClose = QtGui.QPushButton(DialogClient)
        self.pushButtonClose.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonClose.setIcon(icon7)
        self.pushButtonClose.setAutoDefault(False)
        self.pushButtonClose.setObjectName(_fromUtf8("pushButtonClose"))
        self.horizontalLayout.addWidget(self.pushButtonClose)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogClient)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DialogClient)
        DialogClient.setTabOrder(self.treeWidget, self.pushButtonSelect)
        DialogClient.setTabOrder(self.pushButtonSelect, self.pushButtonAdd)
        DialogClient.setTabOrder(self.pushButtonAdd, self.pushButtonEdit)
        DialogClient.setTabOrder(self.pushButtonEdit, self.pushButtonDel)
        DialogClient.setTabOrder(self.pushButtonDel, self.pushButtonSave)
        DialogClient.setTabOrder(self.pushButtonSave, self.pushButtonRefresh)
        DialogClient.setTabOrder(self.pushButtonRefresh, self.pushButtonClose)

    def retranslateUi(self, DialogClient):
        DialogClient.setWindowTitle(QtGui.QApplication.translate("DialogClient", "Заказчик кадастровых работ", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxClientType.setItemText(0, QtGui.QApplication.translate("DialogClient", "Физическое лицо", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxClientType.setItemText(1, QtGui.QApplication.translate("DialogClient", "Российское юридическое лицо", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxClientType.setItemText(2, QtGui.QApplication.translate("DialogClient", "Иностранное юридическое лицо", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxClientType.setItemText(3, QtGui.QApplication.translate("DialogClient", "Орган государственной власти, орган местного самоуправления", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("DialogClient", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("DialogClient", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("DialogClient", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogClient", "Фамилия", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogClient", "Имя", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DialogClient", "Отчество", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPerson), QtGui.QApplication.translate("DialogClient", "Физическое лицо", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DialogClient", "Представитель", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("DialogClient", "<html><head/><body><p>Наименование<br /> юридического лица</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DialogClient", "Страна", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("DialogClient", "Должность", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabOrganization), QtGui.QApplication.translate("DialogClient", "Юридическое лицо или орган власти", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSelect.setToolTip(QtGui.QApplication.translate("DialogClient", "Выбрать заказчика", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAdd.setToolTip(QtGui.QApplication.translate("DialogClient", "Добавить заказчика", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEdit.setToolTip(QtGui.QApplication.translate("DialogClient", "Редактировать атрибуты заказчика", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDel.setToolTip(QtGui.QApplication.translate("DialogClient", "Удалить заказчика", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonSave.setToolTip(QtGui.QApplication.translate("DialogClient", "Сохранить атрибуты заказчика", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonRefresh.setToolTip(QtGui.QApplication.translate("DialogClient", "Обновить атрибуты заказчика", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonClose.setToolTip(QtGui.QApplication.translate("DialogClient", "Закрыть окно", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc