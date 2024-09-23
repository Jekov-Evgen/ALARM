from tkinter import *
from tkinter import ttk
from alarm_clock import Examination
from tkinter import messagebox

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
        user_houre = self.houre.get()
        user_minute = self.minutes.get()
        
        self.__eme_app()
        
        self.time_check = time.check(int(user_houre), int(user_minute))
        
        self.__ex_app()
        
    def __ex_app(self):
        if self.time_check == True:
            exit_app = messagebox.askokcancel("Будильник", "ВРЕМЯ! Хотите выйти?")
            
            if exit_app == True:
                self.root.destroy()
                
    def __eme_app(self):
        emergency_exit = messagebox.askyesno("Будильник", 
                            "Вы поставили время. Если хотите выйти заранее нажмите Yes")
        
        if emergency_exit == True:
            self.root.destroy()