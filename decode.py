import os 

while True: 
    file_to_decode = input("Input the path of the file you want to decode:")
    if os.path.exists(file_to_decode):
        break
    else:
        print("File not found.") 
        continue 

fullSentence = ""
decodedSentence = ""
sentenceArray = ['']
wordArray = ['']

with open(file_to_decode, "r") as f: 
    fullSentence = f.read()
    f.close()

if "-" in fullSentence: 
    sentenceArray = fullSentence.split("-")
else: 
    sentenceArray[0] = fullSentence 

for i, sentence in enumerate(sentenceArray):  
    if decodedSentence != "": 
        decodedSentence = decodedSentence + " "
    wordArray = sentence.split(" ")
    for word in wordArray:
        if word.strip():
            decodedSentence = decodedSentence + word[0] 


print(decodedSentence)