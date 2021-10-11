# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ESAU\imageResizer.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(450, 210)
        Dialog.setMinimumSize(QtCore.QSize(450, 210))
        Dialog.setMaximumSize(QtCore.QSize(450, 210))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.banner = QtGui.QLabel(Dialog)
        self.banner.setMinimumSize(QtCore.QSize(450, 100))
        self.banner.setMaximumSize(QtCore.QSize(450, 100))
        self.banner.setText(_fromUtf8(""))
        self.banner.setPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/banner.jpg")))
        self.banner.setObjectName(_fromUtf8("banner"))
        self.verticalLayout.addWidget(self.banner)
        self.gridLayout.addLayout(self.verticalLayout, 4, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setMargin(9)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setMargin(10)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.width_size = QtGui.QLineEdit(Dialog)
        self.width_size.setToolTip(_fromUtf8(""))
        self.width_size.setObjectName(_fromUtf8("width_size"))
        self.horizontalLayout.addWidget(self.width_size)
        self.label = QtGui.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.height_size = QtGui.QLineEdit(Dialog)
        self.height_size.setToolTip(_fromUtf8(""))
        self.height_size.setObjectName(_fromUtf8("height_size"))
        self.horizontalLayout.addWidget(self.height_size)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.source_path = QtGui.QLineEdit(Dialog)
        self.source_path.setObjectName(_fromUtf8("source_path"))
        self.horizontalLayout_3.addWidget(self.source_path)
        self.browse_btn = QtGui.QPushButton(Dialog)
        self.browse_btn.setToolTip(_fromUtf8(""))
        self.browse_btn.setObjectName(_fromUtf8("browse_btn"))
        self.horizontalLayout_3.addWidget(self.browse_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.overwrite = QtGui.QCheckBox(Dialog)
        self.overwrite.setAcceptDrops(False)
        self.overwrite.setChecked(True)
        self.overwrite.setObjectName(_fromUtf8("overwrite"))
        self.horizontalLayout_4.addWidget(self.overwrite)
        self.resize_btn = QtGui.QPushButton(Dialog)
        self.resize_btn.setObjectName(_fromUtf8("resize_btn"))
        self.horizontalLayout_4.addWidget(self.resize_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_2, 5, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_2.setText(_translate("Dialog", "Size:", None))
        self.label.setText(_translate("Dialog", "X", None))
        self.browse_btn.setText(_translate("Dialog", "Browse", None))
        self.overwrite.setText(_translate("Dialog", "Overwrite output", None))
        self.resize_btn.setText(_translate("Dialog", "resize", None))

import images_rc
