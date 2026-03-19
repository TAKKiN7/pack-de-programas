from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkImage
from pathlib import Path
from PIL import Image
from services import downloader


class AntivirusFrame(CTkFrame):
    def __init__(self, master : CTk):
        super().__init__(master, fg_color="BLACK")
        self.caminho : Path = Path.cwd() / "Imagens"
        self.layout()
    

    def layout(self):
        self.fundo()
        self.voltar_button()


        self.place(relx=0, rely=0, relwidth=1, relheight=1)
    


    def fundo(self):
        img = Image.open(self.caminho / "Antivirus/antivirus_fundo.png")
        imagem = CTkImage(img, size=(900, 600))
        imagemL = CTkLabel(self, text="", image=imagem)

        imagemL.place(relx=0, rely=0, relheight=1, relwidth=1)
    


    def voltar_button(self):
        button_voltar : CTkButton = CTkButton(self, text="Voltar", command=self.voltar)
        button_voltar.place(relx=.05, rely=.05, relwidth=.1)

    def voltar(self):
        self.destroy()