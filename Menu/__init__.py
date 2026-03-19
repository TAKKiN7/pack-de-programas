from services import Download
from colorama import Fore
import os
import sys



class Menu:
    downloader : Download = Download()
    cores : dict = {
        "g" : Fore.GREEN,
        "r" : Fore.RED,
        "y" : Fore.YELLOW,
        "reset" : Fore.RESET
    }

    categorias: list = ["Antivirus", "Codec", "Comunicação", "Dependencias", "Diagnósticos", "Drivers", "Loja De Jogos", "Navegadores", "Office", "Utilitários", "Vpn", "Compactadores", "Encerrar"]
    programas: dict = {
        "Antivirus": ["avast", "avg"],
        "Codec": ["k_lite", "quick_time", "vlc"],
        "Comunicação": ["discord", "ms_teams"],
        "Dependencias": ["direct_x", "java_x64", "java_x86", "jdk_16_x64"],
        "Diagnósticos": ["aida64", "cpu_z", "fur_mark", "gpu_z", "hdtune", "msi_afterburner"],
        "Drivers": ["ddu", "iobit_uninstaller", "amd_adrenaline", "drive_booster", "nvidia_app"],
        "Loja De Jogos": ["battle_net", "ea_app", "epic_games", "hydra_launcher", "riot_games", "steam", "uplay", "xbox"],
        "Navegadores": ["brave_browser", "google_chrome", "mozila_firefox", "opera_gx"],
        "Office": ["office_x64", "office_x86"],
        "Utilitários": ["disk_defrag", "rufus", "win_to_hdd", "ccleaner", "recuva", "utorrent"],
        "Vpn": ["exit_lag", "hamachi", "radmin", "zero_tier"],
        "Compactadores": ["7z_x32", "7z_x64", "winrar_x86", "winrar_x64"]
    }
    

    def start(self):
        os.system("cls")
        try:
            escolha = self.escolha_categoria()
            lista_programas = self.selecionar_categoria(escolha)
            nome_programa = self.escolher_programa(lista_programas).replace(" ", "_")
            self.baixar_programa(nome_programa)        
        except Exception as e:
            print(f"Erro : {e}")


    def escolha_categoria(self) -> str:
        while True:
            for index, cat in enumerate(self.categorias):
                if index == 12:
                    print(f"0 - {cat}")
                    continue
                print(f"{index + 1} - {cat}")

            try:
                op : int = int(input("opção: "))
            except ValueError:
                print("Opção inválida")
                continue
            else:
                if op > len(self.categorias):
                    print(self.cores["r"], "Valor inválido, tente outra opção.", self.cores["reset"])
                    continue
                elif op == 0:
                    sys.exit()
                return self.categorias[op - 1]
    

    def selecionar_categoria(self, nome_categoria : str) -> list | None:
        categoria : list = self.programas.get(nome_categoria.title())
        if not categoria:
            print("Categoria inixistente ate o momento.")
            return
        return categoria


    def escolher_programa(self, programas : list) -> str:
        while True:
            for index, prg in enumerate(programas):
                print(f"{index + 1} - {prg.title()}")
            try:
                op : int = int(input("opção: "))
            except ValueError:
                print("Opção inválida")
                continue
            else:
                if op > len(programas):
                    print(self.cores["r"], "Valor inválido, tente outra opção.", self.cores["reset"])
                    continue
                return programas[op - 1]
        

    
    def baixar_programa(self, nome_programa):
        executavel = self.downloader.baixar(nome_programa)
        #self.downloader.executar(executavel)