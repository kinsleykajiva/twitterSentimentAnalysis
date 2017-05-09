import sys
from PyQt4.Qt import *
 
lista = ['aa', 'ab', 'ac']
listb = ['ba', 'bb', 'bc']
listc = ['ca', 'cb', 'cc']
mystruct = {'A':lista, 'B':listb, 'C':listc}
 
class MyTable(QTableWidget):
    def __init__(self, thestruct, *args):
        QTableWidget.__init__(self, *args)
        self.data = thestruct
        self.setmydata()
 
    def setmydata(self):
        n = 0
        for key in self.data:
            m = 0
            for item in self.data[key]:
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
                m += 1
            n += 1
 
def main(args):
    app = QApplication(args)
    table = MyTable(mystruct, 5, 3)
    table.show()
    sys.exit(app.exec_())

def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]
def testFuncNew(text):
    from nltk.corpus import stopwords 
    cachedStopWords = stopwords.words("english") 
    
    return ' '.join([word for word in text.split() if word not in cachedStopWords])
 
if __name__=="__main__":
   # main(sys.argv)
   import re
    
   import operator
   my_string = "Wow! Is this true? Really!?!? This is crazy!"
   
   my_string=testFuncNew(my_string)#''.join(str(e) for e in removeStopwords(my_string,['is','this','Wow']))
   print(my_string)
   words = re.findall(r'\w+', my_string) #This finds words in the document
   from collections import Counter
   cap_words = [word.upper() for word in words] #capitalizes all the words
   word_counts = Counter(cap_words) #counts the number each time a word appears
   stats = {'a':1000, 'b':3000, 'c': 100, 'd':3000}
   #print (max(word_counts, key=lambda key: word_counts[key]))