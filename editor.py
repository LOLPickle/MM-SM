import customtkinter as ctk

# Налаштування теми
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class MiXTEditor(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MiXT Engine - Editor")
        self.geometry("1100x700")

        # Налаштування сітки (Grid) 
        # 0 - ліва панель, 1 - центр (viewport), 2 - права панель
        self.grid_columnconfigure(1, weight=4)
        self.grid_columnconfigure((0, 2), weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- ЛІВА ПАНЕЛЬ: Ієрархія ---
        self.hierarchy_frame = ctk.CTkFrame(self, corner_radius=0)
        self.hierarchy_frame.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        
        self.hierarchy_label = ctk.CTkLabel(self.hierarchy_frame, text="SCENE HIERARCHY", font=("Roboto", 14, "bold"))
        self.hierarchy_label.pack(pady=10)

        self.obj_list = ctk.CTkScrollableFrame(self.hierarchy_frame, label_text="Objects")
        self.obj_list.pack(expand=True, fill="both", padx=5, pady=5)

        self.add_btn = ctk.CTkButton(self.hierarchy_frame, text="+ Add GameObject", command=self.add_object)
        self.add_btn.pack(pady=10, padx=10, fill="x")

        # --- ЦЕНТРАЛЬНА ПАНЕЛЬ: Viewport ---
        self.viewport_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="#1a1a1a")
        self.viewport_frame.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)
        
        self.viewport_label = ctk.CTkLabel(self.viewport_frame, text="GAME VIEWPORT", text_color="#555555")
        self.viewport_label.place(relx=0.5, rely=0.5, anchor="center")

        # --- ПРАВА ПАНЕЛЬ: Інспектор ---
        self.inspector_frame = ctk.CTkFrame(self, corner_radius=0)
        self.inspector_frame.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)
        
        self.inspector_label = ctk.CTkLabel(self.inspector_frame, text="PROPERTIES", font=("Roboto", 14, "bold"))
        self.inspector_label.pack(pady=10)

        # Приклад полів в інспекторі
        self.name_entry = ctk.CTkEntry(self.inspector_frame, placeholder_text="Object Name")
        self.name_entry.pack(pady=5, padx=10, fill="x")
        
        self.pos_label = ctk.CTkLabel(self.inspector_frame, text="Transform:", anchor="w")
        self.pos_label.pack(padx=10, fill="x")
        
        self.x_pos = ctk.CTkEntry(self.inspector_frame, placeholder_text="X position")
        self.x_pos.pack(pady=2, padx=10, fill="x")
        
        self.y_pos = ctk.CTkEntry(self.inspector_frame, placeholder_text="Y position")
        self.y_pos.pack(pady=2, padx=10, fill="x")

    def add_object(self):
        # Функція для додавання об'єкта в список
        count = len(self.obj_list.winfo_children())
        new_obj = ctk.CTkButton(self.obj_list, text=f"GameObject_{count+1}", fg_color="transparent", anchor="w")
        new_obj.pack(fill="x", pady=2)
        print(f"Added GameObject_{count+1} to scene")

if __name__ == "__main__":
    app = MiXTEditor()
    app.mainloop()