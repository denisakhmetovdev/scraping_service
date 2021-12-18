from django.core import validators
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Введите корректно email адрес')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password,):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, password=password,)
        # user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True, verbose_name='email')
    first_name = models.CharField(max_length=35, verbose_name='Имя')
    last_name = models.CharField(max_length=35, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=40, blank=True, null=True, verbose_name='Отчество')
    phone = models.CharField(max_length=14,
                             validators=[validators.RegexValidator(regex='^((8|\+7)[\- ]?)?[0-9]{10}$')])
    date_joined = models.DateTimeField(verbose_name='Зарегистрирован', auto_now_add=True)
    is_active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural = 'Пользователи'

    def get_full_name(self):
        if self.patronymic:
            full_name = f'{self.last_name} {self.first_name} {self.patronymic}'
        else:
            full_name = f'{self.first_name} {self.last_name}'
        return full_name

    def get_short_name(self):
        return f'{self.first_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.admin
