from customtkinter import CTkFrame, CTkButton, CTkImage, CTkLabel
from PIL import Image
from pathlib import Path
from Interface.Navegadores import NavegadoresFrame
from Interface.Antivirus import AntivirusFrame
from Interface.Codec import CodecFrame
from Interface.Comunicacao import ComunicacaoFrame
from Interface.Lojas import LojasFrame
from Interface.Diagnosticos import DiagnosticosFrame
from Interface.Drivers import DriversFrame
from Interface.Office import OfficeFrame
from Interface.Zip import ZipFrame
from Interface.Dependencias import DependenciasFrame
from Interface.Utilitarios import UtilitariosFrame
from Interface.VPN import VPNFrame


class Menu(CTkFrame):
    caminho_imagens : Path = Path.cwd() / Path("Imagens/Menu")
    

    def __init__(self, master):
        super().__init__(master, fg_color="BLACK", corner_radius=0, border_color="BLACK", border_width=2, bg_color="BLACK")
        self.layout()
        



    def layout(self):
        self.fundo()
        self.button_antivirus()
        self.button_codec()
        self.button_comunicacao()
        self.button_navegadores()
        self.button_dependencias()
        self.button_office()
        self.button_diagnosticos()
        self.button_drivers()
        self.button_lojas()
        self.button_utils()
        self.button_vpn()
        self.button_zip()
        self.button_ativacao()



        self.place(relx=0, rely=0, relwidth=1, relheight=1)


    def fundo(self):
        img = Image.open(self.caminho_imagens / "fundo.png")
        imagem = CTkImage(img, size=(900, 600))
        imagemL = CTkLabel(self, text="", image=imagem)

        imagemL.place(relx=0, rely=0, relheight=1, relwidth=1)



    def button_antivirus(self):
        img_normal = Image.open(self.caminho_imagens / "antivirus_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho_imagens / "antivirus_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        self.antivirus_button : CTkButton = CTkButton(self, text="", fg_color="#5CB86A", hover_color="#5CB86A", corner_radius=0, border_color="BLACK", border_width=2, bg_color="BLACK", image=imagem_normal,
                                              command=self.aba_antivirus)
        
        self.antivirus_button.bind("<Enter>", lambda event: self.button_selected(event, self.antivirus_button, imagem_selected))
        self.antivirus_button.bind("<Leave>", lambda event: self.button_normal(event, self.antivirus_button, imagem_normal))

        self.antivirus_button.place(relx=.02, rely=.1, relwidth=.155, relheight=.06)


    def aba_antivirus(self):
        antivirus_frame : AntivirusFrame = AntivirusFrame(self)



    def button_codec(self):
        img_normal = Image.open(self.caminho_imagens / "codec_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho_imagens / "codec_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#B33436", hover_color="#B33436", bg_color="BLACK", corner_radius=0, border_color="BLACK", border_width=2, image=imagem_normal,
                                              command=self.aba_codec)
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal))

        chrome_button.place(relx=.02, rely=.17, relwidth=.155, relheight=.06)
    

    def aba_codec(self):
        codec_frame : CodecFrame = CodecFrame(self)

    def button_comunicacao(self):
        img_normal = Image.open(self.caminho_imagens / "comunicacao_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho_imagens / "comunicacao_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#D9D9D9", hover_color="#D9D9D9", corner_radius=0, border_color="BLACK", border_width=2, bg_color="BLACK", image=imagem_normal,
                                              command=self.aba_comunicacao)
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal))

        chrome_button.place(relx=.02, rely=.24, relwidth=.155, relheight=.06)
    

    def aba_comunicacao(self):
        comu_frame : ComunicacaoFrame = ComunicacaoFrame(self)
    

    def button_navegadores(self):
        img_normal = Image.open(self.caminho_imagens / "navegadores_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho_imagens / "navegadores_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#37B2FF", hover_color="#37B2FF", bg_color="BLACK", corner_radius=0, border_color="BLACK", border_width=2, image=imagem_normal,
                                              command=self.aba_nav)
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal))

        chrome_button.place(relx=.02, rely=.31, relwidth=.155, relheight=.06)


    def aba_nav(self):
        frame_navegadores : NavegadoresFrame = NavegadoresFrame(self)

    def button_dependencias(self):
        img_normal = Image.open(self.caminho_imagens / "depends_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho_imagens / "depends_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#C7C7C7", hover_color="#C7C7C7", corner_radius=0, border_color="BLACK", bg_color="BLACK", border_width=2, image=imagem_normal,
                                              command=self.aba_depends)
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal))

        chrome_button.place(relx=.02, rely=.38, relwidth=.155, relheight=.06)
    

    def aba_depends(self):
        depends_frame : DependenciasFrame = DependenciasFrame(self)
    


    def button_office(self):
        img_normal = Image.open(self.caminho_imagens / "office_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho_imagens / "office_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#FF5353", hover_color="#FF5353", bg_color="BLACK", corner_radius=0, border_color="BLACK", border_width=2, image=imagem_normal,
                                              command=self.aba_office)
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal))

        chrome_button.place(relx=.02, rely=.45, relwidth=.155, relheight=.06)

    
    def aba_office(self):
        office_frame : OfficeFrame = OfficeFrame(self)


    
    def button_diagnosticos(self):
        img_normal = Image.open(self.caminho_imagens / "diagnosticos_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho_imagens / "diagnosticos_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#AFBE3F", hover_color="#AFBE3F", corner_radius=0, border_color="BLACK", border_width=2, bg_color="BLACK", image=imagem_normal,
                                              command=self.aba_diagnosticos)
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected, direita=True))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal, direita=True))

        chrome_button.place(relx=.825, rely=.1, relwidth=.155, relheight=.06)
    

    def aba_diagnosticos(self):
        diagnosticos_frame : DiagnosticosFrame = DiagnosticosFrame(self)


    def button_drivers(self):
        img_normal = Image.open(self.caminho_imagens / "drivers_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho_imagens / "drivers_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#D9D9D9", hover_color="#D9D9D9", corner_radius=0, border_color="BLACK", border_width=2, bg_color="BLACK", image=imagem_normal,
                                              command=self.aba_drivers)
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected, direita=True))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal, direita=True))

        chrome_button.place(relx=.825, rely=.17, relwidth=.155, relheight=.06)
    

    def aba_drivers(self):
        drivers_frame : DriversFrame = DriversFrame(self)


    def button_lojas(self):
        img_normal = Image.open(self.caminho_imagens / "lojas_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho_imagens / "lojas_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#F0CA2F", hover_color="#F0CA2F", corner_radius=0, border_color="BLACK", border_width=2, bg_color="BLACK", image=imagem_normal,
                                              command=self.aba_jogos)
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected, direita=True))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal, direita=True))

        chrome_button.place(relx=.825, rely=.24, relwidth=.155, relheight=.06)
    

    
    def aba_jogos(self):
        jogos_frame : LojasFrame = LojasFrame(self)
    

    def button_utils(self):
        img_normal = Image.open(self.caminho_imagens / "utilitarios_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho_imagens / "utilitarios_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#4E28C0", hover_color="#4E28C0", corner_radius=0, border_color="BLACK", border_width=2, bg_color="BLACK", image=imagem_normal,
                                              command=self.aba_utils)
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected, direita=True))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal, direita=True))

        chrome_button.place(relx=.825, rely=.31, relwidth=.155, relheight=.06)



    def aba_utils(self):
        utils_frame : UtilitariosFrame = UtilitariosFrame(self)
    
    def button_vpn(self):
        img_normal = Image.open(self.caminho_imagens / "vpn_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho_imagens / "vpn_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#C7C7C7", hover_color="#C7C7C7", corner_radius=0, border_color="BLACK", border_width=2, bg_color="BLACK", image=imagem_normal,
                                              command=self.aba_vpn)
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected, direita=True))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal, direita=True))

        chrome_button.place(relx=.825, rely=.38, relwidth=.155, relheight=.06)
    
    def aba_vpn(self):
        vpn_frame : VPNFrame = VPNFrame(self)
    

    def button_zip(self):
        img_normal = Image.open(self.caminho_imagens / "zip_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho_imagens / "zip_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#C266D9", hover_color="#C266D9", corner_radius=0, border_color="BLACK", border_width=2, bg_color="BLACK", image=imagem_normal,
                                              command=self.aba_zip)
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected, direita=True))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal, direita=True))

        chrome_button.place(relx=.825, rely=.45, relwidth=.155, relheight=.06)
    
    def aba_zip(self):
        zip_frame : ZipFrame = ZipFrame(self)


    def button_ativacao(self):
        img_normal = Image.open(self.caminho_imagens / "ativacao_normal.png")
        imagem_normal = CTkImage(img_normal, size=(130, 36))

        img_selected = Image.open(self.caminho_imagens / "ativacao_selected.png")
        imagem_selected = CTkImage(img_selected, size=(130, 36))

        chrome_button : CTkButton = CTkButton(self, text="", fg_color="#FFA82F", hover_color="#FFA82F", corner_radius=0, border_color="BLACK", border_width=2, bg_color="BLACK", image=imagem_normal,
                                              command=lambda: self.baixar("brave"))
        
        chrome_button.bind("<Enter>", lambda event: self.button_selected(event, chrome_button, imagem_selected, direita=True))
        chrome_button.bind("<Leave>", lambda event: self.button_normal(event, chrome_button, imagem_normal, direita = True))

        chrome_button.place(relx=.825, rely=.87, relwidth=.155, relheight=.06)




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
        
