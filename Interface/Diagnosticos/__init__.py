from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkImage, CTkProgressBar
from threading import Thread
from pathlib import Path
from PIL import Image
from services import downloader


class DiagnosticosFrame(CTkFrame):
    def __init__(self, master : CTk):
        super().__init__(master, fg_color="BLACK")
        self.caminho : Path = Path.cwd() / "Imagens/Diagnosticos"
        self.layout()
    

    def layout(self):
        self.fundo()
        self.button_voltar()
        self.button_aida()
        self.button_cpu()
        self.button_gpu()
        self.button_furmark()
        self.button_msi()
        self.button_hd()
        self.button_crystal_x64()
        self.button_crystal_x86()

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


    

    def button_aida(self):
        img_normal = Image.open(self.caminho / "aida_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho / "aida_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#FF5555", hover_color="#FF5555", bg_color="BLACK", corner_radius=0, border_color="BLACK", border_width=2, image=imagem_normal,
                                              command=lambda: self.baixar("aida64"))
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal))

        chrome_button.place(relx=.02, rely=.2, relwidth=.155, relheight=.06)
    

    def button_cpu(self):
        img_normal = Image.open(self.caminho / "cpu_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho / "cpu_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#E355FF", hover_color="#E355FF", bg_color="BLACK", corner_radius=0, border_color="BLACK", border_width=2, image=imagem_normal,
                                              command=lambda: self.baixar("cpu_z"))
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal))

        chrome_button.place(relx=.02, rely=.27, relwidth=.155, relheight=.06)
    

    def button_gpu(self):
        img_normal = Image.open(self.caminho / "gpu_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho / "gpu_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#79D757", hover_color="#79D757", bg_color="BLACK", corner_radius=0, border_color="BLACK", border_width=2, image=imagem_normal,
                                              command=lambda: self.baixar("gpu_z"))
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal))

        chrome_button.place(relx=.02, rely=.34, relwidth=.155, relheight=.06)
    

    def button_furmark(self):
        img_normal = Image.open(self.caminho / "furmark_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho / "furmark_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#9C2B2B", hover_color="#9C2B2B", bg_color="BLACK", corner_radius=0, border_color="BLACK", border_width=2, image=imagem_normal,
                                              command=lambda: self.baixar("fur_mark"))
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected, direita=True))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal, direita=True))

        chrome_button.place(relx=.825, rely=.2, relwidth=.155, relheight=.06)


    def button_msi(self):
        img_normal = Image.open(self.caminho / "msi_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho / "msi_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#2F3C2C", hover_color="#2F3C2C", bg_color="BLACK", corner_radius=0, border_color="BLACK", border_width=2, image=imagem_normal,
                                              command=lambda: self.baixar("msi_afterburner"))
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected, direita=True))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal, direita=True))

        chrome_button.place(relx=.825, rely=.27, relwidth=.155, relheight=.06)
    

    def button_crystal_x64(self):
        img_normal = Image.open(self.caminho / "crystal_x64_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho / "crystal_x64_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#6A8CFB", hover_color="#6A8CFB", bg_color="BLACK", corner_radius=0, border_color="BLACK", border_width=2, image=imagem_normal,
                                              command=lambda: self.baixar("DiskMark64", zip=True))
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected, direita=True))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal, direita=True))

        chrome_button.place(relx=.825, rely=.41, relwidth=.155, relheight=.06)
    

    def button_crystal_x86(self):
        img_normal = Image.open(self.caminho / "crystal_x86_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho / "crystal_x86_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#6A8CFB", hover_color="#6A8CFB", bg_color="BLACK", corner_radius=0, border_color="BLACK", border_width=2, image=imagem_normal,
                                              command=lambda: self.baixar("DiskMark32", zip=True))
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected, direita=True))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal, direita=True))

        chrome_button.place(relx=.825, rely=.48, relwidth=.155, relheight=.06)
    


    def button_hd(self):
        img_normal = Image.open(self.caminho / "hd_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho / "hd_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#2B4084", hover_color="#2B4084", bg_color="BLACK", corner_radius=0, border_color="BLACK", border_width=2, image=imagem_normal,
                                              command=lambda: self.baixar("hdtune"))
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected, direita=True))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal, direita=True))

        chrome_button.place(relx=.825, rely=.34, relwidth=.155, relheight=.06)


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
    

    def baixar2(self, nome_exe=None, label : CTkLabel = None, zip = None):

        caminho = downloader.baixar(nome=nome_exe, progresso=label, zip=zip)

        label.place_forget()

        downloader.executar(caminho, zip=zip)



    def baixar(self, nome_exe=None, zip=False):
        
  
        progressoL : CTkProgressBar = CTkProgressBar(self, mode="determinate", fg_color="BLACK", bg_color="BLACK", border_color="WHITE", border_width=2,
                                                     progress_color="GREEN")
        progressoL.set(0)
        progressoL.place(relx=.0, rely=.97, relwidth=1, relheight=.03)



        thread = Thread(target=self.baixar2, args=(nome_exe, progressoL, zip))
        thread.start()