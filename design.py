# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_weather_form(object):
    def setupUi(self, weather_form):
        weather_form.setObjectName("weather_form")
        weather_form.resize(368, 485)
        weather_form.setTabletTracking(True)
        weather_form.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon = QtGui.QIcon.fromTheme("image/icon.png")
        weather_form.setWindowIcon(icon)
        weather_form.setWindowOpacity(1.0)
        weather_form.setLayoutDirection(QtCore.Qt.LeftToRight)
        weather_form.setStyleSheet("QWidget{\n"
"background-color: red;\n"
"}")
        self.inputCity = QtWidgets.QLineEdit(weather_form)
        self.inputCity.setGeometry(QtCore.QRect(50, 30, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.inputCity.setFont(font)
        self.inputCity.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.inputCity.setAcceptDrops(False)
        self.inputCity.setStyleSheet("background-color: /*#B8CCD5*/#FCFAF7;\n"
"border-radius: 3px;\n"
"color: #727173;\n"
"padding-left: 6px;\n"
"padding-right: 6px;\n"
"")
        self.inputCity.setInputMethodHints(QtCore.Qt.ImhNone)
        self.inputCity.setInputMask("")
        self.inputCity.setFrame(True)
        self.inputCity.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inputCity.setDragEnabled(False)
        self.inputCity.setReadOnly(False)
        self.inputCity.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.inputCity.setClearButtonEnabled(False)
        self.inputCity.setObjectName("inputCity")
        self.buttonGet = QtWidgets.QPushButton(weather_form)
        self.buttonGet.setGeometry(QtCore.QRect(130, 80, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.buttonGet.setFont(font)
        self.buttonGet.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.buttonGet.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.buttonGet.setAutoFillBackground(False)
        self.buttonGet.setStyleSheet("QPushButton {\n"
"    background-color: /*#B8CCD5*/#FCFAF7;\n"
"    border-radius: 3px;\n"
"    color: #727173;\n"
"    padding-left: 6px;\n"
"    padding-right: 6px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid red;\n"
"    color: red;\n"
"}")
        self.buttonGet.setInputMethodHints(QtCore.Qt.ImhNone)
        self.buttonGet.setCheckable(False)
        self.buttonGet.setAutoRepeat(False)
        self.buttonGet.setAutoExclusive(False)
        self.buttonGet.setAutoRepeatDelay(304)
        self.buttonGet.setObjectName("buttonGet")
        self.text_weather_in_city = QtWidgets.QLabel(weather_form)
        self.text_weather_in_city.setGeometry(QtCore.QRect(-10, 120, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.text_weather_in_city.setFont(font)
        self.text_weather_in_city.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"")
        self.text_weather_in_city.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_weather_in_city.setFrameShadow(QtWidgets.QFrame.Plain)
        self.text_weather_in_city.setTextFormat(QtCore.Qt.AutoText)
        self.text_weather_in_city.setScaledContents(False)
        self.text_weather_in_city.setAlignment(QtCore.Qt.AlignCenter)
        self.text_weather_in_city.setWordWrap(False)
        self.text_weather_in_city.setObjectName("text_weather_in_city")
        self.text_temp = QtWidgets.QLabel(weather_form)
        self.text_temp.setGeometry(QtCore.QRect(20, 190, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(44)
        self.text_temp.setFont(font)
        self.text_temp.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"")
        self.text_temp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_temp.setFrameShadow(QtWidgets.QFrame.Plain)
        self.text_temp.setTextFormat(QtCore.Qt.AutoText)
        self.text_temp.setScaledContents(False)
        self.text_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.text_temp.setWordWrap(False)
        self.text_temp.setObjectName("text_temp")
        self.text_description = QtWidgets.QLabel(weather_form)
        self.text_description.setGeometry(QtCore.QRect(20, 240, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(11)
        self.text_description.setFont(font)
        self.text_description.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"")
        self.text_description.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_description.setFrameShadow(QtWidgets.QFrame.Plain)
        self.text_description.setTextFormat(QtCore.Qt.AutoText)
        self.text_description.setScaledContents(False)
        self.text_description.setAlignment(QtCore.Qt.AlignCenter)
        self.text_description.setWordWrap(False)
        self.text_description.setObjectName("text_description")
        self.frame = QtWidgets.QFrame(weather_form)
        self.frame.setGeometry(QtCore.QRect(-440, -870, 981, 1391))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(440, 1190, 371, 221))
        self.frame_2.setStyleSheet("background: rgba(10,10,10,0.5);\n"
"border-radius: 30;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.text_temp_likes = QtWidgets.QLabel(self.frame_2)
        self.text_temp_likes.setGeometry(QtCore.QRect(10, 50, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.text_temp_likes.setFont(font)
        self.text_temp_likes.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"")
        self.text_temp_likes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_temp_likes.setFrameShadow(QtWidgets.QFrame.Plain)
        self.text_temp_likes.setTextFormat(QtCore.Qt.AutoText)
        self.text_temp_likes.setScaledContents(False)
        self.text_temp_likes.setAlignment(QtCore.Qt.AlignCenter)
        self.text_temp_likes.setWordWrap(False)
        self.text_temp_likes.setObjectName("text_temp_likes")
        self.text_speed_wind = QtWidgets.QLabel(self.frame_2)
        self.text_speed_wind.setGeometry(QtCore.QRect(10, 130, 351, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.text_speed_wind.setFont(font)
        self.text_speed_wind.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"")
        self.text_speed_wind.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_speed_wind.setFrameShadow(QtWidgets.QFrame.Plain)
        self.text_speed_wind.setTextFormat(QtCore.Qt.AutoText)
        self.text_speed_wind.setScaledContents(False)
        self.text_speed_wind.setAlignment(QtCore.Qt.AlignCenter)
        self.text_speed_wind.setWordWrap(False)
        self.text_speed_wind.setObjectName("text_speed_wind")
        self.text_pressure = QtWidgets.QLabel(self.frame_2)
        self.text_pressure.setGeometry(QtCore.QRect(10, 80, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.text_pressure.setFont(font)
        self.text_pressure.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"")
        self.text_pressure.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_pressure.setFrameShadow(QtWidgets.QFrame.Plain)
        self.text_pressure.setTextFormat(QtCore.Qt.AutoText)
        self.text_pressure.setScaledContents(False)
        self.text_pressure.setAlignment(QtCore.Qt.AlignCenter)
        self.text_pressure.setWordWrap(False)
        self.text_pressure.setObjectName("text_pressure")
        self.text_humidity = QtWidgets.QLabel(self.frame_2)
        self.text_humidity.setGeometry(QtCore.QRect(10, 110, 351, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.text_humidity.setFont(font)
        self.text_humidity.setStyleSheet("QLabel {\n"
"    color: white;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"")
        self.text_humidity.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_humidity.setFrameShadow(QtWidgets.QFrame.Plain)
        self.text_humidity.setTextFormat(QtCore.Qt.AutoText)
        self.text_humidity.setScaledContents(False)
        self.text_humidity.setAlignment(QtCore.Qt.AlignCenter)
        self.text_humidity.setWordWrap(False)
        self.text_humidity.setObjectName("text_humidity")
        self.frame.raise_()
        self.inputCity.raise_()
        self.buttonGet.raise_()
        self.text_weather_in_city.raise_()
        self.text_temp.raise_()
        self.text_description.raise_()

        self.retranslateUi(weather_form)
        QtCore.QMetaObject.connectSlotsByName(weather_form)

    def retranslateUi(self, weather_form):
        _translate = QtCore.QCoreApplication.translate
        weather_form.setWindowTitle(_translate("weather_form", "WeatherInYourCity"))
        self.inputCity.setPlaceholderText(_translate("weather_form", "Введите город"))
        self.buttonGet.setText(_translate("weather_form", "Получить"))
        self.text_weather_in_city.setText(_translate("weather_form", "Кемерово"))
        self.text_temp.setText(_translate("weather_form", "56° C"))
        self.text_description.setText(_translate("weather_form", "ОБЛАЧНО С ПРОЯСНЕНИЯМИ"))
        self.text_temp_likes.setText(_translate("weather_form", "По ощущениям 78° C"))
        self.text_speed_wind.setText(_translate("weather_form", "Скорость ветра 34 м/с"))
        self.text_pressure.setText(_translate("weather_form", "Атмосферное давление 749 мм рт. ст."))
        self.text_humidity.setText(_translate("weather_form", "Влажность 33 %"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    weather_form = QtWidgets.QWidget()
    ui = Ui_weather_form()
    ui.setupUi(weather_form)
    weather_form.show()
    sys.exit(app.exec_())
