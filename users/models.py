from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin

'''
model for holding all the users in the club. 
'''
class MyUsersManager(BaseUserManager):

    def create_user(self,first_name,last_name,nat_id,email,phone_number,password):
        '''
        Manages the creation on student instances
        '''
        if not first_name:
            raise ValueError("Full name must be included")
        if not last_name:
            raise ValueError("Please add an admission number")
        if not nat_id:
            raise ValueError("User must have a national_id")
        if not email:
            raise ValueError("Please add the school email address")
        if not phone_number:
            raise ValueError("Please add a phone number")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email),
            last_name = last_name,
            phone_number = phone_number,
            nat_id=nat_id,
            first_name = first_name,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,first_name,last_name,nat_id,email,phone_number,password):
        '''
        Manages the creation of superuser 
        '''
        user = self.create_user(
            first_name=first_name,
            last_name = last_name,
            nat_id = nat_id,                        
            email=self.normalize_email(email=email),
            phone_number=phone_number,
            password=password,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user

class MyUser(AbstractBaseUser, PermissionsMixin):
    first_name        = models.CharField(max_length=50,null= False)
    last_name        = models.CharField(max_length=50,null= False)
    nat_id         = models.PositiveIntegerField(null= False,unique=True)       
    email            = models.EmailField(verbose_name="email", max_length=100, unique=True)
    phone_number     = models.BigIntegerField(unique=True,null= False)
    date_joined      = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login       = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin         = models.BooleanField(default=False)
    is_active        = models.BooleanField(default=True)
    is_staff         = models.BooleanField(default=False)
    is_superuser     = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['nat_id','phone_number','first_name','last_name','password']

    objects = MyUsersManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm, obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True


from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=MyUser) # creates token when user registers
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)