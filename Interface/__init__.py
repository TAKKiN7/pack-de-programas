from customtkinter import *
from PIL import Image
from pathlib import Path
from Interface.Navegadores import NavegadoresFrame
from Interface.Menu import Menu
from time import sleep as pause

class App(CTk):
    def __init__(self):
        super().__init__()
        self.caminho : Path = Path.cwd() / "Imagens" 
        self.config()
        self.layout()


    def config(self):
        self.overrideredirect(True)

        self.title(" " * 110 + "PACK DE PROGRAMAS")
        self.iconbitmap(self.caminho / "logo/Logo.ico")

        largura = 450
        altura = 300

        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()

        x = (largura_tela // 2) - (largura // 2)
        y = (altura_tela // 2) - (altura // 2)
    
        self.geometry(f"{largura}x{altura}+{x}+{y}")

    
    def layout(self):
        self.fundo()
        self.after(3000, self.menu)




    def fundo(self):
        img = Image.open(self.caminho / "Inicio/fundo_inicial2.png")
        imagem = CTkImage(img, size=(450, 300))
        imagemL = CTkLabel(self, text="", image=imagem)

        imagemL.place(relx=0, rely=0, relheight=1, relwidth=1)



    def menu(self):
        self.frame_menu : Menu = Menu(self)
        self.overrideredirect(False)

        largura = 900
        altura = 600

        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()

        x = (largura_tela // 2) - (largura // 2)
        y = (altura_tela // 2) - (altura // 2)
    

        self.geometry(f"{largura}x{altura}+{x}+{y}")
        self.minsize(largura, altura)
        self.maxsize(largura, altura)





    def start(self):
        self.mainloop()