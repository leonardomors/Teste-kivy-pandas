from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
import pandas as pd
import random

class MainWidget(BoxLayout):
    def __init__(self):
        super().__init__()
        self._db = pd.read_excel("teste.xlsx")

    def alterar_nome1(self):
        self._db['text'][0] = self.ids.nome_novo1.text
        self.ids.nome_atual1.text = self.ids.nome_novo1.text
        self._db.to_excel("teste.xlsx")

    def alterar_nome2(self):
        self._db['text'][1] = self.ids.nome_novo2.text
        self.ids.nome_atual2.text = self.ids.nome_novo2.text
        self._db.to_excel("teste.xlsx")

    def conectar_dados(self):
        self.ids.nome_atual1.text = str(self._db['text'][0])
        self.ids.nome_atual2.text = str(self._db['text'][1])

    # def atualizar_dados(self):
        
    #     print(self._db['text'][0])
    #     print(self._db['text'][1])
    #     print(self._db['text'][2])
    #     print(self._db['text'][3])
    #     self.ids.b1.text = str(self._db['text'][0])
    #     self.ids.b2.text = str(self._db['text'][1])
    #     self.ids.b3.text = str(self._db['text'][2])
    #     self.ids.b4.text = str(self._db['text'][3])
    # def alterar_planilha(self):
    #     LISTA_NOMES = ['leonardo','joana','joao','daiana','vinicius','vasco','preto','branco','macaco','baleia','chuva','fluminense','botafogo','maceta','juninho','blastoise','pikachu']
        
    #     self._db['text'][0] = str(random.choice(LISTA_NOMES))
    #     self._db['text'][1] = str(random.choice(LISTA_NOMES))
    #     self._db['text'][2] = str(random.choice(LISTA_NOMES))
    #     ,
    #     self._db['text'][3] = str(random.choice(LISTA_NOMES))
    #     self._db.to_excel("teste.xlsx")



