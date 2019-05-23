from django.contrib import admin

from .models import Course # Importa o model que deseja cadastrar no admin

class CourseAdmin(admin.ModelAdmin): # Classe para customizar o admin de acordo com o model
    list_display = ['name', 'slug', 'start_date', 'created_at'] # Defini as colunas das tabelas que aparecem no Django admin
    search_fields = ['name', 'slug'] # Defini os valores que o curso é encontrado no pesquisar no Django admin, nesse caso, pelo nome ou pelo atalho
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Course, CourseAdmin) # Cadastra o model Course no admin e faz as customizações

