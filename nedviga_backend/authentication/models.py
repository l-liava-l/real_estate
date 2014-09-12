#coding: utf-8

import pdb
import random
import string

from django.core.validators import RegexValidator

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from authentication.utils import re_phone

DEFAULT_PASSWORD = 'yorcc-lab'


class UserManager(BaseUserManager):

    def _create_user(self, phone, password, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username and password.
        """
        now = timezone.now()
        if not phone:
            raise ValueError('The given username must be set')

        user = self.model(phone=phone,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(DEFAULT_PASSWORD)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        return self._create_user(phone, DEFAULT_PASSWORD, False, False, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        return self._create_user(phone, DEFAULT_PASSWORD, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField('Номер телефона', unique=True, max_length=15, validators=[RegexValidator(re_phone)])
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    date_joined = models.DateTimeField('Когда зарегистрировался?', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('id',)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        return self.phone

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.phone

    def generate_sms_code(self):
        return ''.join([random.choice(string.digits) for i in range(4)])
