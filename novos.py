import yt_dlp
import getpass
import os
import inquirer
from colorama import init, Style, Fore
from subprocess import run

init()
nome = getpass.getuser()
caio = f"""{nome} aqui tem seu contexto:
    1: para adicionar links de videos so escolher a opçao e colocar os links
    mas agora temos uma nova adiçao, o poder de colocar varios links em sequencia, so adionar um espaço entre eles, a quantidade de espaços entre links nao alteram, e pode ser a quantidade que voce quiser
    ex:(link1 link2     link3   link4  link5) ai enter na quantidade que voce estiver ok
    2: musica=caso quiser so audios
    3: videos=so videos
    4:sair=sair, qeria que fosse o que, hakear o serasa? vdd gostei da ideia caio.
    5: repertório: corrige o pc se o codigo n der certo"""

download_dir = os.path.join(os.path.expanduser(r'~\Downloads'))
os.makedirs(download_dir, exist_ok=True)
user = getpass.getuser()
def musicas():
    link = input("manda os links")
    link = link.split()
    for i in link:
        tube = i
        ydl_opts = {
                'format': r'mp4',
                "outtmpl": os.path.join(download_dir, '%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    }]
                }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(tube)

def repertorio():
    run("winget install Gyan.Ffmpeg")
def videos():
    link = input("manda os links")
    link = link.split()
    for i in link:
        tube = i
        ydl_opts = {
                'format': r'mp4',
                "outtmpl": os.path.join(download_dir, '%(title)s.%(ext)s'),
                }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(tube)

pergunta = [
        inquirer.List(
            "size",
            message = "que tu quer(se nao souber usar clique em enter em 'info'",
            choices = ["info","audio", "video", "sair","limpo","repertorio"]
            )]

while True:
    quer = inquirer.prompt(pergunta)
    if "audio" in str(quer):
        musicas()
        continue
    elif "repertorio" in str(quer):
        repertorio()
        continue
    elif "video" in str(quer):
        videos()
        continue
    elif "sair" in str(quer):
        break
    elif "info" in str(quer):
        print(Fore.GREEN + caio)
        continue
    elif "limpo" in str(quer):
        print("\n" *  200)
        continue

