# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uchattributes.ui'
#
# Created: Wed May 28 18:09:37 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_uchAttributes(object):
    def setupUi(self, uchAttributes):
        uchAttributes.setObjectName(_fromUtf8("uchAttributes"))
        uchAttributes.setWindowModality(QtCore.Qt.ApplicationModal)
        uchAttributes.resize(820, 740)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/attributes.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        uchAttributes.setWindowIcon(icon)
        uchAttributes.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(uchAttributes)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.toolBox = QtGui.QToolBox(uchAttributes)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 786, 413))
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.textEditIspolzDok = QtGui.QTextEdit(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditIspolzDok.sizePolicy().hasHeightForWidth())
        self.textEditIspolzDok.setSizePolicy(sizePolicy)
        self.textEditIspolzDok.setMaximumSize(QtCore.QSize(16777215, 60))
        self.textEditIspolzDok.setTabChangesFocus(True)
        self.textEditIspolzDok.setObjectName(_fromUtf8("textEditIspolzDok"))
        self.gridLayout_2.addWidget(self.textEditIspolzDok, 5, 1, 1, 3)
        self.label_7 = QtGui.QLabel(self.page)
        self.label_7.setOpenExternalLinks(False)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)
        self.pushButtonUtilization = QtGui.QPushButton(self.page)
        self.pushButtonUtilization.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/format_indent_more.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonUtilization.setIcon(icon1)
        self.pushButtonUtilization.setAutoDefault(False)
        self.pushButtonUtilization.setObjectName(_fromUtf8("pushButtonUtilization"))
        self.gridLayout_2.addWidget(self.pushButtonUtilization, 5, 4, 1, 1)
        self.label_2 = QtGui.QLabel(self.page)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.comboBoxKvr = QtGui.QComboBox(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxKvr.sizePolicy().hasHeightForWidth())
        self.comboBoxKvr.setSizePolicy(sizePolicy)
        self.comboBoxKvr.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBoxKvr.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBoxKvr.setBaseSize(QtCore.QSize(0, 0))
        self.comboBoxKvr.setObjectName(_fromUtf8("comboBoxKvr"))
        self.gridLayout_2.addWidget(self.comboBoxKvr, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.page)
        self.label_6.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.page)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBoxDocumentCategory = QtGui.QComboBox(self.page)
        self.comboBoxDocumentCategory.setObjectName(_fromUtf8("comboBoxDocumentCategory"))
        self.gridLayout_2.addWidget(self.comboBoxDocumentCategory, 3, 3, 1, 1)
        self.lineEditObozNaPlane = QtGui.QLineEdit(self.page)
        self.lineEditObozNaPlane.setObjectName(_fromUtf8("lineEditObozNaPlane"))
        self.gridLayout_2.addWidget(self.lineEditObozNaPlane, 1, 3, 1, 1)
        self.label_15 = QtGui.QLabel(self.page)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_2.addWidget(self.label_15, 3, 2, 1, 1)
        self.comboBoxVid = QtGui.QComboBox(self.page)
        self.comboBoxVid.setEnabled(True)
        self.comboBoxVid.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBoxVid.setBaseSize(QtCore.QSize(0, 0))
        self.comboBoxVid.setObjectName(_fromUtf8("comboBoxVid"))
        self.gridLayout_2.addWidget(self.comboBoxVid, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.page)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.comboBoxKatZem = QtGui.QComboBox(self.page)
        self.comboBoxKatZem.setMaximumSize(QtCore.QSize(272, 16777215))
        self.comboBoxKatZem.setBaseSize(QtCore.QSize(0, 0))
        self.comboBoxKatZem.setEditable(False)
        self.comboBoxKatZem.setObjectName(_fromUtf8("comboBoxKatZem"))
        self.gridLayout_2.addWidget(self.comboBoxKatZem, 3, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.page)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 1, 2, 1, 1)
        self.lineEditGknArea = QtGui.QLineEdit(self.page)
        self.lineEditGknArea.setMaximumSize(QtCore.QSize(125, 16777215))
        self.lineEditGknArea.setObjectName(_fromUtf8("lineEditGknArea"))
        self.gridLayout_2.addWidget(self.lineEditGknArea, 7, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.page)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 1)
        self.spinBoxNomerKontura = QtGui.QSpinBox(self.page)
        self.spinBoxNomerKontura.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxNomerKontura.sizePolicy().hasHeightForWidth())
        self.spinBoxNomerKontura.setSizePolicy(sizePolicy)
        self.spinBoxNomerKontura.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBoxNomerKontura.setMaximum(999)
        self.spinBoxNomerKontura.setObjectName(_fromUtf8("spinBoxNomerKontura"))
        self.gridLayout_2.addWidget(self.spinBoxNomerKontura, 1, 1, 1, 1)
        self.lineEditKn = QtGui.QLineEdit(self.page)
        self.lineEditKn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEditKn.setMaxLength(100)
        self.lineEditKn.setObjectName(_fromUtf8("lineEditKn"))
        self.gridLayout_2.addWidget(self.lineEditKn, 0, 3, 1, 1)
        self.label = QtGui.QLabel(self.page)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 2, 1, 1)
        self.label_17 = QtGui.QLabel(self.page)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_2.addWidget(self.label_17, 6, 2, 1, 1)
        self.lineEditDeltaArea = QtGui.QLineEdit(self.page)
        self.lineEditDeltaArea.setMaximumSize(QtCore.QSize(125, 16777215))
        self.lineEditDeltaArea.setObjectName(_fromUtf8("lineEditDeltaArea"))
        self.gridLayout_2.addWidget(self.lineEditDeltaArea, 7, 3, 1, 1)
        self.pushButtonDocumentCategory = QtGui.QPushButton(self.page)
        self.pushButtonDocumentCategory.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/folders.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDocumentCategory.setIcon(icon2)
        self.pushButtonDocumentCategory.setAutoDefault(False)
        self.pushButtonDocumentCategory.setObjectName(_fromUtf8("pushButtonDocumentCategory"))
        self.gridLayout_2.addWidget(self.pushButtonDocumentCategory, 3, 4, 1, 1)
        self.comboBoxSposobObraz = QtGui.QComboBox(self.page)
        self.comboBoxSposobObraz.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBoxSposobObraz.setBaseSize(QtCore.QSize(0, 0))
        self.comboBoxSposobObraz.setObjectName(_fromUtf8("comboBoxSposobObraz"))
        self.gridLayout_2.addWidget(self.comboBoxSposobObraz, 2, 3, 1, 1)
        self.label_9 = QtGui.QLabel(self.page)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 2, 2, 1, 1)
        self.label_21 = QtGui.QLabel(self.page)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_2.addWidget(self.label_21, 7, 2, 1, 1)
        self.comboBoxDocumentUtilization = QtGui.QComboBox(self.page)
        self.comboBoxDocumentUtilization.setObjectName(_fromUtf8("comboBoxDocumentUtilization"))
        self.gridLayout_2.addWidget(self.comboBoxDocumentUtilization, 6, 3, 1, 1)
        self.pushButtonDocumentUtilization = QtGui.QPushButton(self.page)
        self.pushButtonDocumentUtilization.setText(_fromUtf8(""))
        self.pushButtonDocumentUtilization.setIcon(icon2)
        self.pushButtonDocumentUtilization.setAutoDefault(False)
        self.pushButtonDocumentUtilization.setObjectName(_fromUtf8("pushButtonDocumentUtilization"))
        self.gridLayout_2.addWidget(self.pushButtonDocumentUtilization, 6, 4, 1, 1)
        self.label_20 = QtGui.QLabel(self.page)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_2.addWidget(self.label_20, 7, 0, 1, 1)
        self.comboBoxIspolzSprav = QtGui.QComboBox(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxIspolzSprav.sizePolicy().hasHeightForWidth())
        self.comboBoxIspolzSprav.setSizePolicy(sizePolicy)
        self.comboBoxIspolzSprav.setMaximumSize(QtCore.QSize(632, 16777215))
        self.comboBoxIspolzSprav.setObjectName(_fromUtf8("comboBoxIspolzSprav"))
        self.gridLayout_2.addWidget(self.comboBoxIspolzSprav, 4, 1, 1, 3)
        self.label_22 = QtGui.QLabel(self.page)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_2.addWidget(self.label_22, 8, 2, 1, 1)
        self.comboBoxTypeObject = QtGui.QComboBox(self.page)
        self.comboBoxTypeObject.setObjectName(_fromUtf8("comboBoxTypeObject"))
        self.gridLayout_2.addWidget(self.comboBoxTypeObject, 8, 3, 1, 1)
        self.lineEditAdditionalName = QtGui.QLineEdit(self.page)
        self.lineEditAdditionalName.setObjectName(_fromUtf8("lineEditAdditionalName"))
        self.gridLayout_2.addWidget(self.lineEditAdditionalName, 6, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.page)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.page)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 8, 0, 1, 1)
        self.comboBoxStatus = QtGui.QComboBox(self.page)
        self.comboBoxStatus.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBoxStatus.setBaseSize(QtCore.QSize(0, 0))
        self.comboBoxStatus.setObjectName(_fromUtf8("comboBoxStatus"))
        self.gridLayout_2.addWidget(self.comboBoxStatus, 8, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_16 = QtGui.QLabel(self.page)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_4.addWidget(self.label_16)
        self.lineEditMinArea = QtGui.QLineEdit(self.page)
        self.lineEditMinArea.setObjectName(_fromUtf8("lineEditMinArea"))
        self.horizontalLayout_4.addWidget(self.lineEditMinArea)
        self.comboBoxMinAreaUnit = QtGui.QComboBox(self.page)
        self.comboBoxMinAreaUnit.setObjectName(_fromUtf8("comboBoxMinAreaUnit"))
        self.horizontalLayout_4.addWidget(self.comboBoxMinAreaUnit)
        self.label_18 = QtGui.QLabel(self.page)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_4.addWidget(self.label_18)
        self.lineEditMaxArea = QtGui.QLineEdit(self.page)
        self.lineEditMaxArea.setObjectName(_fromUtf8("lineEditMaxArea"))
        self.horizontalLayout_4.addWidget(self.lineEditMaxArea)
        self.comboBoxMaxAreaUnit = QtGui.QComboBox(self.page)
        self.comboBoxMaxAreaUnit.setObjectName(_fromUtf8("comboBoxMaxAreaUnit"))
        self.horizontalLayout_4.addWidget(self.comboBoxMaxAreaUnit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_23 = QtGui.QLabel(self.page)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout_3.addWidget(self.label_23)
        self.textEditNote = QtGui.QTextEdit(self.page)
        self.textEditNote.setTabChangesFocus(True)
        self.textEditNote.setObjectName(_fromUtf8("textEditNote"))
        self.horizontalLayout_3.addWidget(self.textEditNote)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_24 = QtGui.QLabel(self.page)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.horizontalLayout_6.addWidget(self.label_24)
        self.lineEditCreateUser = QtGui.QLineEdit(self.page)
        self.lineEditCreateUser.setReadOnly(True)
        self.lineEditCreateUser.setObjectName(_fromUtf8("lineEditCreateUser"))
        self.horizontalLayout_6.addWidget(self.lineEditCreateUser)
        self.lineEditCreateDate = QtGui.QLineEdit(self.page)
        self.lineEditCreateDate.setReadOnly(True)
        self.lineEditCreateDate.setObjectName(_fromUtf8("lineEditCreateDate"))
        self.horizontalLayout_6.addWidget(self.lineEditCreateDate)
        self.label_25 = QtGui.QLabel(self.page)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.horizontalLayout_6.addWidget(self.label_25)
        self.lineEditUpdateUser = QtGui.QLineEdit(self.page)
        self.lineEditUpdateUser.setReadOnly(True)
        self.lineEditUpdateUser.setObjectName(_fromUtf8("lineEditUpdateUser"))
        self.horizontalLayout_6.addWidget(self.lineEditUpdateUser)
        self.lineEditUpdateDate = QtGui.QLineEdit(self.page)
        self.lineEditUpdateDate.setReadOnly(True)
        self.lineEditUpdateDate.setObjectName(_fromUtf8("lineEditUpdateDate"))
        self.horizontalLayout_6.addWidget(self.lineEditUpdateDate)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 256, 170))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_13 = QtGui.QLabel(self.page_2)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)
        self.comboBoxTipChast = QtGui.QComboBox(self.page_2)
        self.comboBoxTipChast.setEnabled(False)
        self.comboBoxTipChast.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBoxTipChast.setBaseSize(QtCore.QSize(0, 0))
        self.comboBoxTipChast.setObjectName(_fromUtf8("comboBoxTipChast"))
        self.gridLayout_3.addWidget(self.comboBoxTipChast, 0, 1, 1, 1)
        self.checkBoxSubparcel4Realty = QtGui.QCheckBox(self.page_2)
        self.checkBoxSubparcel4Realty.setEnabled(False)
        self.checkBoxSubparcel4Realty.setObjectName(_fromUtf8("checkBoxSubparcel4Realty"))
        self.gridLayout_3.addWidget(self.checkBoxSubparcel4Realty, 0, 2, 1, 1)
        self.textEditVidObremeneniya = QtGui.QTextEdit(self.page_2)
        self.textEditVidObremeneniya.setEnabled(False)
        self.textEditVidObremeneniya.setMaximumSize(QtCore.QSize(16777215, 60))
        self.textEditVidObremeneniya.setTabChangesFocus(True)
        self.textEditVidObremeneniya.setObjectName(_fromUtf8("textEditVidObremeneniya"))
        self.gridLayout_3.addWidget(self.textEditVidObremeneniya, 1, 1, 1, 1)
        self.label_14 = QtGui.QLabel(self.page_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_3.addWidget(self.label_14, 1, 0, 1, 1)
        self.comboBoxTipObrem = QtGui.QComboBox(self.page_2)
        self.comboBoxTipObrem.setEnabled(False)
        self.comboBoxTipObrem.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBoxTipObrem.setBaseSize(QtCore.QSize(0, 0))
        self.comboBoxTipObrem.setObjectName(_fromUtf8("comboBoxTipObrem"))
        self.gridLayout_3.addWidget(self.comboBoxTipObrem, 2, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.page_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 1)
        self.label_19 = QtGui.QLabel(self.page_2)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_3.addWidget(self.label_19, 3, 0, 1, 1)
        self.comboBoxDocumentEncumbrance = QtGui.QComboBox(self.page_2)
        self.comboBoxDocumentEncumbrance.setEnabled(False)
        self.comboBoxDocumentEncumbrance.setObjectName(_fromUtf8("comboBoxDocumentEncumbrance"))
        self.gridLayout_3.addWidget(self.comboBoxDocumentEncumbrance, 3, 1, 1, 1)
        self.pushButtonDocumentEncumbrance = QtGui.QPushButton(self.page_2)
        self.pushButtonDocumentEncumbrance.setEnabled(False)
        self.pushButtonDocumentEncumbrance.setText(_fromUtf8(""))
        self.pushButtonDocumentEncumbrance.setIcon(icon2)
        self.pushButtonDocumentEncumbrance.setAutoDefault(False)
        self.pushButtonDocumentEncumbrance.setObjectName(_fromUtf8("pushButtonDocumentEncumbrance"))
        self.gridLayout_3.addWidget(self.pushButtonDocumentEncumbrance, 3, 2, 1, 1)
        self.pushButtonEncumbrance = QtGui.QPushButton(self.page_2)
        self.pushButtonEncumbrance.setEnabled(False)
        self.pushButtonEncumbrance.setText(_fromUtf8(""))
        self.pushButtonEncumbrance.setIcon(icon1)
        self.pushButtonEncumbrance.setAutoDefault(False)
        self.pushButtonEncumbrance.setObjectName(_fromUtf8("pushButtonEncumbrance"))
        self.gridLayout_3.addWidget(self.pushButtonEncumbrance, 1, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.toolBox)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.treeWidgetUch = QtGui.QTreeWidget(uchAttributes)
        self.treeWidgetUch.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.treeWidgetUch.setAnimated(True)
        self.treeWidgetUch.setObjectName(_fromUtf8("treeWidgetUch"))
        self.treeWidgetUch.header().setVisible(True)
        self.treeWidgetUch.header().setCascadingSectionResizes(False)
        self.treeWidgetUch.header().setDefaultSectionSize(200)
        self.treeWidgetUch.header().setMinimumSectionSize(200)
        self.horizontalLayout_2.addWidget(self.treeWidgetUch)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonSave = QtGui.QPushButton(uchAttributes)
        self.pushButtonSave.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSave.setIcon(icon3)
        self.pushButtonSave.setObjectName(_fromUtf8("pushButtonSave"))
        self.horizontalLayout.addWidget(self.pushButtonSave)
        self.pushButtonAdd = QtGui.QPushButton(uchAttributes)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/symbol_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAdd.setIcon(icon4)
        self.pushButtonAdd.setAutoDefault(False)
        self.pushButtonAdd.setObjectName(_fromUtf8("pushButtonAdd"))
        self.horizontalLayout.addWidget(self.pushButtonAdd)
        self.pushButtonEdit = QtGui.QPushButton(uchAttributes)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonEdit.setIcon(icon5)
        self.pushButtonEdit.setAutoDefault(False)
        self.pushButtonEdit.setObjectName(_fromUtf8("pushButtonEdit"))
        self.horizontalLayout.addWidget(self.pushButtonEdit)
        self.pushButtonDel = QtGui.QPushButton(uchAttributes)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/symbol_remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDel.setIcon(icon6)
        self.pushButtonDel.setAutoDefault(False)
        self.pushButtonDel.setObjectName(_fromUtf8("pushButtonDel"))
        self.horizontalLayout.addWidget(self.pushButtonDel)
        self.pushButtonRefr = QtGui.QPushButton(uchAttributes)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRefr.setIcon(icon7)
        self.pushButtonRefr.setAutoDefault(False)
        self.pushButtonRefr.setObjectName(_fromUtf8("pushButtonRefr"))
        self.horizontalLayout.addWidget(self.pushButtonRefr)
        self.pushButtonClose = QtGui.QPushButton(uchAttributes)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/openland/icons/close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonClose.setIcon(icon8)
        self.pushButtonClose.setAutoDefault(True)
        self.pushButtonClose.setObjectName(_fromUtf8("pushButtonClose"))
        self.horizontalLayout.addWidget(self.pushButtonClose)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(uchAttributes)
        self.toolBox.setCurrentIndex(0)
        QtCore.QObject.connect(self.treeWidgetUch, QtCore.SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), self.pushButtonEdit.click)
        QtCore.QMetaObject.connectSlotsByName(uchAttributes)
        uchAttributes.setTabOrder(self.comboBoxKvr, self.lineEditKn)
        uchAttributes.setTabOrder(self.lineEditKn, self.spinBoxNomerKontura)
        uchAttributes.setTabOrder(self.spinBoxNomerKontura, self.lineEditObozNaPlane)
        uchAttributes.setTabOrder(self.lineEditObozNaPlane, self.comboBoxVid)
        uchAttributes.setTabOrder(self.comboBoxVid, self.comboBoxSposobObraz)
        uchAttributes.setTabOrder(self.comboBoxSposobObraz, self.comboBoxKatZem)
        uchAttributes.setTabOrder(self.comboBoxKatZem, self.comboBoxDocumentCategory)
        uchAttributes.setTabOrder(self.comboBoxDocumentCategory, self.pushButtonDocumentCategory)
        uchAttributes.setTabOrder(self.pushButtonDocumentCategory, self.comboBoxIspolzSprav)
        uchAttributes.setTabOrder(self.comboBoxIspolzSprav, self.textEditIspolzDok)
        uchAttributes.setTabOrder(self.textEditIspolzDok, self.pushButtonUtilization)
        uchAttributes.setTabOrder(self.pushButtonUtilization, self.lineEditAdditionalName)
        uchAttributes.setTabOrder(self.lineEditAdditionalName, self.comboBoxDocumentUtilization)
        uchAttributes.setTabOrder(self.comboBoxDocumentUtilization, self.pushButtonDocumentUtilization)
        uchAttributes.setTabOrder(self.pushButtonDocumentUtilization, self.lineEditGknArea)
        uchAttributes.setTabOrder(self.lineEditGknArea, self.lineEditDeltaArea)
        uchAttributes.setTabOrder(self.lineEditDeltaArea, self.comboBoxStatus)
        uchAttributes.setTabOrder(self.comboBoxStatus, self.comboBoxTypeObject)
        uchAttributes.setTabOrder(self.comboBoxTypeObject, self.lineEditMinArea)
        uchAttributes.setTabOrder(self.lineEditMinArea, self.comboBoxMinAreaUnit)
        uchAttributes.setTabOrder(self.comboBoxMinAreaUnit, self.lineEditMaxArea)
        uchAttributes.setTabOrder(self.lineEditMaxArea, self.comboBoxMaxAreaUnit)
        uchAttributes.setTabOrder(self.comboBoxMaxAreaUnit, self.textEditNote)
        uchAttributes.setTabOrder(self.textEditNote, self.comboBoxTipChast)
        uchAttributes.setTabOrder(self.comboBoxTipChast, self.checkBoxSubparcel4Realty)
        uchAttributes.setTabOrder(self.checkBoxSubparcel4Realty, self.textEditVidObremeneniya)
        uchAttributes.setTabOrder(self.textEditVidObremeneniya, self.pushButtonEncumbrance)
        uchAttributes.setTabOrder(self.pushButtonEncumbrance, self.comboBoxTipObrem)
        uchAttributes.setTabOrder(self.comboBoxTipObrem, self.comboBoxDocumentEncumbrance)
        uchAttributes.setTabOrder(self.comboBoxDocumentEncumbrance, self.pushButtonDocumentEncumbrance)
        uchAttributes.setTabOrder(self.pushButtonDocumentEncumbrance, self.treeWidgetUch)
        uchAttributes.setTabOrder(self.treeWidgetUch, self.pushButtonSave)
        uchAttributes.setTabOrder(self.pushButtonSave, self.pushButtonAdd)
        uchAttributes.setTabOrder(self.pushButtonAdd, self.pushButtonEdit)
        uchAttributes.setTabOrder(self.pushButtonEdit, self.pushButtonDel)
        uchAttributes.setTabOrder(self.pushButtonDel, self.pushButtonRefr)
        uchAttributes.setTabOrder(self.pushButtonRefr, self.pushButtonClose)

    def retranslateUi(self, uchAttributes):
        uchAttributes.setWindowTitle(_translate("uchAttributes", "Атрибуты кадастрового участка", None))
        self.label_7.setText(_translate("uchAttributes", "<html><head/><body><p align=\"right\">Использование <br/>по документу</p></body></html>", None))
        self.label_2.setText(_translate("uchAttributes", "<html><head/><body><p align=\"right\">Кадастровый<br/>квартал</p></body></html>", None))
        self.label_6.setText(_translate("uchAttributes", "<html><head/><body><p align=\"right\">Использование<br />по справочнику</p></body></html>", None))
        self.label_3.setText(_translate("uchAttributes", "<html><head/><body><p align=\"right\">Вид ЗУ</p></body></html>", None))
        self.label_15.setText(_translate("uchAttributes", "<html><head/><body><p align=\"right\">Документ<br/>категории</p></body></html>", None))
        self.label_5.setText(_translate("uchAttributes", "<html><head/><body><p align=\"right\">Категория<br/>земли</p></body></html>", None))
        self.label_10.setText(_translate("uchAttributes", "<html><head/><body><p align=\"right\">Обозначение<br/>на плане</p></body></html>", None))
        self.label_11.setText(_translate("uchAttributes", "<html><head/><body><p align=\"right\">Номер<br/>контура</p></body></html>", None))
        self.label.setText(_translate("uchAttributes", "<html><head/><body><p align=\"right\">Кадастровый<br/>номер</p></body></html>", None))
        self.label_17.setText(_translate("uchAttributes", "<html><head/><body><p align=\"right\">Документ<br/>использования</p></body></html>", None))
        self.label_9.setText(_translate("uchAttributes", "<html><head/><body><p align=\"right\">Способ образования<br/>(тип нумерации точек)</p></body></html>", None))
        self.label_21.setText(_translate("uchAttributes", "<html><head/><body><p align=\"right\">Оценка<br/>расхождения</p></body></html>", None))
        self.label_20.setText(_translate("uchAttributes", "<html><head/><body><p align=\"right\">Площадь по<br/>сведениям ГКН</p></body></html>", None))
        self.label_22.setText(_translate("uchAttributes", "<html><head/><body><p align=\"right\">Объект<br/>кадастровых работ</p></body></html>", None))
        self.label_8.setText(_translate("uchAttributes", "<html><head/><body><p align=\"right\">Дополнительное<br/>наименование</p></body></html>", None))
        self.label_4.setText(_translate("uchAttributes", "<html><head/><body><p align=\"right\">Статус ЗУ</p></body></html>", None))
        self.label_16.setText(_translate("uchAttributes", "Минимальная площадь", None))
        self.label_18.setText(_translate("uchAttributes", "Максимальная площадь", None))
        self.label_23.setText(_translate("uchAttributes", "<html><head/><body><p align=\"right\">Иные<br/>сведения</p></body></html>", None))
        self.label_24.setText(_translate("uchAttributes", "<html><head/><body><p>Создание:</p></body></html>", None))
        self.label_25.setText(_translate("uchAttributes", "<html><head/><body><p>Последнее изменение:</p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("uchAttributes", "ЗУ, контур многоконтурного", None))
        self.label_13.setText(_translate("uchAttributes", "<html><head/><body><p align=\"right\">Тип ЧЗУ</p></body></html>", None))
        self.checkBoxSubparcel4Realty.setText(_translate("uchAttributes", "ЧЗУ под ОН", None))
        self.label_14.setText(_translate("uchAttributes", "<html><head/><body><p align=\"right\">Вид<br/>обременения</p></body></html>", None))
        self.label_12.setText(_translate("uchAttributes", "<html><head/><body><p align=\"right\">Тип<br/>обременения</p></body></html>", None))
        self.label_19.setText(_translate("uchAttributes", "<html><head/><body><p align=\"right\">Документ<br/>обременение</p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("uchAttributes", "ЧЗУ, обременения", None))
        self.treeWidgetUch.setSortingEnabled(True)
        self.treeWidgetUch.headerItem().setText(0, _translate("uchAttributes", "Атрибут", None))
        self.treeWidgetUch.headerItem().setText(1, _translate("uchAttributes", "Значение", None))
        self.pushButtonSave.setText(_translate("uchAttributes", "Сохранить", None))
        self.pushButtonAdd.setText(_translate("uchAttributes", "Добавить", None))
        self.pushButtonEdit.setText(_translate("uchAttributes", "Редактировать", None))
        self.pushButtonDel.setText(_translate("uchAttributes", "Удалить", None))
        self.pushButtonRefr.setText(_translate("uchAttributes", "Обновить", None))
        self.pushButtonClose.setText(_translate("uchAttributes", "Закрыть", None))

import resources_rc
