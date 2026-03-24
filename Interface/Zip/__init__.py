from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkImage, CTkProgressBar
from threading import Thread
from pathlib import Path
from PIL import Image
from services import downloader


class ZipFrame(CTkFrame):
    def __init__(self, master : CTk):
        super().__init__(master, fg_color="BLACK")
        self.caminho : Path = Path.cwd() / "Imagens/Zip"
        self.layout()
    

    def layout(self):
        self.fundo()
        self.button_voltar()
        self.button_winrar_x64()
        self.button_winrar_x86()
        self.button_7z_x64()
        self.button_7z_x86()



        self.place(relx=0, rely=0, relwidth=1, relheight=1)
    


    def fundo(self):
        img = Image.open(self.caminho / "fundo.png")
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
    

    def button_winrar_x64(self):
        img_normal = Image.open(self.caminho / "winrar_x64_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho / "winrar_x64_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#EB8E31", hover_color="#EB8E31", bg_color="BLACK", corner_radius=0, border_color="BLACK", border_width=2, image=imagem_normal,
                                              command=lambda:self.baixar("winrar_x64"))
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal))

        chrome_button.place(relx=.78, rely=.63, relwidth=.155, relheight=.06)
    


    def button_winrar_x86(self):
        img_normal = Image.open(self.caminho / "winrar_x86_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho / "winrar_x86_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#EB8E31", hover_color="#EB8E31", bg_color="BLACK", corner_radius=0, border_color="BLACK", border_width=2, image=imagem_normal,
                                              command=lambda:self.baixar("winrar_x86"))
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal))

        chrome_button.place(relx=.78, rely=.7, relwidth=.155, relheight=.06)

    
    def button_7z_x64(self):
        img_normal = Image.open(self.caminho / "7z_x64_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho / "7z_x64_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#746969", hover_color="#746969", bg_color="BLACK", corner_radius=0, border_color="BLACK", border_width=2, image=imagem_normal,
                                              command=lambda:self.baixar("7z_x64"))
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal))

        chrome_button.place(relx=.78, rely=.77, relwidth=.155, relheight=.06)
    


    def button_7z_x86(self):
        img_normal = Image.open(self.caminho / "7z_x86_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho / "7z_x86_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#746969", hover_color="#746969", bg_color="BLACK", corner_radius=0, border_color="BLACK", border_width=2, image=imagem_normal,
                                              command=lambda:self.baixar("7z_x86"))
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal))

        chrome_button.place(relx=.78, rely=.84, relwidth=.155, relheight=.06)

    def fechar(self):
        self.destroy()
    

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
    

    def baixar2(self, nome_exe=None, label : CTkLabel = None):

        caminho = downloader.baixar(nome=nome_exe, progresso=label)

        label.place_forget()

        downloader.executar(caminho)



    def baixar(self, nome_exe=None):
        
  
        progressoL : CTkProgressBar = CTkProgressBar(self, mode="determinate", fg_color="BLACK", bg_color="BLACK", border_color="WHITE", border_width=2,
                                                     progress_color="GREEN")
        progressoL.set(0)
        progressoL.place(relx=.0, rely=.97, relwidth=1, relheight=.03)



        thread = Thread(target=self.baixar2, args=(nome_exe, progressoL))
        thread.start()
