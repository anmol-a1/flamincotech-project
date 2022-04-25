from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import datetime
import random
class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user
class NewUser(AbstractBaseUser, PermissionsMixin):
    empid=models.AutoField(primary_key=True)
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=80, blank=True)
    Address = models.CharField(_(
        'address'), max_length=300, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']
    
    def __int__(self):
        return self.id
class InputConfiguration(models.Model):
    sr_no=models.IntegerField()
    desc=models.CharField(max_length=500)
    ft_hardware=models.IntegerField()
    active=models.IntegerField()
    passive=models.IntegerField()
    ddcsensor=models.IntegerField()
    thirdparty=models.IntegerField()
    cabpiptray=models.IntegerField()
    ft_hardware1=models.IntegerField()
    active1=models.IntegerField()
    passive1=models.IntegerField()
    ddcsensor1=models.IntegerField()
    thirdparty1=models.IntegerField()
    cabpiptray1=models.IntegerField()
    ftmandayeffort=models.IntegerField()
    othersmicffort=models.IntegerField()
    ft2=models.IntegerField()
    ft3=models.IntegerField()
    ft4=models.IntegerField()


class vpss(models.Model):
    sr_no=models.IntegerField()
    MakeBrand=models.CharField(max_length=500)
    InstallationEquipments=models.CharField(max_length=500)
    UnitDescription=models.CharField(max_length=500)
    Qty=models.IntegerField()
    InputPrice =models.IntegerField()
    Discount=models.IntegerField()
    DiscountedPrice=models.IntegerField()
    Freight=models.IntegerField()
    InputCostInclusiveoffreight=models.IntegerField()
    InterestCOM=models.IntegerField()
    UnitCost=models.IntegerField()
    InwardTax=models.IntegerField()
    UnitCostInclusiveofRisk=models.IntegerField()
    ContigencyPercentage=models.IntegerField()
    UnitCostInclusiveofContigency=models.IntegerField()
    TotalCost=models.IntegerField()
    Margin=models.IntegerField()
    TotalPrice=models.IntegerField()
    WarrantyCharges=models.IntegerField()
    UnitPrice=models.IntegerField()
    FinalTotalPrice=models.IntegerField()
    InsuranceCharges =models.IntegerField()
    ListPricewithoutRoundup =models.IntegerField()
    ListPricewithRoundedup =models.IntegerField()