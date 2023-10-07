# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_evaluate(object):
    def __init__(self):
        self.playerList=[]
        self.selectMatchList=[]
        self.selectTeamList=[]
        self.allpoints=[]
        self.playerAndTeam=[]
        self.bow=0
        self.economyRate=0
        self.score=0

    # Displaying the players in a Team
    def showTeam_Match(self):
        self.match.addItem("Match")
        self.team_name.addItem("Team")
        cricket=sqlite3.connect('fantasycricket.db')
        objcricket=cricket.cursor()
        objcricket.execute('Select Name from Teams')
        for i in objcricket.fetchall():
            if i[0] not in self.selectTeamList:
                self.team_name.addItem(i[0])
                self.selectTeamList.append(i[0])

        objcricket.execute('Select Match from Matches')
        for i in objcricket.fetchall():
            if i[0] not in self.selectMatchList:
                self.match.addItem(i[0])
                self.selectMatchList.append(i[0])

    # calculating the Scores of the Team
    def calculateScore(self):
        self.players_list.clear()
        self.points_list.clear()
        self.playerList=[]
        self.allpoints=[]
        self.playerAndTeam=[]
        self.score=0
        self.points_lbl.setText(str(self.score))
        cricket=sqlite3.connect('fantasycricket.db')
        objcricket=cricket.cursor()
        objcricket.execute('Select Player,Name from Teams') 
        for i in objcricket.fetchall():
            self.playerAndTeam.append(i)
        objcricket.execute('select Player,Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wkts,Catches,Stumping,RO,Match from Matches')
        self.players_list.clear()
        self.points_list.clear()
        
        if "Match"==self.match.currentText() and "Team" == self.team_name.currentText():
            self.messagebox('INFO','Please Select Team and Match')
        elif "Team" == self.team_name.currentText() and "Match"!=self.match.currentText(): 
            self.messagebox('INFO','Please Select Team')
        elif "Match"==self.match.currentText() and "Team"!=self.team_name.currentText():
            self.messagebox('INFO','Please Select Match')
        else:
            for i in objcricket.fetchall():
                for k in self.playerAndTeam:
                    self.points=0
                    self.economyRate=0
                    self.bow=0
                    if k[1] == self.team_name.currentText() and i[12]==self.match.currentText():
                        if i[0] == k[0]:
                            self.players_list.addItem(i[0])
                            if i[1]%2==0:
                                self.points+=(i[1]/2)
                                if i[1]>=50:
                                    self.points+=5
                                    if i[1]>=100:
                                        self.points+=10
                            else:
                                self.points+=(i[1]-1)/2
                                if i[1]>=50:
                                    self.points+=5
                                    if i[1]>=100:
                                        self.points+=10
                            if i[2] >80:
                                self.points+=2
                                if i[2]>100:
                                    self.points+=4
                            self.points+=i[3]
                            self.points+=i[4]*2
                            if i[5]>0:
                                self.bow=i[5]/6
                                self.economyRate=i[7]/self.bow
                                if self.economyRate>3.5 and self.economyRate<=4.5:
                                    self.points+=4
                                elif self.economyRate>2 and self.economyRate<3.5:
                                    self.points+=7
                                elif self.economyRate<2:
                                    self.points+=10
                            self.points+=i[8]*10
                            if i[8]>=3:
                                self.points+=5
                            if i[8]>=5:
                                self.points+=10
                            self.points+=i[9]*10
                            self.points+=i[10]*10
                            self.points+=i[11]*10
                            self.points_list.addItem(str(self.points))
                            self.allpoints.append(self.points)
            for i in self.allpoints:
                self.score+=i
            self.points_lbl.setText(str(self.score))

        # message box
    def messagebox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setWeight(12)
        mess.setFont(font)
        mess.exec_()

    def setupUi(self, evaluate):
        evaluate.setObjectName("evaluate")
        evaluate.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(evaluate)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(27, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 9, 1, 1)
        self.line = QtWidgets.QFrame(evaluate)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 2, 10)
        self.label_3 = QtWidgets.QLabel(evaluate)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 6, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(141, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 6, 7, 1, 3)
        self.label_2 = QtWidgets.QLabel(evaluate)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(141, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 6, 0, 1, 4)
        self.match = QtWidgets.QComboBox(evaluate)
        self.match.setObjectName("match")
        self.gridLayout.addWidget(self.match, 1, 8, 1, 1)
        self.calculate_btn = QtWidgets.QPushButton(evaluate)
        self.calculate_btn.setObjectName("calculate_btn")
        self.gridLayout.addWidget(self.calculate_btn, 6, 4, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 3, 1, 5)
        spacerItem4 = QtWidgets.QSpacerItem(26, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        self.points_list = QtWidgets.QListWidget(evaluate)
        self.points_list.setObjectName("points_list")
        self.gridLayout.addWidget(self.points_list, 5, 6, 1, 4)
        self.line_2 = QtWidgets.QFrame(evaluate)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 3, 5, 3, 1)
        self.team_name = QtWidgets.QComboBox(evaluate)
        self.team_name.setObjectName("team_name")
        self.gridLayout.addWidget(self.team_name, 1, 1, 1, 2)
        self.players_list = QtWidgets.QListWidget(evaluate)
        self.players_list.setObjectName("players_list")
        self.gridLayout.addWidget(self.players_list, 5, 0, 1, 5)
        self.points_lbl = QtWidgets.QLabel(evaluate)
        self.points_lbl.setText("")
        self.points_lbl.setObjectName("points_lbl")
        self.gridLayout.addWidget(self.points_lbl, 4, 7, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 9, 1, 1)
        self.label = QtWidgets.QLabel(evaluate)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 8)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 0, 1, 1)
        
        self.showTeam_Match()
        self.calculate_btn.clicked.connect(self.calculateScore)

        self.retranslateUi(evaluate)
        QtCore.QMetaObject.connectSlotsByName(evaluate)

    def retranslateUi(self, evaluate):
        _translate = QtCore.QCoreApplication.translate
        evaluate.setWindowTitle(_translate("evaluate", "Evaluate"))
        self.label_3.setText(_translate("evaluate", "Points"))
        self.label_2.setText(_translate("evaluate", "Players"))
        self.calculate_btn.setText(_translate("evaluate", " Calculate Score"))
        self.label.setText(_translate("evaluate", "Evaluate the performance for your fantasy team"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    evaluate = QtWidgets.QWidget()
    ui = Ui_evaluate()
    ui.setupUi(evaluate)
    evaluate.show()
    sys.exit(app.exec_())
