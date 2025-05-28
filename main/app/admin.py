from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import Car, CarHistory, Client
from app.views import send_email

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

@admin.register(CarHistory)
class CarHistoryAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if change:
            send_email("edit_status.html", {"order": obj}, "Изменен статус ремонта", obj.car.user)
            
admin.site.register(Client, CustomUserAdmin)
admin.site.register(Car)
# admin.site.register(CarHistory)