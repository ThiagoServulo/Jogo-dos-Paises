from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
from bs4 import BeautifulSoup
from ui_tela_resultado import CriarTelaResultado
import numpy as np
import urllib.request
import random
import sys
import requests

paises = {'AR': 'Argentina', 'BO': 'Bolívia', 'BR': 'Brasil', 'CL': 'Chile', 'CO': 'Colômbia', 'EC': 'Equador',
          'GY': 'Guiana', 'PY': 'Paraguai', 'PE': 'Peru', 'SR': 'Suriname', 'UY': 'Uruguai', 'VE': 'Venezuela',
          'BZ': 'Belize', 'NI': 'Nicarágua', 'CU': 'Cuba', 'JM': 'Jamaica', 'CR': 'Costa Rica', 'PA': 'Panamá',
          'DM': 'Dominica', 'LC': 'Santa Lúcia', 'SV': 'El Salvador', 'AG': 'Antígua e Barbuda',
          'DO': 'República Dominicana', 'KN': 'São Cristóvão e Névis', 'GT': 'Guatemala', 'BS': 'Bahamas',
          'GD': 'Granada', 'VC': 'São Vicente e Granadinas', 'HN': 'Honduras', 'BB': 'Barbados', 'HT': 'Haiti',
          'TT': 'Trinidad e Tobago', 'CA': 'Canadá', 'US': 'Estado Unidos', 'MX': 'México', 'AU': 'Austrália',
          'FM': 'Estados Federados da Micronésia', 'FJ': 'Fiji', 'MH': 'Ilhas Marshall', 'SB': 'Ilhas Salomão',
          'KI': 'Kiribati', 'NR': 'Nauru', 'NZ': 'Nova Zelândia', 'PW': 'Palau', 'PG': 'Papua-Nova Guiné',
          'WS': 'Samoa', 'TO': 'Tonga', 'TV': 'Tuvalu', 'VU': 'Vanuatu', 'ZA': 'África do Sul', 'GW': 'Guiné-Bissau',
          'KE': 'Quênia', 'AO': 'Angola', 'GQ': 'Guiné Equatorial', 'CF': 'República Centro-Africana',
          'DZ': 'Argélia', 'MG': 'Ilhas de Madagascar', 'CD': 'República Democrática do Congo', 'BJ': 'Benin',
          'CV': 'Ilhas de Cabo Verde', 'CG': 'República do Congo', 'BW': 'Botsuana', 'KM': 'Ilha de Comores',
          'MU': 'República de Maurício', 'BF': 'Burkina Faso', 'ST': 'Ilhas São Tomé e Príncipe', 'RW': 'Ruanda',
          'BI': 'Burundi', 'SC': 'Ilhas Seychelles', 'SN': 'Senegal', 'CM': 'Camarões', 'LS': 'Lesoto',
          'SL': 'Serra Leoa', 'TD': 'Chade', 'LR': 'Libéria', 'SO': 'Somália', 'CI': 'Costa do Marfim',
          'LY': 'Líbia', 'DJ': 'Djibouti', 'MW': 'Malauí', 'SG': 'Sudão', 'EG': 'Egito', 'ML': 'Mali',
          'ER': 'Eritreia', 'MA': 'Marrocos', 'TZ': 'Tanzânia', 'ET': 'Etiópia', 'MR': 'Mauritânia', 'TG': 'Togo',
          'GA': 'Gabão', 'MZ': 'Moçambique', 'TN': 'Tunísia', 'GM': 'Gâmbia', 'NA': 'Namíbia', 'UG': 'Uganda',
          'GH': 'Gana', 'NE': 'Níger', 'ZM': 'Zâmbia', 'GN': 'Guiné', 'NG': 'Nigéria', 'ZW': 'Zimbabue',
          'AL': 'Albânia', 'DE': 'Alemanha', 'AD': 'Andorra', 'AT': 'Áustria', 'BE': 'Bélgica',
          'BA': 'Bósnia e Herzegovina', 'BG': 'Bulgária', 'KZ': 'Cazaquistão', 'CY': 'Chipre', 'HR': 'Croácia',
          'DK': 'Dinamarca', 'SK': 'Eslováquia', 'SI': 'Eslovênia', 'ES': 'Espanha', 'EE': 'Estônia',
          'FI': 'Finlândia', 'FR': 'França', 'GR': 'Grécia', 'HU': 'Hungria', 'IE': 'Irlanda', 'IS': 'Islândia',
          'IT': 'Itália', 'LV': 'Letônia', 'LI': 'Liechtenstein', 'LT': 'Lituânia', 'LU': 'Luxemburgo', 'MT': 'Malta',
          'MC': 'Mônaco', 'ME': 'Montenegro', 'NO': 'Noruega', 'PL': 'Polônia', 'PT': 'Portugal', 'RO': 'Romênia',
          'RU': 'Rússia', 'SM': 'San Marino', 'RS': 'Sérvia', 'SE': 'Suécia', 'CH': 'Suíça', 'TR': 'Turquia',
          'UA': 'Ucrânia', 'AF': 'Afeganistão', 'SA': 'Arábia Saudita', 'AM': 'Armênia', 'AZ': 'Azerbaijão',
          'BD': 'Bangladesh', 'BN': 'Brunei', 'BT': 'Butão', 'KH': 'Camboja', 'KR': 'Coreia do Sul',
          'QA': 'Catar', 'CN': 'China', 'AE': 'Emirados Árabes', 'UZ': 'Uzbequistão', 'VN': 'Vietnã',
          'PH': 'Filipinas', 'GE': 'Geórgia', 'YE': 'Iêmen', 'IN': 'Índia', 'ID': 'Indonésia', 'IR': 'Irã',
          'IQ': 'Iraque', 'IL': 'Israel', 'JP': 'Japão', 'JO': 'Jordânia', 'KW': 'Kuwait', 'LA': 'Laos',
          'LB': 'Líbano', 'MY': 'Malásia', 'MV': 'Maldivas', 'MM': 'Mianmar', 'MN': 'Mongólia',
          'NP': 'Nepal', 'OM': 'Omã', 'PK': 'Paquistão', 'KG': 'Quirguistão', 'SY': 'Síria', 'LK': 'Sri Lanka',
          'TH': 'Tailândia', 'TL': 'Timor-Leste', 'TM': 'Turcomenistão'}


class Ui_tela_jogo(object):

    pontuacao = 0
    pais = ''
    pais_sigla = ''
    lista_paises = []
    paises_sorteados = []

    def setupUi(self, tela_jogo):
        if not tela_jogo.objectName():
            tela_jogo.setObjectName(u"tela_jogo")
        tela_jogo.resize(520, 510)
        tela_jogo.setMinimumSize(QSize(520, 510))
        tela_jogo.setMaximumSize(QSize(520, 510))
        icon = QIcon()
        icon.addFile(u"icone_globo.ico", QSize(), QIcon.Normal, QIcon.Off)
        tela_jogo.setWindowIcon(icon)
        self.tela_resultado = CriarTelaResultado()
        self.centralwidget = QWidget(tela_jogo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 20, 481, 451))
        self.label_bandeira = QLabel(self.groupBox)
        self.label_bandeira.setObjectName(u"label_bandeira")
        self.label_bandeira.setGeometry(QRect(120, 60, 221, 131))
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
        self.botao_pular.setGeometry(QRect(20, 380, 100, 41))
        self.botao_pular.setFont(font1)
        self.botao_meio_a_meio = QPushButton(self.groupBox)
        self.botao_meio_a_meio.setObjectName(u"botao_meio_a_meio")
        self.botao_meio_a_meio.setGeometry(QRect(130, 380, 100, 41))
        self.botao_meio_a_meio.setFont(font1)
        self.botao_confirmar = QPushButton(self.groupBox)
        self.botao_confirmar.setObjectName(u"botao_confirmar")
        self.botao_confirmar.setGeometry(QRect(350, 380, 100, 41))
        self.botao_confirmar.setFont(font1)
        self.botao_dica = QPushButton(self.groupBox)
        self.botao_dica.setObjectName(u"botao_dica")
        self.botao_dica.setGeometry(QRect(240, 380, 100, 41))
        self.botao_dica.setFont(font1)
        tela_jogo.setCentralWidget(self.centralwidget)

        self.tela_resultado.botao_sair.clicked.connect(self.tela_resultado.close)
        self.tela_resultado.botao_novo_jogo.clicked.connect(self.novo_jogo)
        self.botao_pular.clicked.connect(self.pular)
        self.botao_confirmar.clicked.connect(self.confirmar_opcao)
        self.botao_meio_a_meio.clicked.connect(self.eliminar_duas_opcoes)
        self.botao_dica.clicked.connect(self.gerar_dica)
        self.sortear_paises()
        self.buscar_bandeira()

        self.retranslateUi(tela_jogo)
        QMetaObject.connectSlotsByName(tela_jogo)
    # setupUi

    def gerar_dica(self):
        resposta = requests.get(f'https://servicodados.ibge.gov.br/api/v1/paises/{Ui_tela_jogo.pais_sigla}/')
        resposta = str(resposta.json())
        tipo = random.randint(1, 2)
        if tipo == 1:
            resposta = resposta.split("capital': {'nome': '")
            resposta = resposta[1].split("'")
            resposta = f'A capital deste país é {resposta[0]}'
        else:
            resposta = resposta.split("'localizacao':")
            resposta = resposta[1].split("'sub-regiao'")
            resposta = resposta[0].split("'nome': '")
            resposta = resposta[1].split("'")
            resposta = f'Este país está localizado no seguinte continente: {resposta[0]}'
        QMessageBox.question(self, 'Dica', f'{resposta}', QMessageBox.Yes, QMessageBox.Yes)
        self.botao_dica.setEnabled(False)
    # gerar_dica

    def novo_jogo(self):
        Ui_tela_jogo.pontuacao = 0
        Ui_tela_jogo.lista_paises = []
        self.zerar_dados()
        self.sortear_paises()
        self.buscar_bandeira()
        self.tela_resultado.hide()
        self.radio_button_1.setChecked(False)
        self.radio_button_2.setChecked(False)
        self.radio_button_3.setChecked(False)
        self.radio_button_4.setChecked(False)
        self.botao_pular.setEnabled(True)
        self.botao_meio_a_meio.setEnabled(True)
        self.botao_dica.setEnabled(True)
    # novo_jogo

    def mostra_tela_resultado(self):
        self.tela_resultado.label_resultado.setText(f'Sua potuação final foi {Ui_tela_jogo.pontuacao}')
        self.tela_resultado.show()
    # mostra_tela_resultado

    def pular(self):
        self.botao_pular.setEnabled(False)
        Ui_tela_jogo.pontuacao += 1
        self.zerar_dados()
        self.sortear_paises()
        self.buscar_bandeira()
    # pular

    def eliminar_duas_opcoes(self):
        opcoes = [0, 1, 2, 3]
        random.shuffle(opcoes)
        opcoes_eliminadas = 0
        while opcoes_eliminadas < 2:
            opcao = opcoes.pop()
            if Ui_tela_jogo.paises_sorteados[opcao] != Ui_tela_jogo.pais:
                opcoes_eliminadas += 1
                if opcao == 0:
                    self.radio_button_1.setEnabled(False)
                elif opcao == 1:
                    self.radio_button_2.setEnabled(False)
                elif opcao == 2:
                    self.radio_button_3.setEnabled(False)
                elif opcao == 3:
                    self.radio_button_4.setEnabled(False)
        self.botao_meio_a_meio.setEnabled(False)
    # eliminar_duas_opcoes

    def confirmar_opcao(self):
        if self.radio_button_1.isChecked():
            self.radio_button_1.setEnabled(False)
            opcao = 0
        elif self.radio_button_2.isChecked():
            self.radio_button_2.setEnabled(False)
            opcao = 1
        elif self.radio_button_3.isChecked():
            self.radio_button_3.setEnabled(False)
            opcao = 2
        elif self.radio_button_4.isChecked():
            self.radio_button_4.setEnabled(False)
            opcao = 3
        else:
            return

        if Ui_tela_jogo.paises_sorteados[opcao] == Ui_tela_jogo.pais:
            if len(Ui_tela_jogo.paises_sorteados) >= (len(paises) - 5):
                print('Você ganhou')
            Ui_tela_jogo.pontuacao += 1
            self.zerar_dados()
            self.sortear_paises()
            self.buscar_bandeira()
        else:
            self.mostra_tela_resultado()
            Ui_tela_jogo.pontuacao = 0
            Ui_tela_jogo.lista_paises = []
            self.zerar_dados()
    # confirmar_opcao

    def retranslateUi(self, tela_jogo):
        tela_jogo.setWindowTitle(QCoreApplication.translate("tela_jogo", u"Jogo dos Países", None))
        self.groupBox.setTitle("")
        self.label_bandeira.setText("")
        self.label_pergunta.setText(QCoreApplication.translate("tela_jogo", u"Essa bandeira é de qual país ?", None))
        self.botao_pular.setText(QCoreApplication.translate("tela_jogo", u"Pular", None))
        self.botao_meio_a_meio.setText(QCoreApplication.translate("tela_jogo", u"Meio a Meio", None))
        self.botao_confirmar.setText(QCoreApplication.translate("tela_jogo", u"Confirmar", None))
        self.botao_dica.setText(QCoreApplication.translate("tela_jogo", u"Dica", None))
    # retranslateUi

    def zerar_dados(self):
        Ui_tela_jogo.pais = ''
        Ui_tela_jogo.pais_sigla = ''
        Ui_tela_jogo.paises_sorteados = []
        self.radio_button_1.setEnabled(True)
        self.radio_button_2.setEnabled(True)
        self.radio_button_3.setEnabled(True)
        self.radio_button_4.setEnabled(True)
        self.radio_button_1.setChecked(False)
        self.radio_button_2.setChecked(False)
        self.radio_button_3.setChecked(False)
        self.radio_button_4.setChecked(False)
    # zerar_dados

    def sortear_paises(self):
        while True:
            pais_sorteado = random.choice(list(paises))
            pais = paises[pais_sorteado]
            if pais not in Ui_tela_jogo.lista_paises:
                Ui_tela_jogo.lista_paises.append(pais)
                Ui_tela_jogo.paises_sorteados.append(pais)
                Ui_tela_jogo.pais = pais
                Ui_tela_jogo.pais_sigla = pais_sorteado
                break
        while True:
            if len(Ui_tela_jogo.paises_sorteados) == 4:
                random.shuffle(Ui_tela_jogo.paises_sorteados)
                break
            pais_sorteado = random.choice(list(paises))
            pais = paises[pais_sorteado]
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
        image = QImage.fromData(QByteArray(image.tobytes()))
        self.label_bandeira.setPixmap(QPixmap.fromImage(image))
    # buscar_bandeira


class CriarTelaPrincipal(QtWidgets.QMainWindow, Ui_tela_jogo):
    def __init__(self):
        super(CriarTelaPrincipal, self).__init__()
        self.setupUi(self)

    def closeEvent(self, event):
        event.accept()
        sys.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window_login = CriarTelaPrincipal()
    window_login.show()
    sys.exit(app.exec_())
