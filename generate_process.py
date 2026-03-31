# This file looks for new folder inside user-uploads and convert them into reel , if they already not coverted 
import os
from text_to_speech import text_to_speech_file
import time
import subprocess
    
def text_to_audio(folder):
    print("TA -",folder)
    with open(os.path.join("user-uploads",folder,"Description.txt") , "r") as file:
        text = file.read()
    print(text,folder)
    text_to_speech_file(text , folder)
    
def create_reel(folder):
    ffmpeg_path = r"C:\Program Files\ffmpeg\bin\ffmpeg.exe"
    
    command = [      
        ffmpeg_path,
        "-f", "concat",
        "-safe", "0",
        "-i", f"user-uploads/{folder}/input.txt",
        "-i", f"user-uploads/{folder}/audio.mp3",
        "-vf",
        "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black",
        "-c:v", "libx264",
        "-c:a", "aac",
        "-shortest",
        "-r", "30",
        "-pix_fmt", "yuv420p",
        f"static/reels/{folder}.mp4"
        ]
   
    subprocess.run(command,check=True)
    print("CR - ",folder)

if __name__ == "__main__":
    while True :
        print("Processing Queue...")
        with open("done.txt", "r") as file:
            done_folders = file.readlines()
            
        folders = os.listdir("user-uploads")
        done_folders = [f.strip() for f in done_folders]
    
    #storing the names of folders which are already converted into reel inside done.txt to avoid duplicate conversion
        for folder in folders:
            # print(folder)
            if folder not in done_folders:
                
                text_to_audio(folder)
                create_reel(folder)
                with open("done.txt" , "a") as file:
                        if folder not in done_folders:
                            file.write(folder + "\n")    
                        
        time.sleep(4)    