import sys
import os
from PySide6.QtGui import QPalette, QPixmap, QBrush, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow
import random

class MainWindow(QMainWindow,Ui_MainWindow):

    def __init__(self, parent= None):
        super().__init__(parent)
        self.setupUi(self)
        self.resize(900,500)
        self.nao.clicked.connect(self.button_clicked)
        self.nao.enterEvent = self.button_enterEvent
        self.sim.clicked.connect(self.button_sim)
        self.label.setText('Vamos ficar juntos para sempre?') #troca o titulo

        # Carrega a imagem
        path = os.path.join(os.path.dirname(__file__), "files/image.jpg")
        pixmap = QPixmap(path)

        # Define a imagem como fundo da janela
        palette = self.palette()
        palette.setBrush(QPalette.Window, QBrush(pixmap))
        self.setPalette(palette)

    def button_enterEvent(self, event):
        self.muda_botao()

    def button_clicked(self):
        self.muda_botao()

    def muda_botao(self):
        # Gera coordenadas aleatórias para o botão
        x = random.randint(0, self.width() - self.nao.width())
        y = random.randint(0, self.height() - self.nao.height())

        # Define a nova posição do botão
        self.nao.move(x,y)

    def adjustFixedSize(self):
        # Ultimas coisas a colocar
        self.setFixedSize(self.width(), self.height())

    def button_sim(self):
    # Faz o botão 'não' sumir
        self.nao.hide()

        # Faz o botão 'sim' sumir
        self.sim.hide()

        # Altera o texto do QLabel para "Você escolheu SIM"
        self.label.setText("Ficar sem mim não é uma opção!!!") #Titulo de quando aperta sim
 

if __name__=='__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()

    # Criar um objeto QIcon a partir do arquivo de imagem
    path = os.path.join(os.path.dirname(__file__), "files/icone.png")
    icon = QIcon(path)

    # Definir o ícone da janela
    mainwindow.setWindowIcon(icon)
    mainwindow.setWindowTitle("Para todo sempre")


    mainwindow.adjustFixedSize()
    mainwindow.show()
    app.exec()