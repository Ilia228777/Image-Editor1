import customtkinter
import PIL

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.WIDTH = 1080
        self.HEIGHT = 720
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}+{0}+{100}")
        self.title("TriangleSheep")
        self.resizable(False, False)
        self.TABVIEW = customtkinter.CTkTabview(
            master = self,
            width = 150,
            height = 720,
            segmented_button_fg_color = "orange",
            segmented_button_selected_color = "#d36f23",
            segmented_button_selected_hover_color = "#c67538"
        )
        self.TABVIEW.place(x=0, y=0)
        self.FILE = self.TABVIEW.add("Файл")
        self.TOOLS = self.TABVIEW.add("Інструменти")
        self.CURRENT_IMAGE = None# eron don don
        self.IMAGE_LABEL = None



main_app = App()