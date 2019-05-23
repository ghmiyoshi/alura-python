from django.db import models

class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(models.Q(name__icontains=query) | models.Q(description__icontains=query)) # Método que busca um curso pelo nome e descrição


class Course(models.Model): # As classes devem herdar models.Model para ter facilidade em criar tabelas, acessar e manipular os dados

    name = models.CharField('Nome', max_length=100) # CharField - Campo de texto do Django
    slug = models.SlugField('Atalho') # SlugField - Código/valor único do curso
    descript = models.TextField('Descricao Simples', blank=True) # TextField - Campo de texto do Django sem tamanho máximo. blank=true campo não obrigatório
    about = models.TextField('Sobre o curso', blank=True)
    start_date = models.DateField('Data de Início', null=True, blank=True) # DateField - Campo de data do Django. null=True campo pode ser nulo
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)

    # Variáveis importantes para nível de log
    created_at = models.DateTimeField('Criado em ', auto_now_add=True) # DateTimeField - Campo data/hora do Django. Sempre que criar um curso será salvo a data/hora atual
    updated_at = models.DateTimeField('Atualizado em ', auto_now_add=True) # Sempre que o curso for salvo será alterado essa variável para data/hora atual

    objects = CourseManager() # Manager do models

    def __str__(self):
        return self.name

    class Meta: # Classe para mudar os nomes Course e Courses no Django admin
        verbose_name='Curso'
        verbose_name='Cursos'
        ordering = ['name'] # Ordena por nome no Django admin