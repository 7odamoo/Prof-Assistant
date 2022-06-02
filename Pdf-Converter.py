import os
import re
import comtypes.client
from docx2pdf import convert
from PIL import Image

def docx(userInput, userOutput):

    convert(userInput, userOutput)
    
def pptx(userInput, userOutput):

    userInput = os.path.abspath(userInput)
    userOutput = os.path.abspath(userOutput)
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1
    slides = powerpoint.Presentations.Open(userInput)
    slides.SaveAs(userOutput, 32)
    slides.Close()
    
def images(userInput, userOutput):

    image = Image.open(fileNameInput)
    img = image.convert('RGB')
    img.save(fileNameOutput)

def main():

    fileNameInput = input("What is your filename that you want to convert? ")
    
    if not re.search("docx$|pptx$|jpg$|png$|ppt$", fileNameInput):
        print("Sorry, but we are not supported your file that you want to convert it.")
        return
    
    fileNameOutput = input("What do you want me to name your output? ")

    if re.search("docx$", fileNameInput):
        docx(fileNameInput, fileNameOutput)
    
    elif re.search("pptx$|ppt$", fileNameInput):
        pptx(fileNameInput, fileNameOutput)

    elif re.search("jpg$|png$", fileNameInput):
        images(fileNameInput, fileNameOutput)
    
    
if _name_ == '_main_':
    main()
