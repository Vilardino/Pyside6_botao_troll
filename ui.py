# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(854, 773)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 59, 841, 101))
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.sim = QPushButton(self.centralwidget)
        self.sim.setObjectName(u"sim")
        self.sim.setGeometry(QRect(180, 210, 151, 61))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.sim.setFont(font1)
        self.nao = QPushButton(self.centralwidget)
        self.nao.setObjectName(u"nao")
        self.nao.setGeometry(QRect(530, 210, 151, 61))
        self.nao.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Vamos ficar juntos para sempre?", None))
        self.sim.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.nao.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
    # retranslateUi

