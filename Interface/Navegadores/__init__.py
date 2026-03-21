from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkImage
from pathlib import Path
from PIL import Image
from services import downloader


class NavegadoresFrame(CTkFrame):
    def __init__(self, master : CTk):
        super().__init__(master, fg_color="BLACK")
        self.caminho : Path = Path.cwd() / "Imagens/Navegadores"
        self.layout()
    

    def layout(self):
        self.fundo()
        self.button_voltar()
        self.button_chrome()
        self.button_opera()
        self.button_firefox()
        self.button_brave()


        self.place(relx=0, rely=0, relwidth=1, relheight=1)
    


    def fundo(self):
        img = Image.open(self.caminho / "nav_fundo.png")
        imagem = CTkImage(img, size=(900, 600))
        imagemL = CTkLabel(self, text="", image=imagem)

        imagemL.place(relx=0, rely=0, relheight=1, relwidth=1)
    

    def button_voltar(self):
        img_normal = Image.open(self.caminho / "voltar_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho / "voltar_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#02692D", hover_color="#02692D", bg_color="BLACK", corner_radius=0, border_color="BLACK", border_width=2, image=imagem_normal,
                                              command=self.fechar)
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal))

        chrome_button.place(relx=.02, rely=.03, relwidth=.155, relheight=.06)


    def button_chrome(self):
        img_normal = Image.open(self.caminho / "chrome_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho / "chrome_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        self.chorme_button : CTkButton = CTkButton(self, text="", fg_color="#55E0FF", hover_color="#55E0FF", corner_radius=0, border_color="BLACK", border_width=2, bg_color="BLACK", image=imagem_normal,
                                              command=lambda: self.baixar("google_chrome"))
        
        self.chorme_button.bind("<Enter>", lambda event: self.button_selected(event, self.chorme_button, imagem_selected))
        self.chorme_button.bind("<Leave>", lambda event: self.button_normal(event, self.chorme_button, imagem_normal))

        self.chorme_button.place(relx=.16, rely=.87, relwidth=.155, relheight=.06)
    

    def button_opera(self):
        img_normal = Image.open(self.caminho / "opera_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho / "opera_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#732728", hover_color="#732728", bg_color="BLACK", corner_radius=0, border_color="BLACK", border_width=2, image=imagem_normal,
                                              command=lambda: self.baixar("opera_gx"))
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal))

        chrome_button.place(relx=.34, rely=.87, relwidth=.155, relheight=.06)
    

    def button_firefox(self):
        img_normal = Image.open(self.caminho / "firefox_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho / "firefox_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#EB8E31", hover_color="#EB8E31", bg_color="BLACK", corner_radius=0, border_color="BLACK", border_width=2, image=imagem_normal,
                                              command=lambda: self.baixar("mozila_firefox"))
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal))

        chrome_button.place(relx=.51, rely=.87, relwidth=.155, relheight=.06)


    def button_brave(self):
        img_normal = Image.open(self.caminho / "brave_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho / "brave_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#737373", hover_color="#737373", bg_color="BLACK", corner_radius=0, border_color="BLACK", border_width=2, image=imagem_normal,
                                              command=lambda: self.baixar("brave_browser"))
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal))

        chrome_button.place(relx=.68, rely=.87, relwidth=.155, relheight=.06)

    

    def button_selected(self, event,  button : CTkButton, imagem : CTkImage, direita = False):
        button.configure(image=imagem, bg_color="WHITE", border_color="WHITE")
        if direita:
            button.place(relwidth=.17, relx=.81)
            return
        button.place(relwidth=.17)

    def button_normal(self, event,  button : CTkButton, imagem : CTkImage, direita = False):
        button.configure(image=imagem, bg_color="BLACK", border_color="BLACK")
        if direita:
            button.place(relwidth=.155, relx=.825)
            return
        button.place(relwidth=.155)
    

    
    def baixar(self, nome_exe=None):
        caminho = downloader.baixar(nome=nome_exe)
        downloader.executar(caminho)

    
    def fechar(self):
        self.destroy()