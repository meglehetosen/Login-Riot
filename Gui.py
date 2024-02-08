import customtkinter
from PIL import Image, ImageTk 
import ctypes
import Acc 
import atexit
import MainFunctions as mf
import keyboard as k
import time as t
import subprocess as sp

class RadiobuttonFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = customtkinter.StringVar(value="")

        self.title_label = customtkinter.CTkLabel(self, text=self.title, fg_color="#6A7D9B", corner_radius=6, font=("Arial", 10))
        self.title_label.grid(row=0, column=0, padx=5, pady=(4, 0), sticky="ew")

        for i, value in enumerate(self.values):
            radiobutton = customtkinter.CTkRadioButton(self, text=value, fg_color="gray30", value=value, variable=self.variable, font=("Arial", 10))
            radiobutton.grid(row=i + 1, column=0, padx=5, pady=(4, 0), sticky="n")
            self.radiobuttons.append(radiobutton)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)

class ToplevelWindow(customtkinter.CTkToplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Add a new account")
        self.geometry("400x300")
        self.geometry("+800+300") 
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)

        self.labelPath = customtkinter.CTkLabel(self, text="Path:")
        self.labelPath.grid(row=1, column=0, padx=(10, 0), sticky="w")
        self.entryPath = customtkinter.CTkEntry(self, placeholder_text=fr"E:\Riot Games\Riot Client\RiotClientServices.exe", width=300)
        self.entryPath.grid(row=1, column=1, padx=(0, 10), sticky="e")
        self.pathError = customtkinter.CTkLabel(self, text="Wrong path format. Use Ctrl+Shift+C for copying!", fg_color="red")

        self.labelUsername = customtkinter.CTkLabel(self, text="Username:")
        self.labelUsername.grid(row=3, column=0, padx=(10, 0), sticky="w")
        self.entryUsername = customtkinter.CTkEntry(self, placeholder_text="Gragor", width=300)
        self.entryUsername.grid(row=3, column=1, padx=(0, 10), sticky="e")
        self.usernameError = customtkinter.CTkLabel(self, text="You can't login without a username!", fg_color="red")

        self.labelPassword = customtkinter.CTkLabel(self, text="Password:")
        self.labelPassword.grid(row=5, column=0, padx=(10, 0), sticky="w")
        self.entryPassword = customtkinter.CTkEntry(self, placeholder_text="Password123", width=300)
        self.entryPassword.grid(row=5, column=1, padx=(0, 10), sticky="e")
        self.passwordError = customtkinter.CTkLabel(self, text="You can't login without a password!", fg_color="red")

        self.saveButton = customtkinter.CTkButton(self, text="Save", width=300, command=lambda: self.saveAcc(app))
        self.saveButton.grid(row=7, column=1, sticky="s")

    @staticmethod
    def isFilled(entry, error, _row):
        cond = True
        if len(entry.get()) == 0:
            error.grid(row=_row, column=1, padx=(0,10), sticky="w")
            cond = False
        else:
            error.configure(text="", fg_color="transparent")
        return cond
            
        
 
    def saveAcc(self, app):
        condPT = True
        if "\\" not in self.entryPath.get():
            self.pathError.grid(row=2, column=1, padx=(0,10), sticky="w")
            condPT = False
        else:
            self.pathError.configure(text="", fg_color="transparent")

        condUN = self.isFilled(self.entryUsername, self.usernameError, 4)
        condPS = self.isFilled(self.entryPassword, self.passwordError, 6)


        allGood = condUN and condPS and condPT
        if allGood:   
            Acc.AccountSave(self.entryPath.get(), self.entryUsername.get(), self.entryPassword.get())

            app.createFrameLol()

            self.destroy() 


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("For some reason riot can't afford to add this feature to the client")
        self.geometry("600x450")
        self.resizable(False, False)
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        customtkinter.set_default_color_theme("blue")

        #Taskbar icon = iconbitmap()
        appID = u'mycompany.myproduct.subproduct.1'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appID)
        self.iconbitmap("images/icon.ico")

        # Create a Canvas widget as the background
        self.canvas = customtkinter.CTkCanvas(self, width=410, height=600)
        self.canvas.grid(row=0, column=0, rowspan=5, sticky="nsew")

        # Load and display the background image on the Canvas
        background_image = Image.open("images/bg.png") 
        self.background_image = ImageTk.PhotoImage(background_image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.background_image)


        def createFrameLol():
            self.frameLol = RadiobuttonFrame(self, "Riot Accounts", values=Acc.returnUsernames())
            self.frameLol.grid(row=0, column=1, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.createFrameLol = createFrameLol
        self.createFrameLol()

        self.toplevel_window = None
        self.buttonAdd = customtkinter.CTkButton(self, text="+", command=self.open_toplevel)
        self.buttonAdd.grid(row=1, column=1, padx=10, pady=10, sticky="n", columnspan=1)

        self.buttonDel = customtkinter.CTkButton(self, text="Delete all accounts", command=self.deleteAllAcc)
        self.buttonDel.grid(row=2, column=1, padx=10, pady=10, sticky="n", columnspan=1)

        self.buttonLogin = customtkinter.CTkButton(self, text="Login", command=self.runMainWThreading)
        self.buttonLogin.grid(row=4, column=1, padx=10, pady=10, sticky="nsew", columnspan=1)

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)
            self.toplevel_window.focus()
        else:
            self.toplevel_window.focus()

    def deleteAllAcc(self):
        Acc.deleteAll()
        self.createFrameLol()


    def Main(self):
        selectedRB = self.frameLol.get()
        
        pathList = Acc.returnPaths()
        unList = Acc.returnUsernames()
        passList = Acc.returnPasswords()
        
        index = 0

        for un in unList:
           if un == selectedRB:
               index = unList.index(selectedRB)
        
        sp.Popen(pathList[index], stdout=sp.PIPE, stderr=sp.PIPE, shell=True)

        t.sleep(6)

        unArea = Image.open("images/usernameArea.png")
        passArea = Image.open("images/passwordArea.png")
        bluePlay = Image.open("images/playBlue.png")

        mf.searchAndClick(unArea)
        k.write(unList[index])

        mf.searchAndClick(passArea)
        k.write(passList[index])

        t.sleep(0.5)
        k.press("enter")

        mf.searchAndClick(bluePlay)

        app.destroy()

    def runMainWThreading(self):
        mf.threadMaker(self.Main)


atexit.register(Acc.close)
app = App()
app.mainloop()
