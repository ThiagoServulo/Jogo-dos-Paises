from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys

class Ui_tela_resultado(object):
    def setupUi(self, tela_resultado):
        if not tela_resultado.objectName():
            tela_resultado.setObjectName(u"tela_resultado")
        tela_resultado.resize(290, 180)
        tela_resultado.setMinimumSize(QSize(290, 180))
        tela_resultado.setMaximumSize(QSize(290, 180))
        icon = QIcon()
        icon.addFile(u"icone_globo.ico", QSize(), QIcon.Normal, QIcon.Off)
        tela_resultado.setWindowIcon(icon)
        self.centralwidget = QWidget(tela_resultado)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 241, 61))
        font = QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_resultado = QLabel(self.centralwidget)
        self.label_resultado.setObjectName(u"label_resultado")
        self.label_resultado.setGeometry(QRect(20, 70, 241, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_resultado.setFont(font1)
        self.label_resultado.setAlignment(Qt.AlignCenter)
        self.botao_sair = QPushButton(self.centralwidget)
        self.botao_sair.setObjectName(u"pushButton")
        self.botao_sair.setGeometry(QRect(10, 130, 121, 41))
        self.botao_sair.setFont(font1)
        self.botao_novo_jogo = QPushButton(self.centralwidget)
        self.botao_novo_jogo.setObjectName(u"pushButton_2")
        self.botao_novo_jogo.setGeometry(QRect(150, 130, 121, 41))
        self.botao_novo_jogo.setFont(font1)
        tela_resultado.setCentralWidget(self.centralwidget)

        self.retranslateUi(tela_resultado)

        QMetaObject.connectSlotsByName(tela_resultado)
    # setupUi

    def retranslateUi(self, tela_resultado):
        tela_resultado.setWindowTitle(QCoreApplication.translate("tela_resultado", u"Fim de Jogo", None))
        self.label.setText(QCoreApplication.translate("tela_resultado", u"Fim de Jogo", None))
        self.label_resultado.setText(QCoreApplication.translate("tela_resultado", u"Sua pontuação final foi: XX", None))
        self.botao_sair.setText(QCoreApplication.translate("tela_resultado", u"Sair", None))
        self.botao_novo_jogo.setText(QCoreApplication.translate("tela_resultado", u"Novo Jogo", None))
    # retranslateUi


class CriarTelaResultado(QtWidgets.QMainWindow, Ui_tela_resultado):
    def __init__(self):
        super(CriarTelaResultado, self).__init__()
        self.setupUi(self)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Sair do jogo', 'Deseja sair do jogo?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
            sys.exit()
        else:
            event.ignore()
