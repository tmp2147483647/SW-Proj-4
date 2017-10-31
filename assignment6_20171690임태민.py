import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit, QGridLayout)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
        
        
    def initUI(self):
        nlabel = QLabel('Name:')
        nameedit = QLineEdit()
        
        agelabel = QLabel('Age:')
        ageedit = QLineEdit()
        
        slabel = QLabel('Score:')
        scoreedit = QLineEdit()
        
        alabel = QLabel('Amount:')
        amountedit = QLineEdit()
        
        klabel = QLabel('Key:')
        self.keycombo = QComboBox()
        self.keycombo.addItem('Name')
        self.keycombo.addItem('Age')
        self.keycombo.addItem('Score')

        rslabel = QLabel('result :')
        self.rstextedit = QTextEdit()

        addbtn = QPushButton('Add')
        delbtn = QPushButton('Del')
        findbtn = QPushButton('Find')
        incbtn = QPushButton('Inc')
        showbtn = QPushButton('Show')

        grid = QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(nlabel, 1, 0)
        grid.addWidget(nameedit, 1, 1)
        grid.addWidget(agelabel, 1, 2)
        grid.addWidget(ageedit, 1, 3)
        grid.addWidget(slabel, 1, 4)
        grid.addWidget(scoreedit, 1, 5)

        grid.addWidget(alabel, 2, 2)
        grid.addWidget(amountedit, 2, 3)
        grid.addWidget(klabel, 2, 4)
        grid.addWidget(self.keycombo, 2, 5)

        grid.addWidget(addbtn, 3, 1)
        grid.addWidget(delbtn, 3, 2)
        grid.addWidget(findbtn, 3, 3)
        grid.addWidget(incbtn, 3, 4)
        grid.addWidget(showbtn, 3, 5)

        grid.addWidget(rslabel, 5, 0)
        grid.addWidget(self.rstextedit, 6, 0, 5, 6)
        
        self.setLayout(grid)
        
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')    
        self.show()


    def closeEvent(self, event):

        self.writeScoreDB()

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


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        self.key = self.keycombo.currentText()
        rtstring = ""
        for i in sorted(self.scoredb, key=lambda person: person[self.key]):
            for j in sorted(i):
                rtstring += j + ":" + str(i[j]) + "\t"
            rtstring += "\n"
        self.rstextedit.setText(rtstring)
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
