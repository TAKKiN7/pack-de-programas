import urllib.request
from pathlib import Path
import subprocess
from links import links
from math import trunc
from colorama import Fore

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


    def baixar(self, nome):
        link = links.get(nome)
        nome_exe : Path = Path(f"{nome.replace("_", " ")}.exe")
        caminho_exe = self.caminho / nome_exe

        exe : Path = Path(caminho_exe)
        try:
            exe.touch(exist_ok=False)
        except:
            print("Executavel ja existe")
            return caminho_exe

        print("Iniciando download")
        urllib.request.urlretrieve(link, caminho_exe, reporthook=self.progresso)
        print(self.cores["g"], "\nDownload concluido", self.cores["reset"])

        return caminho_exe

    def progresso(self, b_baixados, tamanho_b, tamanho_t):
        baixado = b_baixados * tamanho_b
        if tamanho_t > 0:
            porcentagem = baixado / tamanho_t * 100
            print(f"\r{trunc(porcentagem)}%", end="")

    
    def executar(self, caminho_exe):
        subprocess.run([caminho_exe])


downloader : Download = Download()