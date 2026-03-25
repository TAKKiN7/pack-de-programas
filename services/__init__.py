import urllib.request
from pathlib import Path
import subprocess
from links import links
from math import trunc
from colorama import Fore
import zipfile
from tkinter import messagebox as msg
from customtkinter import CTkProgressBar
import ctypes

# caminho : Path = Path.cwd() / "Instaladores"
# caminho.mkdir(exist_ok=True)

# for nome, link in links.items():
#     nome_exe : Path = Path(f"{nome.replace("_", " ")}.exe")
#     caminho_exe = caminho / nome_exe
#     print(f"Downloading {nome.replace("_", " ")}...")
#     urllib.request.urlretrieve(link, caminho_exe)
#     print("Downlonad finalizado!")



class Download:
    cores : dict = {
        "g" : Fore.GREEN,
        "r" : Fore.RED,
        "y" : Fore.YELLOW,
        "reset" : Fore.RESET
    }
     
    def __init__(self):
        caminho : Path = Path.cwd() / "Instaladores"
        caminho.mkdir(exist_ok=True)
        self.links = links
        self.caminho : Path = Path.cwd() / "Instaladores"


    def baixar(self, nome, zip = False, progresso : CTkProgressBar = None):
        link = links.get(nome)
        if not zip:
            nome_exe : Path = Path(f"{nome.replace("_", " ")}.exe")
        else:
            nome_exe : Path = Path(f"{nome.replace("_", " ")}.zip")
        caminho_exe = self.caminho / nome_exe

        exe : Path = Path(caminho_exe)
        try:
            exe.touch(exist_ok=False)
        except:
            print("Executavel ja existe")
            return caminho_exe

        for tentativa in range(3):
            try:
                print("Iniciando download")
                urllib.request.urlretrieve(link, caminho_exe, reporthook=lambda b_baixados, tamanho_b, tamanho_t: self.progresso(b_baixados, tamanho_b, tamanho_t, progresso))
            except:
                print(self.cores["r"], "\nErro ao baixar o arquivo", self.cores["reset"])
            else:
                print(self.cores["g"], "\nDownload concluido", self.cores["reset"])
                break

        return caminho_exe

    def progresso(self, b_baixados, tamanho_b, tamanho_t, progresso : CTkProgressBar = None):
        baixado = b_baixados * tamanho_b
        if tamanho_t > 0:
            porcentagem = baixado / tamanho_t * 100
            print(f"\r{trunc(porcentagem)}%", end="")
            progresso.set(porcentagem / 100)

    
    def executar(self, caminho_exe=None, zip=False):
        if zip:
            with zipfile.ZipFile(caminho_exe, "r") as zip:
                zip.extractall(self.caminho)
        
            caminho_txt = str(caminho_exe)
            caminho_novo = caminho_txt.replace("zip", "exe")
            caminho_exe : Path = Path(caminho_novo)

        try:
            res = ctypes.windll.shell32.ShellExecuteW(
                None,
                "runas",
                rf"{caminho_exe}",
                None,
                None,
                1
            )
            if res <= 32:
                raise FileNotFoundError("Erro ao executar o arquivo.")
            else:
                pass
        except FileNotFoundError:
            try:
                caminho_txt = str(caminho_exe)
                caminho_novo = caminho_txt.replace("exe", "msi")
                caminho_exe : Path = Path(caminho_novo)
                print(caminho_novo)
                print(caminho_exe)
                subprocess.run(["msiexec", "/i", caminho_exe])
            except FileNotFoundError:
                msg.showwarning("Erro", "Arquivo não encontrado!")

            

    def ativar_win10(self):
        txt : str = "irm https://get.activated.win | iex"
        subprocess.run(["powershell", "-Command", txt])


downloader : Download = Download()
