from django.db import models

# Create your models here.

class servers(models.Model):
    user_nom = models.ManyToManyField('users',null=True, verbose_name='Пользователь')
    tarif_nom = models.ManyToManyField('tarif', null=True, verbose_name='Тариф')
    payday = models.DateField(verbose_name='payday', null=False)
    tarif_g_id = models.ManyToManyField('test', null=True, verbose_name='Тариф1')
    def __int__(self):
        return self.user_nom

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
    title1 = models.CharField(max_length = 255, verbose_name='title', null=True)
    use = models.ManyToManyField('tarif', null=True, verbose_name='Тариф')

    def display_test(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([tarif.tarif_group_id for tarif in self.tarif.all()[:3]])

    display_test.short_description = 'tarif'