import re
import string
import nltk
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def readTxt(fileName):
    textFile = open(fileName, "r")
    lines = textFile.readlines()
    lines2 = []
    for i in lines:
        i = i.replace('\n', '')
        lines2.append(i)
    return lines2

# Kalimat
# Saya Sedang memakan apel seharga 25000 dan Saya sedang MeMASak mie ???? instan


# Input Dokumen
stringText = input("Input text : ")

# Case Folding
lower_document = stringText.lower()
print("Lowcase Document : ", lower_document)

dltNumber = re.sub(r"\d+", "", lower_document)
print("Document with no number : ", dltNumber)

noPunctuation = dltNumber.translate(str.maketrans("","",string.punctuation))
print("Document with no punctuation : ", noPunctuation)

noWhitespace = noPunctuation.strip();
print("Dokumen with no whitespace: ", noWhitespace)

#Tokenizing
tokens = nltk.tokenize.word_tokenize(noWhitespace)
kemunculan = nltk.FreqDist(tokens)
print("Tokenizing NLTK")
print(kemunculan.most_common())

#Filtering / Stop Removal
stopRemoval = readTxt('StopWord.txt')
withoutStopword = [x for x in kemunculan if x not in stopRemoval]
print("Filtering Document : ",withoutStopword)

factory = StemmerFactory()
stemmer = factory.create_stemmer()

withoutStopword = ' '.join(withoutStopword)

hasil = stemmer.stem(withoutStopword)
print("Result: ", hasil)

