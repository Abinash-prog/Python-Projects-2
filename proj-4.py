# Clear the Clutter

import os
def createIfNotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName,files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")
if __name__ == "__main__": 
    files = os.listdir()
    files.remove("proj-4.py")

    createIfNotExists('Images')
    createIfNotExists('Docs')
    createIfNotExists('Media')
    imgExts = [".png",".jpg",".jpeg",".webp"]
    images = [file for  file in files if os.path.splitext(file)[1].lower() in imgExts]

    docExts = [".txt",".docx",".doc"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]


    mediaExts = [".pdf"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

    move("Media", medias)
    move("Images", images)
    move("Docs", docs)
     
    
    