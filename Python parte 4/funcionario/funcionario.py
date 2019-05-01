class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostra_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostra_tarefas(self):
        print("Fez muita coisa Caelum")

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando curso desse mês')

class Alura(Funcionario):
    # def mostra_tarefas(self):
    #     print('Fez muita coisa Alura')

    def busca_perguntas_sem_respostas(self):
        print('Mostrando perguntas não respondidas no fórum')

class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum, Hipster):
    pass

ryan = Senior('Ryan')
print(ryan)

