from tkinter import *
from tkinter import ttk
from alarm_clock import Examination
from tkinter import messagebox
from sound import SoundAlarm
from threading import Thread


class MainWindow:
    def draw_main(self):
        self.root = Tk()
        self.root.title("Будильник")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        frm = ttk.Frame(self.root, padding=10)
        frm.grid(sticky="nsew")
        

        frm.columnconfigure(0, weight=1)
        frm.columnconfigure(1, weight=1)
        frm.columnconfigure(2, weight=1)

        greetings = Label(frm, text="Будильник", font=('', 15), fg='white', bg="black")
        greetings.grid(row=0, column=0, columnspan=3, pady=10, sticky="nsew")

        instructions = Label(frm, text="Введите время", font=('', 15), fg='white', bg="black")
        instructions.grid(row=1, column=0, columnspan=3, pady=10, sticky="nsew")

        self.houre = Entry(frm, width=10)
        self.houre.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        colon = Label(frm, text=":", font=('', 15))
        colon.grid(row=2, column=1, padx=10, pady=10)

        self.minutes = Entry(frm, width=10)
        self.minutes.grid(row=2, column=2, padx=10, pady=10, sticky="w")

        launch = Button(frm, text="Завести будильник", 
                        font=('', 15), command=self.__button_processing)
        launch.grid(row=3, column=0, columnspan=3, pady=10)

        self.root.mainloop()
    
        
    def __button_processing(self):
        time = Examination()
        self.go_sound = SoundAlarm()
        try:
            user_houre = self.houre.get()
            user_minute = self.minutes.get()
            self.time_check = time.check(int(user_houre), int(user_minute))
        except:
            messagebox.showerror("Будильник", 
         
                                 "Вы ввели значения которые невозможно представить в виде врмени")
        
        output_stream = Thread(target=self.__ex_sound)
        sound_steram = Thread(target=self.go_sound.run_sound)
        
        output_stream.start()
        sound_steram.start()
    
        
    def __ex_sound(self):
        if self.time_check == True:
            exit_sound = messagebox.askokcancel("Будильник", "ВРЕМЯ! Остановить звук?")
            
        if exit_sound == True:
            self.go_sound.stop_sound()