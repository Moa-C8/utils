from pytube import YouTube
import os
import shutil



def changeOPath():
    outPath = input("path for your .mp3: ")
    return outPath

def dowloadRequest(path):
    url = input("URL de la vidéo : ")
    print("                 -----------------------                         ")
    video = YouTube(url)
    print('Titre :', video.title)
    audio_stream = video.streams.filter(only_audio=True).first()
    out_path = audio_stream.download()
    new_name = os.path.splitext(out_path)[0] +  '.mp3'
    os.rename(out_path, new_name)
    if path != '':
        try:
            shutil.move(new_name,path)
        except:
            path = os.path.dirname(__file__)     
    print(f'Terminé {video.title} telecharger {path}')
    print("                 -----------------------                         ")

path = ''
while True:
    
    print(f'Actual path :{path}')
    print("                 -----------------------                         ")
    Qpath = input('Would you change out path ? (y/n) : ')
    if Qpath == 'y':
        path = changeOPath()
            
    dowloadRequest(path)

    print('\n')
    response = input("Another one ? (y/n) : ")
    print('\n')
    print("                 -----------------------                         ")
    if response.lower() != 'y':
        break
        
