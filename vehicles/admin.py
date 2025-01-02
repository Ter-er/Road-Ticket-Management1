from django.contrib import admin
from .models import Vehicle


class VehicleAdmin(admin.ModelAdmin):
    # Organizing fields into different sections in the admin form
    fieldsets = ()
    
    # Customizing the list view to make it more informative
    list_display = ('reg_no', 'owner', 'make', 'model', 'colour', 'year')
    list_filter = ('make', 'model', 'colour', 'year')  # Filter by make, model, colour, and year
    search_fields = ('reg_no', 'make', 'model', 'owner__username')  # Search by registration number, make, model, or owner's username
    
    # Ordering vehicles by registration number
    ordering = ('reg_no',)
    
    # Limit the number of vehicles displayed per page
    list_per_page = 20

admin.site.register(Vehicle, VehicleAdmin)

# Register your models here.

# admin.site.register(Vehicle)