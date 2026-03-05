import customtkinter 

class TextFrame(customtkinter.CTkFrame):
	def __init__(self, master, **kwargs):
		super().__init__(master, **kwargs)

		self.label = customtkinter.CTkLabel(self, text="MM&SM", font=('',70))
		self.label.grid(row=0, column=0, padx=20, pady=20)

		self.info = customtkinter.CTkLabel(self, text="v.alpha.1", font=('',20))
		self.info.grid(row=1, column=0, padx=20, pady=(0,20))

class ButtonsFrame(customtkinter.CTkFrame):
	def __init__(self, master, **kwargs):
		super().__init__(master, **kwargs)

		self.buttonNewProj = customtkinter.CTkButton(self, text="New Project")
		self.buttonNewProj.grid(row=0, column=0, padx=20, pady=(20,10))

		self.buttonOpenProj = customtkinter.CTkButton(self, text="Open Project")
		self.buttonOpenProj.grid(row=1, column=0, padx=20, pady=(10,10))

		self.buttonsProperties = customtkinter.CTkButton(self, text="Properties")
		self.buttonsProperties.grid(row=2, column=0, padx=20, pady=(10,20))


class App(customtkinter.CTk):
	def __init__(self):
		super().__init__()
		self.geometry("550x215")
		self.title("MM&SM")
		self.resizable(False, False)

		self.menu_frame = TextFrame(master=self)
		self.menu_frame.grid(row=0, column=0, padx=(20,10), pady=(20,10), sticky="nsew")

		self.buttons_frame = ButtonsFrame(master=self)
		self.buttons_frame.grid(row=0, column=1, padx=(10,20), pady=20, sticky="nsew")

app = App()
app.mainloop()