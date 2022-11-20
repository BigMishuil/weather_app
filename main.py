import sys
import json
import requests as req
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush
from design import Ui_weather_form
from config import api_token



class MainWindow(QtWidgets.QMainWindow, Ui_weather_form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.init_UI()
        self.frame.setStyleSheet("background-image: url(images/back.jpg);")
        self.text_weather_in_city.hide()
        self.text_temp.hide()
        self.text_description.hide()
        self.text_temp_likes.hide()
        self.text_pressure.hide()
        self.text_humidity.hide()
        self.text_speed_wind.hide()
        self.frame_2.hide()
        self.buttonGet.clicked.connect(self.get_weather)

    def init_UI(self):
        self.setWindowIcon(QIcon('images/icon.png'))

    def get_weather(self, city_name):
            city_name = self.inputCity.text()
            r = req.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_token}&units=metric&lang=ru")
            data = r.json()

            if "message" in data.keys():
                try:
                    if data["cod"] == "404":
                        self.text_weather_in_city.setText("Такой город не существует")

                    elif data["cod"] == "400":
                        self.text_weather_in_city.setText("Вы не ввели город")

                    self.text_temp.setText("--° C")
                    self.text_temp.show()
                    self.text_temp_likes.setText("По ощущениям --° C")
                    self.text_temp_likes.show()
                    self.text_description.setText("------------")
                    self.text_description.show()
                    self.text_pressure.setText("Атмосферное давление --- мм.рт.ст")
                    self.text_pressure.show()
                    self.text_humidity.setText("Влажность --- %")
                    self.text_humidity.show()
                    self.text_speed_wind.setText("Скорость ветра --- м/с")
                    self.text_speed_wind.show()
                    self.frame_2.show()

                except KeyError:
                    self.text_weather_in_city.setText("Ошибка приложения")
                    self.text_temp.hide()
                    self.text_description.hide()
                    self.text_temp_likes.hide()
                    self.text_pressure.hide()
                    self.text_humidity.hide()
                    self.text_speed_wind.hide()
                    self.frame_2.show()

            else:
                try:
                    self.text_weather_in_city.setText(str(data["name"]))
                except KeyError:
                    self.text_weather_in_city.setText("Погода не найдена..")
                finally:
                    self.frame_2.show()
                    self.text_weather_in_city.show()

                try:
                    self.text_temp.setText(str(data["main"]["temp"]) + "° C")
                except KeyError:
                    self.text_temp.setText("--° C")
                finally:
                    self.text_temp.show()

                try:
                    self.text_temp_likes.setText("По ощущениям " + str(data["main"]["feels_like"]) + "° C")
                except KeyError:
                    self.text_temp_likes.setText("По ощущениям --° C")
                finally:
                    self.text_temp_likes.show()

                try:
                    self.text_description.setText(data["weather"][0]["description"])
                except KeyError:
                    self.text_description.setText("------------")
                finally:
                    self.text_description.show()

                try:
                    self.text_pressure.setText(
                        "Атмосферное давление " + str(round(data["main"]["pressure"] * 0.75)) + " мм.рт.ст")
                except KeyError:
                    self.text_pressure.setText("Атмосферное давление --- мм.рт.ст")
                finally:
                    self.text_pressure.show()

                try:
                    self.text_humidity.setText("Влажность " + str(data["main"]["humidity"]) + " %")
                except KeyError:
                    self.text_humidity.setText("Влажность --- %")
                finally:
                    self.text_humidity.show()

                try:
                    self.text_speed_wind.setText("Скорость ветра " + str(data["wind"]["speed"]) + " м/с")
                except KeyError:
                    self.text_speed_wind.setText("Скорость ветра --- м/с")
                finally:
                    self.text_speed_wind.show()


app = QtWidgets.QApplication([])

application = MainWindow()
ui = Ui_weather_form()
application.show()

sys.exit(app.exec_())
