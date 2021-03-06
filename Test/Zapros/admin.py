from django.contrib import admin
from .models import  tarif, users, servers, test

# Register your models here.




class TarifAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'link','speed','pay_period','tarif_group_id')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'login', 'name_last', 'name_first')
    list_display_links = ('id', 'login')
    search_fields = ('id', 'login')

class ServersAdmin(admin.ModelAdmin):
    list_display = ('id', 'payday')
    list_display_links = ('id', 'payday')
    search_fields = ('id', 'payday')

class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'pay_period')
    list_display_links = ('id', 'pay_period')
    search_fields = ('id', 'pay_period')

admin.site.register(tarif, TarifAdmin)
admin.site.register(users, UsersAdmin)
admin.site.register(servers, ServersAdmin)
admin.site.register(test, TestAdmin)
