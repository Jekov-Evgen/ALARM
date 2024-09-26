from alarm_clock import Examination
from sound import SoundAlarm
from PySide6 import QtWidgets, QtCore, QtGui
from app_style import STYLE_LABEL, STYLE_ENTRY, STYLE_COLON, STYLE_BUTTON, STYLE_MESSAGEBOX


class MainWindow:
    def draw_main(self):
        self.app = QtWidgets.QApplication([])
        window = QtWidgets.QWidget()
        window.setWindowTitle("Будильник")
        icon = QtGui.QIcon("icon.ico")
        window.setWindowIcon(icon)
        
        box_of_elements = QtWidgets.QVBoxLayout()
        horizontal_view = QtWidgets.QGridLayout()
        
        greetings = QtWidgets.QLabel("Будильник")
        greetings.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        
        time_setting = QtWidgets.QPushButton("Завести время")
        self.hours = QtWidgets.QLineEdit()
        colon = QtWidgets.QLabel(":")
        self.minute = QtWidgets.QLineEdit()
        
        horizontal_view.addWidget(self.hours, 1, 0)
        horizontal_view.addWidget(colon, 1, 1)
        horizontal_view.addWidget(self.minute, 1, 2)
        
        box_of_elements.addWidget(greetings)
        box_of_elements.addLayout(horizontal_view)
        box_of_elements.addWidget(time_setting)
        
        time_setting.clicked.connect(self.click_processing)
        
        window.setLayout(box_of_elements)
        
        greetings.setStyleSheet(STYLE_LABEL)
        colon.setStyleSheet(STYLE_COLON)
        self.hours.setStyleSheet(STYLE_ENTRY)
        self.minute.setStyleSheet(STYLE_ENTRY)
        time_setting.setStyleSheet(STYLE_BUTTON)
        
        window.show()
        self.app.exec()
        
    def click_processing(self):
        user = self.get_user_time()
        self.installation(user[0], user[1])

    def get_user_time(self):
        try:
            hour = int(self.hours.text())
            minute = int(self.minute.text())
            return [hour, minute]
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setText("Вводить можно только числа")
            msg.exec()
            return None

    def installation(self, hour, minute):
        control = Examination()
        time_up = control.check(hour, minute)
        if time_up:
            self.sound_alarm = SoundAlarm()
            self.sound_alarm.run_sound()
            
            self.msg = QtWidgets.QMessageBox()
            self.msg.setStyleSheet(STYLE_MESSAGEBOX)
            icon = QtGui.QIcon("icon.ico")
            self.msg.setWindowIcon(icon)
            self.msg.setText("Время! После нажатия кнопки будильник выключится")
            self.msg.buttonClicked.connect(self.stop_alarm)
            self.msg.exec()

    def stop_alarm(self):
        if self.sound_alarm is not None:
            self.sound_alarm.stop_sound()
            self.msg.destroy()
            
            

        
        
        