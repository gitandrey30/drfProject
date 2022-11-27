from django.contrib import admin

from .models import Category, Service, Salun, Auto, Warehouse, Buyer, Condition, Airboard, Airport, Person, House, Super


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Salun)
admin.site.register(Auto)
admin.site.register(Warehouse)
admin.site.register(Buyer)
admin.site.register(Condition)
admin.site.register(Airport)
admin.site.register(Airboard)
admin.site.register(Person)
admin.site.register(House)
admin.site.register(Super)
