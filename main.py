import customtkinter 

class TextFrame(customtkinter.CTkFrame):
	def __init__(self, master, **kwargs):
		super().__init__(master, **kwargs)

		self.label = customtkinter.CTkLabel(self, text="MiXT", font=('',70))
		self.label.grid(row=0, column=0, padx=20, pady=20)

		self.info = customtkinter.CTkLabel(self, text="v.alpha.2", font=('',20))
		self.info.grid(row=1, column=0, padx=20, pady=(0,20))

class ButtonsFrame(customtkinter.CTkFrame):
	def __init__(self, master, **kwargs):
		super().__init__(master, **kwargs)

		self.buttonNewProj = customtkinter.CTkButton(self, text="New Project", command=self.but_newproj)
		self.buttonNewProj.grid(row=0, column=0, padx=20, pady=(20,10))

		self.buttonOpenProj = customtkinter.CTkButton(self, text="Open Project")
		self.buttonOpenProj.grid(row=1, column=0, padx=20, pady=(10,10))

		self.buttonsProperties = customtkinter.CTkButton(self, text="Properties")
		self.buttonsProperties.grid(row=2, column=0, padx=20, pady=(10,20))

	def but_newproj(self):
		proj = NewProject(self)

class NewProject(customtkinter.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("New Project")
        self.geometry("380x200")
        self.resizable(False, False)

        self.inputFrame = customtkinter.CTkFrame(master=self)
        self.inputFrame.grid(row=0, column=0, padx=20, pady=(20,10))

        self.name = customtkinter.CTkLabel(self.inputFrame, text="Name")
        self.name.grid(row=0, column=0, padx=(20,10), pady=20)

        self.name_input = customtkinter.CTkEntry(self.inputFrame, placeholder_text="project name")
        self.name_input.grid(row=0, column=1, padx=(10,20), pady=20)

        # ------------- 

        self.btns_Frame = customtkinter.CTkFrame(master=self)
        self.btns_Frame.grid(row=1, column=0, padx=20, pady=(10, 20))

        self.btn_cancel = customtkinter.CTkButton(self.btns_Frame, text="Cancel", command=self.destroy)
        self.btn_cancel.grid(row=1, column=0, padx=(20,10), pady=20)

        self.btn_create = customtkinter.CTkButton(self.btns_Frame, text="Create", command=self.save)
        self.btn_create.grid(row=1, column=1, padx=(10,20), pady=20)

    def save(self):
        self.ProjName = self.name_input.get()
        print(self.ProjName)


class App(customtkinter.CTk):
	def __init__(self):
		super().__init__()
		self.geometry("440x215")
		self.title("MiXT")
		self.resizable(False, False)

		self.menu_frame = TextFrame(master=self)
		self.menu_frame.grid(row=0, column=0, padx=(20,10), pady=20, sticky="nsew")

		self.buttons_frame = ButtonsFrame(master=self)
		self.buttons_frame.grid(row=0, column=1, padx=(10,20), pady=20, sticky="nsew")

app = App()
app.mainloop()