from django.contrib import admin
from .models import Log, Vehicle


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ['payee', 
                    # 'price_with_unit', 
                    # 'quantity_with_unit', 
                    'fuel_type', 
                    'odo', 
                    'location',
                    'created_at']

    # @admin.display(description='Price')
    # def price_with_unit(self, obj: Log):
    #     return f"Rs {obj.price}"


    # @admin.display(description="Quantity")
    # def quantity_with_unit(self, obj: Log):
    #     return f"{obj.quantity} {obj.unit()}"

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    pass