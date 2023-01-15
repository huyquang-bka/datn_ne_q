# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/layouts/widget_in.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WidgetIn(object):
    def setupUi(self, WidgetIn):
        WidgetIn.setObjectName("WidgetIn")
        WidgetIn.resize(665, 498)
        self.gridLayout = QtWidgets.QGridLayout(WidgetIn)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(WidgetIn)
        self.groupBox_2.setStyleSheet("background-color: rgb(173, 221, 230);\n"
"border-radius: 6px;\n"
"")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.qlabel_frame = QtWidgets.QLabel(self.groupBox_2)
        self.qlabel_frame.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border: 6px;\n"
"border-radius: 6px;")
        self.qlabel_frame.setObjectName("qlabel_frame")
        self.gridLayout_2.addWidget(self.qlabel_frame, 0, 0, 1, 1)
        self.qframe_map = QtWidgets.QFrame(self.groupBox_2)
        self.qframe_map.setStyleSheet("background-color: rgb(255, 255, 255 );\n"
"border: 2px solid black;\n"
"border-radius: 6px;")
        self.qframe_map.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qframe_map.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qframe_map.setObjectName("qframe_map")
        self.gridLayout_2.addWidget(self.qframe_map, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(WidgetIn)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_3.setStyleSheet("background-color: rgb(173, 221, 230);\n"
"border: 2px solid black;\n"
"border-radius: 6px;\n"
"")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.qline_plate_digit = QtWidgets.QLineEdit(self.groupBox_3)
        self.qline_plate_digit.setGeometry(QtCore.QRect(180, 60, 181, 31))
        self.qline_plate_digit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 6px;")
        self.qline_plate_digit.setText("")
        self.qline_plate_digit.setAlignment(QtCore.Qt.AlignCenter)
        self.qline_plate_digit.setPlaceholderText("")
        self.qline_plate_digit.setObjectName("qline_plate_digit")
        self.qline_type_vehicle = QtWidgets.QLineEdit(self.groupBox_3)
        self.qline_type_vehicle.setGeometry(QtCore.QRect(180, 20, 181, 31))
        self.qline_type_vehicle.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 6px;")
        self.qline_type_vehicle.setText("")
        self.qline_type_vehicle.setAlignment(QtCore.Qt.AlignCenter)
        self.qline_type_vehicle.setPlaceholderText("")
        self.qline_type_vehicle.setObjectName("qline_type_vehicle")
        self.qline_slot = QtWidgets.QLineEdit(self.groupBox_3)
        self.qline_slot.setGeometry(QtCore.QRect(180, 99, 181, 31))
        self.qline_slot.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 6px;")
        self.qline_slot.setText("")
        self.qline_slot.setAlignment(QtCore.Qt.AlignCenter)
        self.qline_slot.setPlaceholderText("")
        self.qline_slot.setObjectName("qline_slot")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 31))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 6px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 131, 31))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 6px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 131, 31))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 6px;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.btn_apply = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_apply.setGeometry(QtCore.QRect(20, 150, 341, 32))
        self.btn_apply.setStyleSheet("QPushButton {\n"
"            background-color: rgb(255, 255, 255); \n"
"        }\n"
"QPushButton:pressed {\n"
"            background-color: rgb(127, 127, 127);\n"
"        }")
        self.btn_apply.setObjectName("btn_apply")
        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.retranslateUi(WidgetIn)
        QtCore.QMetaObject.connectSlotsByName(WidgetIn)

    def retranslateUi(self, WidgetIn):
        _translate = QtCore.QCoreApplication.translate
        WidgetIn.setWindowTitle(_translate("WidgetIn", "Form"))
        self.qlabel_frame.setText(_translate("WidgetIn", "TextLabel"))
        self.label.setText(_translate("WidgetIn", "Loại xe"))
        self.label_2.setText(_translate("WidgetIn", "Biển số xe"))
        self.label_3.setText(_translate("WidgetIn", "Chỗ đỗ"))
        self.btn_apply.setText(_translate("WidgetIn", "Chấp nhận"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WidgetIn = QtWidgets.QWidget()
    ui = Ui_WidgetIn()
    ui.setupUi(WidgetIn)
    WidgetIn.show()
    sys.exit(app.exec_())
