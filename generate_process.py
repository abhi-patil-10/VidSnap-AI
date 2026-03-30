# This file looks for new folder inside user-uploads and convert them into reel , if they already not coverted 
import os

def create_reel(folder):
    print("CR - ",folder)
    
def text_to_audio(folder):
    print("TA -",folder)

if __name__ == "__main__":
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
                    
        