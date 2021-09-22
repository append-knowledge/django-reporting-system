
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, email,roll, password=None):
        """
        Creates and saves a User with the given email, role and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            roll=roll,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,roll, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            roll=roll,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    options=(('faculty','faculty'),('HR','HR'),('COUNSILER','COUNSILER'))
    roll=models.CharField(max_length=40,choices=options,default='faculty')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['roll','password']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Course(models.Model):
    course_name=models.CharField(max_length=25,unique=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.course_name

class Batch(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    batch_name=models.CharField(max_length=25,unique=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        self.batch_name
