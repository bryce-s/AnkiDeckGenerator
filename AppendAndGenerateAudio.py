import sys
import os
from gtts import gTTS
import csv
import json
import uuid
import genanki
import shutil
import random


class CardInfo:
    frontText = ""
    backText = ""
    frontAudio = ""
    backAudio = ""
    def __init__(self, frontText: str, backText: str, frontAudio: str, backAudio: str):
        self.frontText = frontText
        self.backText = backText
        self.frontAudio = frontAudio
        self.backAudio = backAudio

class AudioGenerator:

    def __init__(self, filename: str = "input.csv"):
        self.filename: str = filename
        self.outputDir = "./output/"
        self.frontLanguage: str = ""
        self.backLanguage: str = ""
        self.assignFrontAndBackLanguages()
        self.createAudioOutputDir()
        self.cardAudioStore: list = list()
        self.model = None
        self.mediaFilePaths: list = list()

    def assignFrontAndBackLanguages(self):
        with open("settings.json") as settingsFile:
            jsonStr: str = settingsFile.read()
            languages: dict = json.loads(jsonStr)
            self.frontLanguage = languages["front-language"]
            self.backLanguage = languages["back-language"]

    def createAudioOutputDir(self):
        """delete and re-create output dir.. otherwise just create it"""
        if os.path.isdir(self.outputDir):
            shutil.rmtree(self.outputDir)
        os.mkdir(self.outputDir)


    def generateAudio(self):
        with open(self.filename) as f:
            csvReader = csv.reader(f, delimiter='|')
            rowNum = 0
            for row in csvReader:
                rowNum += 1
                frontSide: str = row[0]
                backSide: str = row[1]
                print(f'row {str(rowNum)}: front: {frontSide}, back: {backSide}')
                try:
                    frontAudio = gTTS(text=frontSide, lang=self.frontLanguage, slow=False)
                    backAudio = gTTS(text=backSide, lang=self.backLanguage, slow=False)
                except AssertionError:
                    print(AssertionError)
                    print("Probably input is malformatted. Check line {}".format(str(rowNum)))
                    exit(1)

                # the filenames have to be unique--what can we do here?
                frontUUID: str = uuid.uuid1()
                frontFilename: str = "{}.mp3".format(frontUUID)

                backUUID: str = uuid.uuid1()
                backFilename: str = "{}.mp3".format(backUUID)
                frontAudioPath = "{}{}".format(self.outputDir, frontFilename)
                frontAudio.save(frontAudioPath)
                backAudioPath = "{}{}".format(self.outputDir, backFilename)
                backAudio.save(backAudioPath)
                self.mediaFilePaths.append(frontAudioPath)
                self.mediaFilePaths.append(backAudioPath)
                self.cardAudioStore.append(CardInfo(frontSide, backSide, frontFilename, backFilename))
    
    def __buildGenankiModel(self):
        cssStr=".card { text-align: center; font-size: 24px; }"
        self.model = genanki.Model(
                    1607392219,
                    'Simple Model',
                    css=cssStr,
                    fields=[
                      {'name': 'Question'},
                      {'name': 'FrontAudio'},
                      {'name': 'Answer'},
                      {'name': 'BackAudio'}
                    ],
                    templates=[
                      {
                          'name': 'Card 1',
                          'qfmt': '{{Question}}<br>{{FrontAudio}}',
                          'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}<br>{{BackAudio}}',
                        },
                    ])

    def buildGenankiDeck(self, name:str, filename: str, mirror: bool):
        self.__buildGenankiModel()
        deckID: int = random.randrange(1 << 30, 1 << 31)
        newDeck = genanki.Deck(deckID, name)
        for cardInfo in self.cardAudioStore:
            newDeck.add_note(genanki.Note(model=self.model, fields=[
                cardInfo.frontText, 
                "[sound:{}]".format(cardInfo.frontAudio), 
                cardInfo.backText, 
                ""
                ]
                ))
        if mirror:
            for cardInfo in self.cardAudioStore:
                newDeck.add_note(genanki.Note(model=self.model, fields=[
                    cardInfo.backText, 
                    "",
                    cardInfo.frontText, 
                    "[sound:{}]".format(cardInfo.frontAudio)]))
        pack = genanki.Package(newDeck)
        pack.media_files = self.mediaFilePaths
        pack.write_to_file(name + '.apkg')

def printUsageAndExit():
        print("USAGE: AppendAndGenerate.py input.csv mirror:true kapitalEins")
        exit(1) 

if __name__ == "__main__":
    if len(sys.argv) != 4:
        printUsageAndExit()
    mirror: bool = False
    if (sys.argv[2] != "mirror:true" and sys.argv[2] != "mirror:false"):
        printUsageAndExit()
    
    if (sys.argv[2] == "mirror:true"):
        mirror = True

    name: str = sys.argv[3]

    file: str = sys.argv[1]
    gen: AudioGenerator = AudioGenerator(file)
    gen.generateAudio()
    gen.buildGenankiDeck(name, file, mirror)

