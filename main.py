from PySide2 import *
import sys
import pymongo
import pyautogui
from tab_ui import *

client = pymongo.MongoClient()
DB = client["SwitchOn"]
Collection = DB["Stock_Status"]
list_all = Collection.find()

maxWidth, maxHeight= pyautogui.size()

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.showAll(list_all)
        x = maxWidth // 250

    def showAll(self,list_all):
        col = maxWidth // 250
        rowNo = 0
        colNo = 0
        rowNo_1 = 0
        colNo_1 = 0
        rowNo_2 =0
        colNo_2 = 0
        for x in list_all:
            color = "rgb(0,255,0)"
            if x["Status"] == "Bad":
                color = 'rgb(255,0,0)'
            unit_id = x["Unit_id"]
            pic = "pics\\"+unit_id+".jpg"
            self.createNewCard_All(rowNo,colNo,color,unit_id,pic)
            colNo = colNo + 1
            if colNo % col == 0:
                colNo = 0
                rowNo = rowNo + 1
            if x["Status"] == "Bad":
                self.createNewCard_Bad(rowNo_1,colNo_1,unit_id,pic)
                colNo_1 = colNo_1 + 1
                if colNo_1 % col == 0:
                    colNo_1 = 0
                    rowNo_1 = rowNo_1 + 1
            if x["Status"] == "Good":
                self.createNewCard_Good(rowNo_2,colNo_2,unit_id,pic)
                colNo_2 = colNo_2 + 1
                if colNo_2 % col == 0:
                    rowNo_2 = rowNo_2 + 1
                    colNo_2 = 0     
        

    def createNewCard_All(self,rowNo,colNo,color,unit_id,pic):
        self.All_Card = QFrame(self.ui.scrollAreaWidgetContents_3)
        self.All_Card.setObjectName(u"All_Card")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.All_Card.sizePolicy().hasHeightForWidth())
        self.All_Card.setSizePolicy(sizePolicy1)
        self.All_Card.setMinimumSize(QSize(250, 400))
        self.All_Card.setMaximumSize(QSize(250, 400))
        self.All_Card.setStyleSheet(u"QFrame{\n"
            "background-color: rgb(156, 226, 255);\n"
            "border: 3px solid black;\n"
            "border-radius: 5px;\n"
            "}")
        self.All_Card.setFrameShape(QFrame.StyledPanel)
        self.All_Card.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.All_Card)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pic = QLabel(self.All_Card)
        self.pic.setObjectName(u"pic")
        sizePolicy1.setHeightForWidth(self.pic.sizePolicy().hasHeightForWidth())
        self.pic.setSizePolicy(sizePolicy1)
        self.pic.setMinimumSize(QSize(225, 275))
        self.pic.setMaximumSize(QSize(225, 275))
        self.pic.setPixmap(QPixmap(u"{0}".format(pic)))
        self.pic.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.pic, 0, Qt.AlignHCenter)

        self.color = QLabel(self.All_Card)
        self.color.setObjectName(u"color")
        sizePolicy1.setHeightForWidth(self.color.sizePolicy().hasHeightForWidth())
        self.color.setSizePolicy(sizePolicy1)
        self.color.setMinimumSize(QSize(225, 20))
        self.color.setMaximumSize(QSize(225, 20))
        self.color.setStyleSheet(u"QLabel{\n"+
        "	background-color: {0};\n".format(color)+
        "}")

        self.verticalLayout_2.addWidget(self.color, 0, Qt.AlignHCenter)

        self.ID = QLabel(self.All_Card)
        self.ID.setObjectName(u"ID")
        sizePolicy1.setHeightForWidth(self.ID.sizePolicy().hasHeightForWidth())
        self.ID.setSizePolicy(sizePolicy1)
        self.ID.setMinimumSize(QSize(225, 50))
        self.ID.setMaximumSize(QSize(225, 50))

        self.verticalLayout_2.addWidget(self.ID, 0, Qt.AlignHCenter)
        self.pic.setText("")
        self.color.setText("")
        self.ID.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Unit ID : {0}</span></p></body></html>".format(unit_id), None))
        # self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.All), QCoreApplication.translate("MainWindow", u"All", None))

        self.ui.gridLayout_6.addWidget(self.All_Card, rowNo, colNo, 1, 1) 
        
    def createNewCard_Bad(self,rowNo,colNo,unit_id,pic):
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        self.Bad_Card = QFrame(self.ui.scrollAreaWidgetContents_2)
        self.Bad_Card.setObjectName(u"Bad_Card")
        sizePolicy1.setHeightForWidth(self.Bad_Card.sizePolicy().hasHeightForWidth())
        self.Bad_Card.setSizePolicy(sizePolicy1)
        self.Bad_Card.setMinimumSize(QSize(250, 400))
        self.Bad_Card.setMaximumSize(QSize(250, 400))
        self.Bad_Card.setStyleSheet(u"QFrame{\n"
            "background-color: rgb(156, 226, 255);\n"
            "border: 3px solid black;\n"
            "border-radius: 5px;\n"
            "}")
        self.Bad_Card.setFrameShape(QFrame.StyledPanel)
        self.Bad_Card.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Bad_Card)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pic_2 = QLabel(self.Bad_Card)
        self.pic_2.setObjectName(u"pic_2")
        sizePolicy1.setHeightForWidth(self.pic_2.sizePolicy().hasHeightForWidth())
        self.pic_2.setSizePolicy(sizePolicy1)
        self.pic_2.setMinimumSize(QSize(225, 275))
        self.pic_2.setMaximumSize(QSize(225, 275))
        self.pic_2.setPixmap(QPixmap(u"{0}".format(pic)))
        self.pic_2.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.pic_2, 0, Qt.AlignHCenter)

        self.color_2 = QLabel(self.Bad_Card)
        self.color_2.setObjectName(u"color_2")
        sizePolicy1.setHeightForWidth(self.color_2.sizePolicy().hasHeightForWidth())
        self.color_2.setSizePolicy(sizePolicy1)
        self.color_2.setMinimumSize(QSize(225, 20))
        self.color_2.setMaximumSize(QSize(225, 20))
        self.color_2.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.verticalLayout_3.addWidget(self.color_2, 0, Qt.AlignHCenter)

        self.ID_2 = QLabel(self.Bad_Card)
        self.ID_2.setObjectName(u"ID_2")
        sizePolicy1.setHeightForWidth(self.ID_2.sizePolicy().hasHeightForWidth())
        self.ID_2.setSizePolicy(sizePolicy1)
        self.ID_2.setMinimumSize(QSize(225, 50))
        self.ID_2.setMaximumSize(QSize(225, 50))

        self.verticalLayout_3.addWidget(self.ID_2, 0, Qt.AlignHCenter)
        self.pic_2.setText("")
        self.color_2.setText("")
        self.ID_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Unit ID: {0}</span></p></body></html>".format(unit_id), None))

        self.ui.gridLayout_5.addWidget(self.Bad_Card, rowNo, colNo, 1, 1)



    def createNewCard_Good(self,rowNo,colNo,unit_id,pic):
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        self.Good_Card = QFrame(self.ui.scrollAreaWidgetContents)
        self.Good_Card.setObjectName(u"Good_Card")
        sizePolicy1.setHeightForWidth(self.Good_Card.sizePolicy().hasHeightForWidth())
        self.Good_Card.setSizePolicy(sizePolicy1)
        self.Good_Card.setMinimumSize(QSize(250, 400))
        self.Good_Card.setMaximumSize(QSize(250, 400))
        self.Good_Card.setStyleSheet(u"QFrame{\n"
            "	background-color: rgb(156, 226, 255);\n"
            "border: 3px solid blacl;\n"
            "border-radius: 5px;\n"
            "}")
        self.Good_Card.setFrameShape(QFrame.StyledPanel)
        self.Good_Card.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Good_Card)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pics = QLabel(self.Good_Card)
        self.pics.setObjectName(u"pics")
        sizePolicy1.setHeightForWidth(self.pics.sizePolicy().hasHeightForWidth())
        self.pics.setSizePolicy(sizePolicy1)
        self.pics.setMinimumSize(QSize(225, 275))
        self.pics.setMaximumSize(QSize(225, 275))
        self.pics.setPixmap(QPixmap(u"{0}".format(pic)))
        self.pics.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.pics, 0, Qt.AlignHCenter)

        self.color_3 = QLabel(self.Good_Card)
        self.color_3.setObjectName(u"color_3")
        sizePolicy1.setHeightForWidth(self.color_3.sizePolicy().hasHeightForWidth())
        self.color_3.setSizePolicy(sizePolicy1)
        self.color_3.setMinimumSize(QSize(225, 20))
        self.color_3.setMaximumSize(QSize(225, 20))
        self.color_3.setStyleSheet(u"background-color: rgb(0, 255, 0);")

        self.verticalLayout_4.addWidget(self.color_3, 0, Qt.AlignHCenter)

        self.ID_3 = QLabel(self.Good_Card)
        self.ID_3.setObjectName(u"ID_3")
        sizePolicy1.setHeightForWidth(self.ID_3.sizePolicy().hasHeightForWidth())
        self.ID_3.setSizePolicy(sizePolicy1)
        self.ID_3.setMinimumSize(QSize(225, 50))
        self.ID_3.setMaximumSize(QSize(225, 50))

        self.verticalLayout_4.addWidget(self.ID_3, 0, Qt.AlignHCenter)
        self.pics.setText("")
        self.color_3.setText("")
        self.ID_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Unit ID : {0}</span></p></body></html>".format(unit_id), None))

        self.ui.gridLayout_4.addWidget(self.Good_Card, rowNo, colNo, 1, 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())