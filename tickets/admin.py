from django.contrib import admin
from .models import Ticket, Offence

class TicketAdmin(admin.ModelAdmin):
    fieldsets = ()


    list_display = ('ticket_no', 'motorist', 'official', 'offence', 'issue_date','due_date', 'is_paid')
    list_filter = ('ticket_no', 'issue_date')
    search_fields = ('ticket_no', 'motorist__username', 'official__username', 'offence__name')
    ordering = ('-issue_date',)
    list_per_page = 20


    readonly_fields = ('ticket_no', 'issue_date', 'due_date')  # Make 'ticket_no', 'issue_date', 'due_date' read-only


class OffenceAdmin(admin.ModelAdmin):
    list_display = ('ticket_infringement', 'code', 'points', 'penalty', 'category')
    search_fields = ('ticket_infringement', 'code', 'category')
    ordering = ('ticket_infringement',)
    list_per_page = 20


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Offence, OffenceAdmin)