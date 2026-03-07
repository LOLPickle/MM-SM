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
		result = proj.show()
		if result:
			print(f"New project: {result}")

class NewProject(customtkinter.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("New Project")
        self.geometry("400x300")
        self.resizable(False, False)

        # Головний контейнер (розтягується на все вікно)
        self.main_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # === ФРЕЙМ 1: Назва проекту ===
        self.name_frame = customtkinter.CTkFrame(self.main_frame, fg_color="transparent")
        self.name_frame.pack(fill="x", expand=True)
        
        # Налаштовуємо колонки для фрейму з назвою
        self.name_frame.grid_columnconfigure(0, weight=1)
        self.name_frame.grid_columnconfigure(1, weight=1)
        
        self.label = customtkinter.CTkLabel(
            self.name_frame, 
            text="Name:", 
            width=30,
            font=("Helvetica", 14)
        )
        self.label.grid(row=0, column=0, padx=(0, 10), sticky="e")
        
        self.entry = customtkinter.CTkEntry(
            self.name_frame, 
            width=200, 
            placeholder_text="enter project name"
        )
        self.entry.grid(row=0, column=1, padx=(10, 0), sticky="w")

        # === ФРЕЙМ 2: Кнопки (знизу) ===
        self.button_frame = customtkinter.CTkFrame(self.main_frame, fg_color="transparent")
        self.button_frame.pack(side="bottom", fill="x", pady=(20, 0))
        
        # Налаштовуємо колонки для фрейму з кнопками
        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)
        
        self.save_btn = customtkinter.CTkButton(
            self.button_frame, 
            text="Save", 
            command=self.save,
            fg_color="#2d7a3d",  # зелений
            hover_color="#1e5529"
        )
        self.save_btn.grid(row=0, column=0, padx=(0, 5), sticky="e")
        
        self.cancel_btn = customtkinter.CTkButton(
            self.button_frame, 
            text="Cancel", 
            command=self.destroy,
            fg_color="#a33d3d",  # червоний
            hover_color="#7a2e2e"
        )
        self.cancel_btn.grid(row=0, column=1, padx=(5, 0), sticky="w")
        
        self.result = None

    def save(self):
        self.result = self.entry.get()
        self.destroy()
    
    def show(self):
        self.wait_window()
        return self.result


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