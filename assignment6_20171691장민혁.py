import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.change_int()
        self.doScoreDB()
        self.showScoreDB()
        
        
    def initUI(self):
        
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')

        label_name = QLabel("Name")
        label_age = QLabel("Age")
        label_score = QLabel("Score")
        label_amount = QLabel("Amount")
        label_key = QLabel("Key")
        label_result = QLabel("Result:")

        self.textEdit_result = QTextEdit()

        self.text_name = QLineEdit()
        self.text_age = QLineEdit()
        self.text_score = QLineEdit()
        self.text_amont = QLineEdit()
        self.text_result = QLineEdit()

        self.button_add = QPushButton("Add")
        self.button_del = QPushButton("Del")
        self.button_find = QPushButton("Find")
        self.button_inc = QPushButton("Inc")
        self.button_show = QPushButton("Show")

        self.combo = QComboBox(self)
        self.combo.addItem("Name")
        self.combo.addItem("Age")
        self.combo.addItem("Score")

        vertical_layout = QVBoxLayout()
        horizontal_layout1 = QHBoxLayout()
        horizontal_layout2 = QHBoxLayout()
        horizontal_layout3 = QHBoxLayout()
        horizontal_layout4 = QHBoxLayout()
        horizontal_layout5 = QHBoxLayout()

        horizontal_layout1.addWidget(label_name)
        horizontal_layout1.addWidget(self.text_name)

        horizontal_layout1.addWidget(label_age)
        horizontal_layout1.addWidget(self.text_age)

        horizontal_layout1.addWidget(label_score)
        horizontal_layout1.addWidget(self.text_score)

        horizontal_layout2.addSpacing(200)

        horizontal_layout2.addWidget(label_amount)
        horizontal_layout2.addWidget(self.text_amont)

        horizontal_layout2.addWidget(label_key)
        horizontal_layout2.addWidget(self.combo)

        horizontal_layout3.addSpacing(50)
        horizontal_layout3.addWidget(self.button_add)
        horizontal_layout3.addWidget(self.button_del)
        horizontal_layout3.addWidget(self.button_find)
        horizontal_layout3.addWidget(self.button_inc)
        horizontal_layout3.addWidget(self.button_show)

        horizontal_layout4.addWidget(label_result)

        horizontal_layout5.addWidget(self.textEdit_result)


        vertical_layout.addLayout(horizontal_layout1)
        vertical_layout.addLayout(horizontal_layout2)
        vertical_layout.addLayout(horizontal_layout3)
        vertical_layout.addLayout(horizontal_layout4)
        vertical_layout.addLayout(horizontal_layout5)
        self.setLayout(vertical_layout)
        self.show()


    def closeEvent(self, event):

        self.writeScoreDB()


    def readScoreDB(self):
        dbfilename = 'test3_4.dat'
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close( )


    def doScoreDB(self):
        self.button_add.clicked.connect(self.addScoreDB)
        self.button_del.clicked.connect(self.delScoreDB)
        self.button_find.clicked.connect(self.findScoreDB)
        self.button_inc.clicked.connect(self.incScoreDB)
        self.button_show.clicked.connect(self.showScoreDB)

    def change_int(self):  # age와 score를 int형으로 바꿔줌
        for i in self.scoredb:
            i['Age'] = int(i['Age'])
            i['Score'] = int(i['Score'])
        return self.scoredb


    def addScoreDB(self):
        name = self.text_name.text()
        age  = self.text_age.text()
        score = self.text_score.text()
        record = {'Name': name, 'Age': age, 'Score': score}
        self.scoredb.append(record)
        self.showScoreDB()


    def delScoreDB(self):
        rm_list = []
        for c, p in enumerate(self.scoredb):
            if p['Name'] == self.text_name.text():
                rm_list.append(c)
        for t in rm_list[::-1]:
            del self.scoredb[t]
        self.showScoreDB()


    def findScoreDB(self):
        ret_string = ""
        for p in self.scoredb:
            if p['Name'] == self.text_name.text():
                for attr in sorted(p):
                    ret_string += attr + ":" + str(p[attr]) + "\t"
                ret_string += "\n"
            self.textEdit_result.setText(ret_string)


    def incScoreDB(self):
        self.change_int()
        name = self.text_name.text()
        amount = self.text_amont.text()
        for p in self.scoredb:
            if p['Name'] == name:
                p['Score'] += int(amount)
        self.showScoreDB()


    def showScoreDB(self):
        self.key = self.combo.currentText()
        ret_string = ""
        for p in sorted(self.scoredb, key=lambda person: person[self.key]):
            for attr in sorted(p):
                ret_string += attr + ":" + str(p[attr]) + "\t"
            ret_string += "\n"
        self.textEdit_result.setText(ret_string)


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





