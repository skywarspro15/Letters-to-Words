import requests
import os 

str = ""

while True: 
    file_to_decode = input("Input the path of the file you want to decode:")
    if os.path.exists(file_to_decode):
        with open(file_to_decode, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines: 
                str = str + line + " "
            f.close()
        break
    else:
        print("File not found.") 
        continue 

while True: 
    try:
        minLen = input("Word must be longer than:") 
        minLen = int(minLen)
    except ValueError: 
        print("Please enter a valid integer.")
        continue 
    else: 
        break 
        

print("Fetching words...")
r = requests.get("https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt")

with open("words_temp", "w") as f:
    curText = r.text 
    f.write(curText.replace("\n", "\r\n"))
    f.close()

with open("words_temp", "r") as r, open("words", "w") as o: 
    for line in r: 
        if line.strip(): 
            o.write(line)

os.remove("words_temp")

fullSentence = ""
letterFound = False
wordArray = str.split(" ")

for wc, word in enumerate(wordArray):
    for i, letter in enumerate(word):      
        letterFound = False
        if letter == "": 
            fullSentence = fullSentence + "- "
        
        if letter.isalpha() == False: 
            fullSentence = fullSentence + letter + " "
        
        with open("words", "r") as f:
            for line in f: 
                isLetterLower = letter.islower()
                if line.startswith(letter.lower()) and letterFound == False and len(line) > minLen:
                    if isLetterLower: 
                        fullSentence = fullSentence + line.replace("\n", "") + " "
                    else: 
                        fullSentence = fullSentence + line.replace("\n", "").capitalize() + " "
                    letterFound = True
            f.close()
        
        print(f"Generating word {wc + 1}/{len(wordArray)} {int((i / len(word)) * 100)}%")
    
    if wc != len(wordArray) -1:
        fullSentence = fullSentence + "- "

with open("generated", "w") as f: 
    f.write(fullSentence)
    f.close()
