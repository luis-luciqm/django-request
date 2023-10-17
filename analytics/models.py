from django.db import models
# Create your models here.

class AccessForAnalytics(models.Model):

    TYPE_PAGE = (
        ('HOME', 'HOME'),
        ('DETAIL', 'DETAIL')
    )

    page = models.CharField('Página', choices = TYPE_PAGE, max_length = 10)
    value_page = models.CharField('Valor da Página', max_length = 455)
    accessed_at = models.DateTimeField('Acessado em', auto_now_add = True)
    ip = models.CharField('Endereço IP do Acesso', max_length = 50)
    # user agent

    class Meta:
        verbose_name = 'Acessos'
        verbose_name_plural = 'Acessos'
