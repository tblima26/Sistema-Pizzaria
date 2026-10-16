from django.db import models

class Pizza(models.Model):
  CATEGORIAS = [
    ('tradicional', 'Tradicional'),
    ('especial', 'Especial'),
    ('doce', 'Doce'),
  ]
  nome = models.CharField(max_length=100)
  preco = models.DecimalField(max_digits=7, decimal_places=2)
  categoria = models.CharField(max_length=20, choices=CATEGORIAS)
  ingredientes = models.TextField()

  def __str__(self):
      return self.nome