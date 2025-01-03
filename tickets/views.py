from django.shortcuts import render
from .models import Ticket

def get_user_tickets(User):
    return Ticket.objects.select_related('offence').filter(user=User)
