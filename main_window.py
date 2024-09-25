from alarm_clock import Examination
from sound import SoundAlarm
from PySide6 import QtWidgets
import threading


class MainWindow:
    def draw_main(self):
        self.app = QtWidgets.QApplication([])
        window = QtWidgets.QWidget()
        window.setWindowTitle("Будильник")
        
        box_of_elements = QtWidgets.QVBoxLayout()
        horizontal_view = QtWidgets.QGridLayout()
        
        greetings = QtWidgets.QLabel("Будильник")
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
        
        window.show()
        self.app.exec()
        
    def click_processing(self):
        user = self.get_user_time()
        if user is not None:
            self.run = threading.Thread(target=self.installation, args=(user[0], user[1],))
            self.run.start()

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
            self.msg.setText("Время! После нажатия кнопки будильник выключится")
            self.msg.buttonClicked.connect(self.stop_alarm)
            self.msg.exec()

    def stop_alarm(self):
        if self.sound_alarm is not None:
            self.sound_alarm.stop_sound()
            self.msg.destroy()
            self.app.exit()
            
            

        
        
        