from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    ROLE_CHOICES = [   
        ('USR', 'Usuário'),
        ('RH', 'Recursos Humanos'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=3, choices=ROLE_CHOICES, default='USR')

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"

class Vaga(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    description = models.TextField(verbose_name="Descrição")
    location = models.CharField(max_length=100, verbose_name="Localização")
    salary = models.CharField(max_length=50, blank=True, null=True, verbose_name="Salário")
    requirements = models.TextField(blank=True, null=True, verbose_name="Requisitos")
    data_publication = models.DateField(auto_now_add=True, verbose_name="Data de Publicação")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Criado por")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Vaga"
        verbose_name_plural = "Vagas"
        ordering = ['-data_publication']

@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
