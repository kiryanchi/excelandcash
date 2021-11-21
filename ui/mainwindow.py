# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(QSize(800, 800))
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        self.action_save = QAction(MainWindow)
        self.action_save.setObjectName(u"action_save")
        self.action_saveas = QAction(MainWindow)
        self.action_saveas.setObjectName(u"action_saveas")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_file = QLabel(self.centralwidget)
        self.label_file.setObjectName(u"label_file")
        self.label_file.setMaximumSize(QSize(16777215, 30))

        self.gridLayout.addWidget(self.label_file, 0, 1, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)

        self.groupBox_detail = QGroupBox(self.centralwidget)
        self.groupBox_detail.setObjectName(u"groupBox_detail")
        self.groupBox_detail.setMaximumSize(QSize(16777215, 200))
        self.groupBox_detail.setCheckable(False)
        self.gridLayout_2 = QGridLayout(self.groupBox_detail)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.groupBox_detail)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.lineEdit_company = QLineEdit(self.groupBox_detail)
        self.lineEdit_company.setObjectName(u"lineEdit_company")

        self.gridLayout_2.addWidget(self.lineEdit_company, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_detail)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit_interval = QLineEdit(self.groupBox_detail)
        self.lineEdit_interval.setObjectName(u"lineEdit_interval")

        self.gridLayout_2.addWidget(self.lineEdit_interval, 2, 1, 1, 1)

        self.lineEdit_process = QLineEdit(self.groupBox_detail)
        self.lineEdit_process.setObjectName(u"lineEdit_process")

        self.gridLayout_2.addWidget(self.lineEdit_process, 2, 3, 1, 1)

        self.lineEdit_project = QLineEdit(self.groupBox_detail)
        self.lineEdit_project.setObjectName(u"lineEdit_project")

        self.gridLayout_2.addWidget(self.lineEdit_project, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_detail)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.lineEdit_name = QLineEdit(self.groupBox_detail)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.gridLayout_2.addWidget(self.lineEdit_name, 1, 3, 1, 1)

        self.lineEdit_date = QLineEdit(self.groupBox_detail)
        self.lineEdit_date.setObjectName(u"lineEdit_date")

        self.gridLayout_2.addWidget(self.lineEdit_date, 0, 3, 1, 1)

        self.label_5 = QLabel(self.groupBox_detail)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)

        self.label_6 = QLabel(self.groupBox_detail)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox_detail)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 2, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_detail, 2, 0, 1, 2)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setAcceptDrops(True)
        self.tableWidget.setLineWidth(7)
        self.tableWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(220)

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_open)
        self.menu.addAction(self.action_save)
        self.menu.addAction(self.action_saveas)
        self.menu.addSeparator()
        self.menu.addAction(self.action_exit)

        self.retranslateUi(MainWindow)
        self.action_exit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Excel Photo Manager", None))
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"\uc5f4\uae30", None))
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5", None))
#if QT_CONFIG(shortcut)
        self.action_save.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.action_saveas.setText(QCoreApplication.translate("MainWindow", u"\ub2e4\ub978 \uc774\ub984\uc73c\ub85c \uc800\uc7a5", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"\uc885\ub8cc", None))
        self.label_file.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac \ud30c\uc77c \uc5c6\uc74c", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c\uba85", None))
        self.groupBox_detail.setTitle(QCoreApplication.translate("MainWindow", u"\uacf5\uc0ac \uc815\ubcf4 \uc218\uc815", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\uad6c\uac04\uba85", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uacf5\uc0ac\uba85", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uacf5\uc5c5\uccb4", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\uacf5\uc0ac\uc77c\uc790", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\ub2f4\ub2f9\uc790", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\uacf5\uc815\uba85", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c", None))
    # retranslateUi

