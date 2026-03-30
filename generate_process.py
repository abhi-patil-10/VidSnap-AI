# This file looks for new folder inside user-uploads and convert them into reel , if they already not coverted 
import os
from text_to_speech import text_to_speech_file
import time

    
def text_to_audio(folder):
    print("TA -",folder)
    with open(os.path.join("user-uploads",folder,"Description.txt") , "r") as file:
        text = file.read()
        
    print(text,folder)
    # text_to_speech_file(text , folder)
    
def create_reel(folder):
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
            if folder not in done_folders:
                text_to_audio(folder)
                create_reel(folder)
                with open("done.txt" , "a") as file:
                        if folder not in done_folders:
                            file.write(folder + "\n")    
                        
        time.sleep(4)    