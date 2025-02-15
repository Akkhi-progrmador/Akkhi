from django.db import models

class Projecto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='portfolio/images/')
    link = models.URLField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
