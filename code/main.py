import customtkinter 

class MenuFrame(customtkinter.CTkFrame):
	def __init__(self, master, **kwargs):
		super().__init__(master, **kwargs)

		self.label = customtkinter.CTkLabel(self, text="MM&SM")
		self.label.grid(row=0, column=0, padx=20)

class App(customtkinter.CTk):
	def __init__(self):
		super().__init__()
		self.geometry("600x500")
		self.title("MM&SM")

		self.menu_frame = MenuFrame(master=self)
		self.menu_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


app = App()
app.mainloop()