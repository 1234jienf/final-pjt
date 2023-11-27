from django.db import models

# Create your models here.

class Bank(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField()
    dcls_month = models.TextField()
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='deposit_products', null=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    join_deny = models.IntegerField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()

class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE, related_name = 'deposit_options')
    fin_prdt_cd = models.TextField()
    dcls_month = models.TextField()
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()

class SavingProducts(models.Model):
    fin_prdt_cd = models.TextField()
    dcls_month = models.TextField()
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='saving_products', null=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    join_deny = models.IntegerField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()

class SavingOptions(models.Model):
    product = models.ForeignKey(SavingProducts, on_delete=models.CASCADE, related_name = 'saving_options')
    fin_prdt_cd = models.TextField()
    dcls_month = models.TextField()
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()
