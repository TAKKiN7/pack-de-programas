from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkImage, CTkProgressBar
from threading import Thread
from pathlib import Path
from PIL import Image
from services import downloader


class CodecFrame(CTkFrame):
    def __init__(self, master : CTk):
        super().__init__(master, fg_color="BLACK")
        self.caminho : Path = Path.cwd() / "Imagens/Codec"
        self.layout()
    

    def layout(self):
        self.fundo()
        self.button_voltar()
        self.button_vlc()
        self.button_k_lite()
        self.button_quick()

        self.place(relx=0, rely=0, relwidth=1, relheight=1)

    def fundo(self):
        img = Image.open(self.caminho / "codec_fundo.png")
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
    

    def button_vlc(self):
        img_normal = Image.open(self.caminho / "vlc_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho / "vlc_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        self.chorme_button : CTkButton = CTkButton(self, text="", fg_color="#EFB572", hover_color="#EFB572", corner_radius=0, border_color="BLACK", border_width=2, bg_color="BLACK", image=imagem_normal,
                                              command=lambda: self.baixar("vlc"))
        
        self.chorme_button.bind("<Enter>", lambda event: self.button_selected(event, self.chorme_button, imagem_selected))
        self.chorme_button.bind("<Leave>", lambda event: self.button_normal(event, self.chorme_button, imagem_normal))

        self.chorme_button.place(relx=.02, rely=.3, relwidth=.155, relheight=.06)
    


    def button_k_lite(self):
        img_normal = Image.open(self.caminho / "klite_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho / "klite_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#575FEF", hover_color="#575FEF", bg_color="BLACK", corner_radius=0, border_color="BLACK", border_width=2, image=imagem_normal,
                                              command=lambda: self.baixar("k_lite"))
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal))

        chrome_button.place(relx=.02, rely=.37, relwidth=.155, relheight=.06)

    def button_quick(self):
        img_normal = Image.open(self.caminho / "quick_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho / "quick_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#9C9FCE", hover_color="#9C9FCE", bg_color="BLACK", corner_radius=0, border_color="BLACK", border_width=2, image=imagem_normal,
                                              command=lambda: self.baixar("quick_time"))
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal))

        chrome_button.place(relx=.02, rely=.44, relwidth=.155, relheight=.06)


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
