from django.db import models

# Create your models here.



class tarif(models.Model):

    title = models.CharField(max_length = 255, verbose_name='title', null=False)
    price = models.DecimalField(max_digits=15, decimal_places=4, verbose_name='price', null=True)
    link = models.CharField(max_length = 255, verbose_name='link', null=True)
    speed = models.IntegerField(verbose_name='speed', null=True)
    pay_period = models.IntegerField(verbose_name='pay_period', null=True)
    tarif_group_id = models.IntegerField(verbose_name='tarif_group_id1', null=True)


    def __int__(self):
        return self.title

class users(models.Model):
    login = models.CharField(max_length = 12, verbose_name='login', null=True)
    name_last = models.CharField(max_length = 255, verbose_name='name_last', null=True)
    name_first = models.CharField(max_length = 255, verbose_name='name_first', null=True)


    def __str__(self):
        return self.login

class test(models.Model):
    pay_period = models.CharField(max_length = 255, verbose_name='1 месяц', null=True)
    pay_period3 = models.CharField(max_length=255, verbose_name='3 месяц', null=True)
    pay_period6 = models.CharField(max_length=255, verbose_name='6 месяц', null=True)
    pay_period12 = models.CharField(max_length=255, verbose_name='12 месяц', null=True)

    def __int__(self):
        return self.id



class servers(models.Model):
    user_id = models.ForeignKey('users', verbose_name='Пользователь', on_delete=models.CASCADE, null=True)
    tarif_id = models.ForeignKey('tarif', null=True, verbose_name='Тариф',on_delete=models.CASCADE)
    payday = models.DateField(verbose_name='payday', null=False)
    tarif_group_id = models.ForeignKey('test', null=True, verbose_name='Тариф',on_delete=models.CASCADE)
    def __int__(self):
        return f"{self.login} из категории \"{self.users.login}\""
