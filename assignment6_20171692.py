import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,QComboBox,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt
##

class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()
        self.dbfilename = 'test3_4.dat'
        self.scoredb = []
        self.readScoreDB()

        self.check = 0
        self.showScoreDB()


    def initUI(self):
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')



        NameLabel = QLabel("Name:")
        self.NameEdit = QLineEdit()

        AgeLabel = QLabel("Age:")
        self.AgeEdit = QLineEdit()

        ScoreLabel = QLabel("Score:")
        self.ScoreEdit = QLineEdit()

        AmountLabel = QLabel("Amount:")
        self.AmountEdit = QLineEdit()

        KeyLabel = QLabel("Key:")
        ResLabel = QLabel("Result:")
        #################################
        self.combo = QComboBox(self)
        self.combo.addItem("Name")
        self.combo.addItem("Age")
        self.combo.addItem("Score")
        #################################
        self.AddBtn = QPushButton("Add")
        self.DelBtn = QPushButton("Del")
        self.FindBtn = QPushButton("Find")
        self.IncBtn = QPushButton("inc")
        self.ShowBtn = QPushButton("show")
        #################################
        self.TextEdit = QTextEdit()
        #################################
        self.AddBtn.clicked.connect(self.Addbtn_Clicked)
        self.DelBtn.clicked.connect(self.Delbtn_Clicked)
        self.ShowBtn.clicked.connect(self.Showbtn_Clicked)
        self.FindBtn.clicked.connect(self.Findbtn_Clicked)
        self.IncBtn.clicked.connect(self.Incbtn_Clicked)
        ##################################
        w1layout = QHBoxLayout()
        w2layout = QHBoxLayout()
        w3layout = QHBoxLayout()
        w4layout = QHBoxLayout()
        w5layout = QHBoxLayout()
        layout = QVBoxLayout()
        #################################
        w1layout.addWidget(NameLabel)
        w1layout.addWidget(self.NameEdit)

        w1layout.addWidget(AgeLabel)
        w1layout.addWidget(self.AgeEdit)

        w1layout.addWidget(ScoreLabel)
        w1layout.addWidget(self.ScoreEdit)

        w2layout.addSpacing(200)
        w2layout.addWidget(AmountLabel)
        w2layout.addWidget(self.AmountEdit)

        w2layout.addWidget(KeyLabel)
        w2layout.addWidget(self.combo)

        w3layout.addWidget(self.AddBtn)
        w3layout.addWidget(self.DelBtn)
        w3layout.addWidget(self.FindBtn)
        w3layout.addWidget(self.IncBtn)
        w3layout.addWidget(self.ShowBtn)

        w4layout.addWidget(ResLabel)

        w5layout.addWidget(self.TextEdit)
        #####################################
        layout.addLayout(w1layout)
        layout.addLayout(w2layout)
        layout.addLayout(w3layout)
        layout.addLayout(w4layout)
        layout.addLayout(w5layout)
        ####################################
        ####################################
        self.setLayout(layout)


        self.show()


    def closeEvent(self, event):

        self.writeScoreDB()

    def Addbtn_Clicked(self):
        name_tmp = self.NameEdit.text()
        age_tmp = self.AgeEdit.text()
        score_tmp=self.ScoreEdit.text()
        record = {'Name':name_tmp,'Age':int(age_tmp),'Score':int(score_tmp)}
        print(str)
        self.scoredb.append(record)
        self.showScoreDB()

    def Delbtn_Clicked(self):
        name_tmp = self.NameEdit.text()
        for i in self.scoredb:
            if i['Name'] == name_tmp:
                while (True):
                        self.scoredb.remove(i)
                        if i not in self.scoredb:
                            break
        self.showScoreDB()

    def Showbtn_Clicked(self):
        self.showScoreDB()


    def Findbtn_Clicked(self):
        result = ""
        name_tmp=self.NameEdit.text()
        for p in self.scoredb:
            if p['Name'] == name_tmp:
                for attr in sorted(p):
                    result += attr + ":" + str(p[attr]) + "\t"
                result += "\n"
            self.TextEdit.setText(result)


    def Incbtn_Clicked(self):
        name_tmp=self.NameEdit.text()
        amount_tmp = int(self.AmountEdit.text())
        for p in self.scoredb:
            if p['Name'] == name_tmp:
                p['Score'] +=amount_tmp
        self.showScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

        #for p in self.scoredb:
        #    p['Age'] = int(p['Age'])
        #    p['Score'] = int(p['Score'])






    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)

        fH.close()

    def showScoreDB(self):
        keyname = self.combo.currentText()
        result = ""
        for p in sorted(self.scoredb, key =lambda person: person[keyname]):
            for attr in sorted(p):
                result += attr + ":" + str(p[attr]) + "\t"
            result += "\n"
        self.TextEdit.setText(result)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





