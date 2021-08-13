from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
from bs4 import BeautifulSoup
import numpy as np
import urllib.request
import cv2
import random
import sys
import requests

paises = ['Canadá', 'Estado Unidos', 'México', 'Austrália', 'Estados Federados da Micronésia', 'Fiji', 'Ilhas Marshall',
          'Ilhas Salomão', 'Kiribati', 'Nauru', 'Nova Zelândia', 'Palau', 'Papua-Nova Guiné', 'Samoa', 'Tonga',
          'Tuvalu', 'Vanuatu', 'África do Sul', 'Guiné-Bissau', 'Quênia', 'Angola', 'Guiné Equatorial',
          'República Centro-Africana', 'Argélia', 'Ilhas de Madagascar', 'República Democrática do Congo', 'Benin',
          'Ilhas de Cabo Verde', 'República do Congo', 'Botsuana', 'Ilha de Comores', 'República de Maurício',
          'Burkina Faso', 'Ilhas São Tomé e Príncipe', 'Ruanda', 'Burundi', 'Ilhas Seychelles', 'Senegal', 'Camarões',
          'Lesoto', 'Serra Leoa', 'Chade', 'Libéria', 'Somália', 'Costa do Marfim', 'Líbia', 'Djibouti', 'Malauí',
          'Sudão', 'Egito', 'Mali', 'Eritreia', 'Marrocos', 'Tanzânia', 'Etiópia', 'Mauritânia', 'Togo', 'Gabão',
          'Moçambique', 'Tunísia', 'Gâmbia', 'Namíbia', 'Uganda', 'Gana', 'Níger', 'Zâmbia', 'Guiné', 'Nigéria',
          'Zimbabue', 'Albânia', 'Alemanha', 'Andorra', 'Áustria', 'Bélgica', 'Bósnia e Herzegovina', 'Bulgária',
          'Cazaquistão', 'Chipre', 'Croácia', 'Dinamarca', 'Eslováquia', 'Eslovênia', 'Espanha', 'Estônia', 'Finlândia',
          'França', 'Grécia', 'Hungria', 'Irlanda', 'Islândia', 'Itália', 'Letônia', 'Liechtenstein', 'Lituânia',
          'Luxemburgo', 'Malta', 'Moldávia', 'Mônaco', 'Montenegro', 'Noruega', 'Países Baixos', 'Polônia',
          'Portugal', 'Tchéquia', 'Macedônia do Norte', 'Inglaterra', 'Irlanda do Norte', 'Escócia', 'País de Gales',
          'Romênia', 'Rússia', 'San Marino', 'Sérvia', 'Suécia', 'Suíça', 'Turquia', 'Ucrânia', 'Vaticano',
          'Afeganistão', 'Arábia Saudita', 'Armênia', 'Azerbaijão', 'Bahrein', 'Bangladesh', 'Brunei', 'Butão',
          'Camboja', 'Cazaquistão', 'Catar', 'China', 'Chipre', 'Cingapura', 'Coreia do Norte', 'Coreia do Sul',
          'Egito', 'Emirados Árabes', 'Filipinas', 'Geórgia', 'Iêmen', 'Índia', 'Indonésia', 'Irã', 'Iraque', 'Israel',
          'Japão', 'Jordânia', 'Kuwait', 'Laos', 'Líbano', 'Malásia', 'Maldivas', 'Mianmar', 'Mongólia', 'Nepal', 'Omã',
          'Paquistão', 'Quirguistão', 'Síria', 'Sri Lanka', 'Tajiquistão', 'Tailândia', 'Timor-Leste', 'Turcomenistão',
          'Uzbequistão', 'Vietnã', 'Argentina', 'Bolívia', 'Brasil', 'Chile', 'Colômbia', 'Equador', 'Guiana',
          'Paraguai', 'Peru', 'Suriname', 'Uruguai', 'Venezuela', 'Belize', 'Nicarágua', 'Cuba', 'Jamaica',
          'Costa Rica', 'Panamá', 'Dominica', 'Santa Lúcia', 'El Salvador', 'Antígua e Barbuda', 'República Dominicana',
          'São Cristóvão e Névis', 'Guatemala', 'Bahamas', 'Granada', 'São Vicente e Granadinas', 'Honduras',
          'Barbados', 'Haiti', 'Trinidad e Tobago']


class Ui_tela_jogo(object):

    pais = ''
    lista_paises = []
    paises_sorteados = []

    def setupUi(self, tela_jogo):
        if not tela_jogo.objectName():
            tela_jogo.setObjectName(u"tela_jogo")
        tela_jogo.resize(522, 508)
        tela_jogo.setMaximumSize(QSize(800, 800))
        icon = QIcon()
        icon.addFile(u"icone_globo.png", QSize(), QIcon.Normal, QIcon.Off)
        tela_jogo.setWindowIcon(icon)
        self.centralwidget = QWidget(tela_jogo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 20, 481, 451))
        self.label_bandeira = QLabel(self.groupBox)
        self.label_bandeira.setObjectName(u"label_bandeira")
        self.label_bandeira.setGeometry(QRect(120, 60, 221, 131))
        self.label_bandeira.setPixmap(QPixmap(u"bandeira.png"))
        self.label_pergunta = QLabel(self.groupBox)
        self.label_pergunta.setObjectName(u"label_pergunta")
        self.label_pergunta.setGeometry(QRect(80, 10, 301, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_pergunta.setFont(font)
        self.radio_button_1 = QRadioButton(self.groupBox)
        self.radio_button_1.setObjectName(u"radio_button_1")
        self.radio_button_1.setGeometry(QRect(80, 200, 291, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.radio_button_1.setFont(font1)
        self.radio_button_2 = QRadioButton(self.groupBox)
        self.radio_button_2.setObjectName(u"radio_button_2")
        self.radio_button_2.setGeometry(QRect(80, 280, 291, 31))
        self.radio_button_2.setFont(font1)
        self.radio_button_3 = QRadioButton(self.groupBox)
        self.radio_button_3.setObjectName(u"radio_button_3")
        self.radio_button_3.setGeometry(QRect(80, 320, 291, 31))
        self.radio_button_3.setFont(font1)
        self.radio_button_4 = QRadioButton(self.groupBox)
        self.radio_button_4.setObjectName(u"radio_button_4")
        self.radio_button_4.setGeometry(QRect(80, 240, 291, 31))
        self.radio_button_4.setFont(font1)
        self.botao_pular = QPushButton(self.groupBox)
        self.botao_pular.setObjectName(u"botao_pular")
        self.botao_pular.setGeometry(QRect(40, 380, 121, 41))
        self.botao_pular.setFont(font1)
        self.botao_meio_a_meio = QPushButton(self.groupBox)
        self.botao_meio_a_meio.setObjectName(u"botao_meio_a_meio")
        self.botao_meio_a_meio.setGeometry(QRect(180, 380, 121, 41))
        self.botao_meio_a_meio.setFont(font1)
        self.botao_arriscar = QPushButton(self.groupBox)
        self.botao_arriscar.setObjectName(u"botao_arriscar")
        self.botao_arriscar.setGeometry(QRect(320, 380, 121, 41))
        self.botao_arriscar.setFont(font1)
        tela_jogo.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(tela_jogo)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 522, 21))
        self.menuJogo = QMenu(self.menubar)
        self.menuJogo.setObjectName(u"menuJogo")
        tela_jogo.setMenuBar(self.menubar)

        self.sortear_paises()
        self.buscar_bandeira()
        self.label_bandeira.setPixmap(QPixmap(u"bandeira.png"))

        self.menubar.addAction(self.menuJogo.menuAction())
        self.retranslateUi(tela_jogo)
        QMetaObject.connectSlotsByName(tela_jogo)
    # setupUi

    def retranslateUi(self, tela_jogo):
        tela_jogo.setWindowTitle(QCoreApplication.translate("tela_jogo", u"Jogo dos Países", None))
        self.groupBox.setTitle("")
        self.label_bandeira.setText("")
        self.label_pergunta.setText(QCoreApplication.translate("tela_jogo", u"Essa bandeira é de qual país ?", None))
        # self.radio_button_1.setText("")
        # self.radio_button_2.setText("")
        # self.radio_button_3.setText("")
        # self.radio_button_4.setText("")
        self.botao_pular.setText(QCoreApplication.translate("tela_jogo", u"Pular", None))
        self.botao_meio_a_meio.setText(QCoreApplication.translate("tela_jogo", u"Meio a Meio", None))
        self.botao_arriscar.setText(QCoreApplication.translate("tela_jogo", u"Arriscar", None))
        self.menuJogo.setTitle(QCoreApplication.translate("tela_jogo", u"Jogo", None))
    # retranslateUi

    def sortear_paises(self):
        while True:
            pais = random.choice(paises)
            if pais not in Ui_tela_jogo.lista_paises:
                Ui_tela_jogo.lista_paises.append(pais)
                Ui_tela_jogo.paises_sorteados.append(pais)
                Ui_tela_jogo.pais = pais
                break
        while True:
            if len(Ui_tela_jogo.paises_sorteados) == 4:
                random.shuffle(Ui_tela_jogo.paises_sorteados)
                break
            pais = random.choice(paises)
            if pais in Ui_tela_jogo.lista_paises:
                continue
            if pais not in Ui_tela_jogo.paises_sorteados:
                Ui_tela_jogo.paises_sorteados.append(pais)
        self.radio_button_1.setText(Ui_tela_jogo.paises_sorteados[0])
        self.radio_button_2.setText(Ui_tela_jogo.paises_sorteados[1])
        self.radio_button_3.setText(Ui_tela_jogo.paises_sorteados[2])
        self.radio_button_4.setText(Ui_tela_jogo.paises_sorteados[3])
    # sortear_paises

    def buscar_bandeira(self):
        pais = Ui_tela_jogo.pais.replace(' ', '+')
        resposta = requests.get(f'https://www.google.com/search?q=bandeira+{pais}&tbm=isch&ved=2ahUKEwjxiJCM66nyAh'
                                    f'WBjJUCHdT9AI0Q2-cCegQIABAA&oq=bandeira+finlandia&gs_lcp=CgNpbWcQAzIFCAAQgAQyBggAE'
                                    f'AgQHjIECAAQHjIGCAAQCBAeMgYIABAIEB4yBggAEAgQHjIGCAAQCBAeMgYIABAIEB4yBggAEAoQGDoGCA'
                                    f'AQBRAeUK9iWOVrYMRuaABwAHgAgAG7AYgBuQmSAQMwLjmYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&scli'
                                    f'ent=img&ei=0jYUYfHXGIGZ1sQP1PuD6Ag&bih=757&biw=1600')
        html_file = BeautifulSoup(resposta.text, "html.parser")
        link_img = html_file.prettify()
        link_img = link_img.split('<img alt=""')
        link_img = link_img[1].split('src="')
        link_img = link_img[1].split('"/>')
        resp = urllib.request.urlopen(link_img[0])
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        cv2.imwrite("bandeira.png", image)
    # buscar_bandeira


class CriarTelaPrincipal(QtWidgets.QMainWindow, Ui_tela_jogo):
    def __init__(self):
        super(CriarTelaPrincipal, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window_login = CriarTelaPrincipal()
    window_login.show()
    sys.exit(app.exec_())