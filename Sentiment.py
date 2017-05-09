# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sentiment.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import Utils as utils
from netconx import Netconx
from sqDb import DB
import PanGraphing as pan

POSITIVITY = """
QProgressBar{
    border: 2px solid green;
    border-radius: 5px;
    text-align: center
}

QProgressBar::chunk {
    background-color: lightblue;
    width: 10px;
    margin: 1px;
}
"""

NEGATIVITY = """
QProgressBar{
    border: 2px solid grey;
    border-radius: 5px;
    text-align: center
}

QProgressBar::chunk {
    background-color: red;
    width: 10px;
    margin: 1px;
}
"""

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1100, 484)
        palette = QtGui.QPalette()
        app_icon = QtGui.QIcon()
        app_icon.addFile('twitter.png', QtCore.QSize(32,32))
        app.setWindowIcon(app_icon)
        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(QtGui.QPixmap("3.jpg")))
        MainWindow.setPalette(palette)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 171, 331))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.openSavedFiles = QtGui.QPushButton(self.verticalLayoutWidget)
        self.openSavedFiles.setObjectName(_fromUtf8("openSavedFiles"))
        self.verticalLayout.addWidget(self.openSavedFiles)
        self.saveToFile = QtGui.QPushButton(self.verticalLayoutWidget)
        self.saveToFile.setObjectName(_fromUtf8("saveToFile"))
        self.verticalLayout.addWidget(self.saveToFile)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 10, 321, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.queryText = QtGui.QLineEdit(self.centralwidget)
        self.queryText.setGeometry(QtCore.QRect(190, 60, 261, 21))
        self.queryText.setObjectName(_fromUtf8("queryText"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 40, 171, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.testQuerySentiment = QtGui.QPushButton(self.centralwidget)
        self.testQuerySentiment.setGeometry(QtCore.QRect(460, 60, 75, 23))
        self.testQuerySentiment.setObjectName(_fromUtf8("testQuerySentiment"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 160, 171, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 220, 161, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.negativeProgressbar = QtGui.QProgressBar(self.centralwidget)
        self.negativeProgressbar.setGeometry(QtCore.QRect(190, 180, 261, 23))
        self.negativeProgressbar.setProperty("value", 0)
        self.negativeProgressbar.setObjectName(_fromUtf8("negativeProgressbar"))
        self.positivityProgressbar = QtGui.QProgressBar(self.centralwidget)
        self.positivityProgressbar.setGeometry(QtCore.QRect(190, 250, 261, 23))
        self.positivityProgressbar.setProperty("value", 0)
        self.positivityProgressbar.setObjectName(_fromUtf8("positivityProgressbar"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 310, 111, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.Processstatus = QtGui.QLabel(self.centralwidget)
        self.Processstatus.setGeometry(QtCore.QRect(230, 100, 201, 41))
        self.Processstatus.setObjectName(_fromUtf8("Processstatus"))
        self.tableViewlist = QtGui.QTableWidget(self.centralwidget)
        self.tableViewlist.setGeometry(QtCore.QRect(470, 100, 610, 321))
        self.tableViewlist.setObjectName(_fromUtf8("tableViewlist"))
        self.savedTopics = QtGui.QComboBox(self.centralwidget)
        self.savedTopics.setGeometry(QtCore.QRect(190, 140, 169, 20))
        self.savedTopics.setObjectName(_fromUtf8("savedTopics"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 140, 71, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.generalReview = QtGui.QLabel(self.centralwidget)
        self.generalReview.setGeometry(QtCore.QRect(550, 80, 131, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.generalReview.setFont(font)
        self.generalReview.setObjectName(_fromUtf8("generalReview"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.customeFunctions()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", utils.WINDOW_TITLE, None))
        self.openSavedFiles.setText(_translate("MainWindow", "Open Saved Streams", None))
        self.saveToFile.setText(_translate("MainWindow", "Save Stream", None))
        self.label.setText(_translate("MainWindow", "Political Sentiment Analysis System on Tweeter Nueron Project", None))
        self.label_2.setText(_translate("MainWindow", "Test Sentiment on Which topic:", None))
        self.testQuerySentiment.setText(_translate("MainWindow", "Test", None))
        self.label_3.setText(_translate("MainWindow", "Negativity ", None))
        self.label_4.setText(_translate("MainWindow", "Positivity", None))
        self.pushButton.setText(_translate("MainWindow", "Show on Graph", None))
        self.Processstatus.setText(_translate("MainWindow", "....", None))
        self.label_5.setText(_translate("MainWindow", "Saved Topics", None))
        self.generalReview.setText(_translate("MainWindow", "General View", None))


    def customeFunctions(self):

        self.queryText.setPlaceholderText("Put Query or test Topic To Test Sentiment on")
        self.saveToFile.clicked.connect(self.testingButtonClicks)
        self.testQuerySentiment.clicked.connect(self.Click_testsentiments)
        self.pushButton.clicked.connect(self.showCurrentSentimentsOnGraph)
        self.NetConn=Netconx()
        self.load_comboBox()
        self.negativeProgressbar.setEnabled(False)
        self.positivityProgressbar.setEnabled(False)
        """self.setPositivityVale(67)
        self.setNegativityVale(97)"""
        #self.savedTopics.setEnabled(False)
        

    def Click_testsentiments(self):
        
        utils.topic=self.queryText.text().strip()
        if len(utils.topic )<1:            
            msgBox=QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Information)
            msgBox.setText('Please put a topic to test on ')
            msgBox.setWindowTitle("Empty Input Error")
            msgBox.addButton(QtGui.QPushButton('Ok'), QtGui.QMessageBox.YesRole)
            ret = msgBox.exec_()
        else:
            if self.NetConn.checkNet_Exists() is True:
                self.Processstatus.setText("Testing  ......")              
                self.Processstatus.setStyleSheet('color: red')         
        
                utils.processLinner()  

                self.Processstatus.setText("Testing  ....Processing")              
                self.Processstatus.setStyleSheet('color: red') 

                fromtweeter=utils.getQueryTweets(utils.topic)

                tweeet_msgs,   polarity,  subjectivity   =utils.analiseTweetSentment(fromtweeter)     
                

                self.loadData_Table(    tweeet_msgs,   polarity  )

            else:
                msgBox=QtGui.QMessageBox()
                msgBox.setIcon(QtGui.QMessageBox.Information)
                msgBox.setText('Connection Failed .Try Again Later')
                msgBox.setWindowTitle("No Internet !!")
                msgBox.addButton(QtGui.QPushButton('Ok'), QtGui.QMessageBox.YesRole)
                msgBox.addButton(QtGui.QPushButton('Load Saved Analysis'), QtGui.QMessageBox.YesRole)
                ret = msgBox.exec_()
                print(ret)
                
                



    def testingButtonClicks(self):
       
        print(self.queryText.text())
        
        print("asd")

    def setPositivityVale(self,val):
        self.positivityProgressbar.setProperty("value", val)
        self.positivityProgressbar.setStyleSheet(POSITIVITY)

    def setNegativityVale(self,val):
        self.negativeProgressbar.setProperty("value", val)
        self.negativeProgressbar.setStyleSheet(NEGATIVITY)

    def load_comboBox(self):
        
        self.savedTopics.addItem("Select A Topic")
        db=DB()
        data=db.getSavedTopics()
        d_=[]
        for v in data:
            d_.append(v[0])

        data_=utils.removeDuplicates(d_)

        for row in data_:            
            self.savedTopics.addItem(row)
            

        db.closeClassConnection()
            
        
        self.savedTopics.activated[str].connect(self.selectedsavedTopic)

    def selectedsavedTopic(self,text):
        #self.label_5.setText(text)
        if text != "Select A Topic":            
            db=DB()
            tweeet_msgs=[]
            polarity=[]
            utils.topic=text
            self.queryText.setText(utils.topic)
            data=db.getSavedQuery(   text   )       
            for row in data:
                tweeet_msgs.append(row[1])
                polarity.append(row[2])

            self.loadData_Table(    tweeet_msgs,   polarity  )
        else:
            self.criticalErrorMessageBox("Select Another Option Other Than This")
            self.loadData_Table(    [],   []  )

    def showCurrentSentimentsOnGraph(self):
        self.tweet_global
        self.polarity_global
        x=[]
        y=[]
        x_=0
        y_=0
        for i in self.polarity_global:
            x_+=1       
            if i < 0:
                y_+=1
            elif i>0:
                y_-=1

            x.append(x_)
            y.append(y_)
        pan.graph_data_1(x,y)



    def criticalErrorMessageBox(self,messageTxt):
        MESSAGE = QtCore.QT_TR_NOOP("<p>"+messageTxt+"</p>"                           )
        reply = QtGui.QMessageBox.critical(self, self.tr("tGui.QMessageBox.showCritical()"),
                                               MESSAGE, QtGui.QMessageBox.Abort)

    #@QtCore.pyqtSlot() # prevents executing following function twice
    def cell_was_clicked(self,row,column):
        row=row+0
        #print("Row %d and Column %d was clicked" % (row, column))
        if column != 1:
            item = self.tableViewlist.item(row, column)
            content_data = item.text() 
            content_data=content_data.split(' ', 1) # >> ['0.85', '-- Positive']
            #print(content_data[0])
            content_data=float(content_data[0]) * 100
            pos_=content_data
            nage_=content_data-10
            #print("positivity :",pos_)
            #print("negativity: ",nage_)
            self.setPositivityVale(pos_)
            self.setNegativityVale(nage_)
      
        

        



    def loadData_Table(self,tweet,polarity__):
        self.load_comboBox()
        self.Processstatus.setText("Done Check Table for results!!!")              
        self.Processstatus.setStyleSheet('color: green')
        self.tweet_global=tweet
        self.polarity_global=polarity__    
        determiner=[]
        general_pos=0
        general_neg=0
        general_net=0
        for i in polarity__:
            if float(i) == 0 or float(i) == 0.0 :
                determiner.append("Neutral")
                general_net+=1
            elif float(i) < 0 :
                determiner.append("Negative")
                general_neg+=1
            else:
                determiner.append("Positive")            
                general_pos+=1
        

        polarity__= ['{:.2f}'.format(float(x)) for x in polarity__] # direct conversion from a floast list to a string list as QTable was not rendering
        polarity__x=[]
        for x in range(len(determiner)):
            polarity__x.append(polarity__[x]+" -- "+determiner[x])

        data_forTable={'Tweet':tweet,'Sentment polarity':polarity__x}
             
              
        self.tableViewlist.setRowCount(len(tweet))
        self.tableViewlist.setColumnCount(2)

        #print(general_pos,general_neg,general_net)
        General_View="General View:"+" Neutral"

        if general_pos>general_neg and general_pos>general_net:
            
            General_View="General View: "+"Positive"
            self.generalReview.setStyleSheet('color: green')         
        elif general_neg>general_pos and general_neg>general_net:
            
            General_View="General View: "+"Negative"
            self.generalReview.setStyleSheet('color: red')     
        elif general_net>general_pos and general_net>general_neg:
            
            General_View="General View:"+" Neutral"   
            self.generalReview.setStyleSheet('color: black')     
        
        #print(General_View)
        self.generalReview.setText(General_View)
        
        self.tableViewlist.cellClicked.connect(self.cell_was_clicked)            
          
        
        
        

        # putting the dataonto our table
        headers=[]
        for n,key in enumerate(sorted(data_forTable.keys())):
            headers.append(key)
            for m,item in enumerate(data_forTable[key]):
                newitem=QtGui.QTableWidgetItem(item)
                self.tableViewlist.setItem(m,n,newitem)

        # adding headers
        self.tableViewlist.setHorizontalHeaderLabels(headers)
        #Adjust size of Table
        self.tableViewlist.resizeColumnsToContents()
        self.tableViewlist.resizeRowsToContents()

        



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

