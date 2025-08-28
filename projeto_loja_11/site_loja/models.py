from django.db import models
from django.contrib.auth.models import User # Importa o modelo de usuário padrão do Django
from PIL import Image # Importa o Image para redimensionar a imagem

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem = models.ImageField(default='perfil_padrao.jpg', upload_to='imagens_perfil')
    cpf = models.CharField( max_length=11)
    email = models.EmailField( max_length=254)
    tel_fixo = models.TextField(_("+dd"))
    data de nascimento = models.DateField( auto_now=False, auto_now_add=False)
    genero = models.CharField( max_length=50)

    
        
    
        class Meta:
            verbose_name = _("")
            verbose_name_plural = _("s")
    
        def __str__(self):
            return self.name
    
        def get_absolute_url(self):
            return reverse("_detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return f'Perfil de {self.usuario.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # Salva a imagem primeiro

        img = Image.open(self.imagem.path) # Abre a imagem
        if img.height > 300 or img.width > 300: # Verifica se é maior que 300x300 pixels
            output_size = (300, 300)
            img.thumbnail(output_size) # Redimensiona a imagem
            img.save(self.imagem.path) # Salva a imagem redimensionada

    ##class endereço
class endereço( models.Model):
    cep = models.models.CharField( max_length=50)
    bairro = models.CharField( max_length=50)
    rua = models.models.CharField(max_length=50)
    numemero = models.CharField( max_length=50)
    complemento = models.CharField( max_length=50)



##
    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
)


##
# Modelo - Contatos (Aula 11.02.02)
##
class ContactRequest(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome")
    email = models.EmailField(verbose_name="E-mail")
    mensagem = models.TextField(verbose_name="Mensagem")
    
    # Campos de data
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    data_atualizacao = models.DateTimeField(auto_now=True, 
                    verbose_name="Enviado em")
    
    def __str__(self):
        return f"Contato de {self.name} - {self.email}"

class endereço (class Mixin(models.Model))
    class endereço