from django.contrib import admin
from.models import User,Person,Students,identification_types,cities,departments,cpuntries
# Register your models here.
class UserFields(admin.ModelAdmin):
    list_display = ('email', 'password', 'status')


class PersonFields(admin.ModelAdmin):
    list_display = ('firstname', 'lastname',' age','ident_number')


admin.site.register(User)
admin.site.register(Person)
admin.site.register(Students)
admin.site.register(identification_types)
admin.site.register(cities)
admin.site.register(departments)
admin.site.register(cpuntries)