from textblob import TextBlob
with open("transcription.txt","r")as f:
    data=f.read()
sentences=TextBlob(data).sentences
print(sentences)
    

def genQuestion(line):
    words = line.split()
    for i in range(len(words)):
        if words[i].istitle():
            question = "What did " + words[i-1] + " " + words[i] + "?"
            return question

for sentence in sentences:
    question = genQuestion(sentence)
    print(question)
    
    
