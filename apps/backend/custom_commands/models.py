from django.db import models
# Create your models here.
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
        
    class Meta:
        verbose_name = 'Categorie'

    def __str__(self) -> str:
            return self.name

class UserAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username,email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username = username,
            email=email,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username,
            email,
            password=password,
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

    
class UserAccount(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


    class Meta:
        verbose_name = "Utilisateurs"
        ordering = ['-is_staff']
        
        
    def __str__(self):
            return self.email

class BlogPost(models.Model):
    #author = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category,)
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField()

    @property
    def publish_string(self):
        if self.published:
            return "L'article est publié"
        return "L'article n'est pas disponible"
    
    def save( self, *args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.title)
        super().save(*args,  **kwargs)


    class Meta:
        verbose_name = 'Article'
        ordering = ["published", "-date"]

    def __str__(self) -> str:
            return self.title