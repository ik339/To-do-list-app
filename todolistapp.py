from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
                               QListWidgetItem, QPushButton, QSizePolicy, QWidget, QMessageBox)

import sys

class Ui_todo(object):
    def setupUi(self, todo):
        if not todo.objectName():
            todo.setObjectName(u"todo")
        todo.resize(400, 400)
        todo.setMaximumSize(QSize(400, 400))
        font = QFont()
        font.setFamilies([u"Segoe Script"])
        font.setPointSize(10)
        todo.setFont(font)
        self.listWidget = QListWidget(todo)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(30, 100, 281, 211))

        self.addbutton = QPushButton(todo)
        self.addbutton.setObjectName(u"addbutton")
        self.addbutton.setGeometry(QRect(330, 60, 41, 31))
        #add
        self.addbutton.clicked.connect(self.addtolist)

        self.taskinput = QLineEdit(todo)
        self.taskinput.setObjectName(u"taskinput")
        self.taskinput.setGeometry(QRect(130, 70, 151, 21))

        self.newtasklabel = QLabel(todo)
        self.newtasklabel.setObjectName(u"newtasklabel")
        self.newtasklabel.setGeometry(QRect(30, 70, 91, 21))
        font1 = QFont()
        font1.setFamilies([u"Segoe Print"])
        font1.setPointSize(12)
        self.newtasklabel.setFont(font1)

        self.todolabel = QLabel(todo)
        self.todolabel.setObjectName(u"todolabel")
        self.todolabel.setGeometry(QRect(120, 10, 171, 41))
        font2 = QFont()
        font2.setFamilies([u"Segoe Print"])
        font2.setPointSize(20)
        self.todolabel.setFont(font2)

        self.deletebutton = QPushButton(todo)
        self.deletebutton.setObjectName(u"deletebutton")
        self.deletebutton.setGeometry(QRect(330, 190, 41, 31))
        #delete
        self.deletebutton.clicked.connect(self.performdelete)

        self.emailinput = QLineEdit(todo)
        self.emailinput.setObjectName(u"emailinput")
        self.emailinput.setGeometry(QRect(30, 350, 211, 21))

        self.emailbutton = QPushButton(todo)
        self.emailbutton.setObjectName(u"emailbutton")
        self.emailbutton.setGeometry(QRect(250, 340, 101, 31))
        #email
        self.emailbutton.clicked.connect(self.sendemail)

        self.retranslateUi(todo)

        QMetaObject.connectSlotsByName(todo)
    # setupUi

    def retranslateUi(self, todo):
        todo.setWindowTitle(QCoreApplication.translate("todo", u"Form", None))
        self.addbutton.setText(QCoreApplication.translate("todo", u"+", None))
        self.newtasklabel.setText(QCoreApplication.translate("todo", u"New Task: ", None))
        self.todolabel.setText(QCoreApplication.translate("todo", u"To Do List", None))
        self.deletebutton.setText(QCoreApplication.translate("todo", u"-", None))
        self.emailbutton.setText(QCoreApplication.translate("todo", u"Email Tasks", None))
    # retranslateUi

    def sendemail(self):
        i2 = self.emailinput.text()

        print("email sent") #how to make it send to email?

    def addtolist(self):
        i1 = self.taskinput.text()
        i1 = i1.strip()#make sure cant add blank spaces - using if. - strip()function
        if len(i1)>0: #check length
            self.listWidget.addItem(str(i1))
        else:
            QMessageBox.warning(None, "Warning", "Error. No blank spaces allowed") #qmessage box.warnign.

#extract the text first before writiing to file. after writing to file we need to send as email.
        #file = open("todolistapp.txt", "w") as file:
        #file.write("todolistapp")
            #for i in i1:
                #file.writeline(item)
            #file.close()

    def performdelete(self):
        selected_items = self.listWidget.selectedItems()
        if not selected_items: return
        for item in selected_items:
            self.listWidget.takeItem(self.listWidget.row(item))

app = QApplication([]) # makes the program run
widget = QWidget()
form = Ui_todo()
form.setupUi(widget)
widget.show()
sys.exit(app.exec())

# save to a file when add to list!?
# items count index for?
# n=i
# gmail pip install package.
# olympus @ac.uk = developer society code guide.
# udemy - extra courses