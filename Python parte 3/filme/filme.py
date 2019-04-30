class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return "Nome: {} ano: {} likes: {}".format(self._nome, self.ano, self._likes)


class Playlist:
    def __init__(self, nome, programas):
        self._nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return "Nome: {} ano: {} likes: {} duracao: {} min".format(self._nome, self.ano, self._likes, self.duracao)

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return "Nome: {} ano: {} likes: {} temporadas: {}".format(self._nome, self.ano, self._likes, self.temporadas)

# Filmes
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()
vingadores.dar_likes()

click = Filme('click',2012,120)
click.dar_likes()
click.dar_likes()
click.dar_likes()

# Séries
atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
#print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}')
#print('Nome: {} - Ano: {}'.format(atlanta.nome,atlanta.ano))

got = Serie('game of thrones', 2010, 8)
got.dar_likes()
got.dar_likes()
got.dar_likes()
got.dar_likes()
got.dar_likes()

filmes_e_series = [vingadores, atlanta, click, got]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

for programa in playlist_fim_de_semana:
    print(programa)




