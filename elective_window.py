# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'elective_window.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import lightstyle

class Ui_elective_window(object):
    def setupUi(self, elective_window):
        elective_window.setObjectName("elective_window")
        elective_window.resize(661, 491)
        elective_window.setStyleSheet(lightstyle.css)
        elective_window.setWindowIcon(QtGui.QIcon('icons/favicon.ico'))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(elective_window.sizePolicy().hasHeightForWidth())
        elective_window.setSizePolicy(sizePolicy)
        elective_window.setMinimumSize(QtCore.QSize(661, 491))
        elective_window.setMaximumSize(QtCore.QSize(661, 491))
        self.centralWidget = QtWidgets.QWidget(elective_window)
        self.centralWidget.setGeometry(QtCore.QRect(0, 0, 661, 492))
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(3, 6, 0, 0)
        self.gridLayout.setHorizontalSpacing(9)
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 10, 1, 1, 1)
        self.elective_short_input = QtWidgets.QLineEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.elective_short_input.sizePolicy().hasHeightForWidth())
        self.elective_short_input.setSizePolicy(sizePolicy)
        self.elective_short_input.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.elective_short_input.setFont(font)
        self.elective_short_input.setObjectName("elective_short_input")
        self.gridLayout.addWidget(self.elective_short_input, 11, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 12, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addBtn = QtWidgets.QPushButton(self.centralWidget)
        self.addBtn.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.addBtn.setFont(font)
        self.addBtn.setObjectName("addBtn")
        self.horizontalLayout.addWidget(self.addBtn)
        self.removeBtn = QtWidgets.QPushButton(self.centralWidget)
        self.removeBtn.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.removeBtn.setFont(font)
        self.removeBtn.setObjectName("removeBtn")
        self.horizontalLayout.addWidget(self.removeBtn)
        self.resetBtn = QtWidgets.QPushButton(self.centralWidget)
        self.resetBtn.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.resetBtn.setFont(font)
        self.resetBtn.setObjectName("resetBtn")
        self.horizontalLayout.addWidget(self.resetBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.backBtn = QtWidgets.QPushButton(self.centralWidget)
        self.backBtn.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.backBtn.setFont(font)
        self.backBtn.setObjectName("backBtn")
        self.horizontalLayout.addWidget(self.backBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 13, 0, 1, 6)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        self.elective_list = QtWidgets.QListWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.elective_list.sizePolicy().hasHeightForWidth())
        self.elective_list.setSizePolicy(sizePolicy)
        self.elective_list.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.elective_list.setFont(font)
        self.elective_list.setAlternatingRowColors(True)
        self.elective_list.setObjectName("elective_list")
        self.gridLayout.addWidget(self.elective_list, 1, 5, 12, 1)
        self.label = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 6, QtCore.Qt.AlignHCenter)
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 10, 2, 1, 1)
        self.credits_spinbox = QtWidgets.QSpinBox(self.centralWidget)
        self.credits_spinbox.setMinimumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.credits_spinbox.setFont(font)
        self.credits_spinbox.setProperty("value", 1)
        self.credits_spinbox.setObjectName("credits_spinbox")
        self.gridLayout.addWidget(self.credits_spinbox, 11, 2, 1, 1)
        self.lab_checkbox = QtWidgets.QCheckBox(self.centralWidget)
        self.lab_checkbox.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.lab_checkbox.setFont(font)
        self.lab_checkbox.setObjectName("lab_checkbox")
        self.gridLayout.addWidget(self.lab_checkbox, 11, 3, 1, 1)
        self.semester_combobox = QtWidgets.QComboBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.semester_combobox.sizePolicy().hasHeightForWidth())
        self.semester_combobox.setSizePolicy(sizePolicy)
        self.semester_combobox.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.semester_combobox.setFont(font)
        self.semester_combobox.setObjectName("semester_combobox")
        self.gridLayout.addWidget(self.semester_combobox, 3, 1, 1, 1)
        self.electiveGroup_combobox = QtWidgets.QComboBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.electiveGroup_combobox.sizePolicy().hasHeightForWidth())
        self.electiveGroup_combobox.setSizePolicy(sizePolicy)
        self.electiveGroup_combobox.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.electiveGroup_combobox.setFont(font)
        self.electiveGroup_combobox.setObjectName("electiveGroup_combobox")
        self.gridLayout.addWidget(self.electiveGroup_combobox, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 1, 1, 1)
        self.elective_spinbox = QtWidgets.QSpinBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.elective_spinbox.sizePolicy().hasHeightForWidth())
        self.elective_spinbox.setSizePolicy(sizePolicy)
        self.elective_spinbox.setMinimumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.elective_spinbox.setFont(font)
        self.elective_spinbox.setProperty("value", 1)
        self.elective_spinbox.setObjectName("elective_spinbox")
        self.gridLayout.addWidget(self.elective_spinbox, 6, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(110, 0))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setMinimumSize(QtCore.QSize(0, 0))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 0, 1, 5)
        self.line_2 = QtWidgets.QFrame(self.centralWidget)
        self.line_2.setMinimumSize(QtCore.QSize(0, 0))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 7, 0, 1, 5)
        self.elective_input_textbox = QtWidgets.QLineEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.elective_input_textbox.sizePolicy().hasHeightForWidth())
        self.elective_input_textbox.setSizePolicy(sizePolicy)
        self.elective_input_textbox.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.elective_input_textbox.setFont(font)
        self.elective_input_textbox.setObjectName("elective_input_textbox")
        self.gridLayout.addWidget(self.elective_input_textbox, 9, 1, 1, 4)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.actionSave = QtWidgets.QAction(elective_window)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtWidgets.QAction(elective_window)
        self.actionLoad.setObjectName("actionLoad")
        self.actionExit = QtWidgets.QAction(elective_window)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(elective_window)
        self.actionAbout.setObjectName("actionAbout")

        self.retranslateUi(elective_window)
        QtCore.QMetaObject.connectSlotsByName(elective_window)
        elective_window.setTabOrder(self.semester_combobox, self.elective_spinbox)
        elective_window.setTabOrder(self.elective_spinbox, self.electiveGroup_combobox)
        elective_window.setTabOrder(self.electiveGroup_combobox, self.elective_input_textbox)
        elective_window.setTabOrder(self.elective_input_textbox, self.elective_short_input)
        elective_window.setTabOrder(self.elective_short_input, self.credits_spinbox)
        elective_window.setTabOrder(self.credits_spinbox, self.lab_checkbox)
        elective_window.setTabOrder(self.lab_checkbox, self.addBtn)
        elective_window.setTabOrder(self.addBtn, self.elective_list)
        elective_window.setTabOrder(self.elective_list, self.removeBtn)
        elective_window.setTabOrder(self.removeBtn, self.resetBtn)
        elective_window.setTabOrder(self.resetBtn, self.backBtn)

    def retranslateUi(self, elective_window):
        _translate = QtCore.QCoreApplication.translate
        elective_window.setWindowTitle(_translate("elective_window", "TimeTable Generator - Elective Entry"))
        self.label_5.setText(_translate("elective_window", "Elective Name:"))
        self.label_6.setText(_translate("elective_window", "Elective short form:"))
        self.addBtn.setText(_translate("elective_window", "Add"))
        self.removeBtn.setText(_translate("elective_window", "Remove"))
        self.resetBtn.setText(_translate("elective_window", "Reset"))
        self.backBtn.setText(_translate("elective_window", "Back"))
        self.label_2.setText(_translate("elective_window", "Semester:"))
        self.label.setText(_translate("elective_window", "Elective Entry"))
        self.label_7.setText(_translate("elective_window", "Credits:"))
        self.lab_checkbox.setText(_translate("elective_window", "Lab"))
        self.label_3.setText(_translate("elective_window", "Elective Group:"))
        self.label_4.setText(_translate("elective_window", "No.of Elective Groups:"))
        self.actionSave.setText(_translate("elective_window", "Save"))
        self.actionLoad.setText(_translate("elective_window", "Load"))
        self.actionExit.setText(_translate("elective_window", "Exit"))
        self.actionAbout.setText(_translate("elective_window", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    elective_window = QtWidgets.QWidget()
    ui = Ui_elective_window()
    ui.setupUi(elective_window)
    elective_window.show()
    sys.exit(app.exec_())

