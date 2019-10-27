import sys
import os
from gtts import gTTS
import csv
import json


class AudioGenerator:

    def __init__(self, filename: str = "input.csv"):
        self.filename: str = filename
        self.outputDir = "./output/"
        self.frontLanguage: str = ""
        self.backLanguage: str = ""
        self.assignFrontAndBackLanguages()
        self.createAudioOutputDir()

    def assignFrontAndBackLanguages(self):
        with open("settings.json") as settingsFile:
            jsonStr: str = settingsFile.read()
            languages: dict = json.loads(jsonStr)
            self.frontLanguage = languages["front-language"]
            self.backLanguage = languages["back-language"]

    def createAudioOutputDir(self):
        """delete and re-create output dir.. otherwise just create it"""
        if os.path.isdir(self.outputDir):
            os.rmdir(self.outputDir)
        os.mkdir(self.outputDir)


    def generateAudio(self):
        with open(self.filename) as f:
            csvReader = csv.reader(f, delimiter=',')
            rowNum = 0
            for row in csvReader:
                frontSide: str = row[0]
                backSide: str = row[1]
                print(f'row {str(rowNum)}: front: {frontSide}, back: {backSide}')
                frontAudio = gTTS(text=frontSide, lang=self.frontLanguage, slow=False)
                backAudio = gTTS(text=backSide, lang=self.backLanguage, slow=False)
                
                # the filenames have to be unique--what can we do here?

    


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: AppendAndGenerate.py input.csv")
        exit(1)
    file: str = sys.argv[1]
    gen: AudioGenerator = AudioGenerator(file)
    gen.generateAudio()

