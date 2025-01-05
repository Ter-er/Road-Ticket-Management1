from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TicketForm
from .models import Ticket

def get_user_tickets(User):
    return Ticket.objects.select_related('offence').filter(user=User)



def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Ticket created successfully!')
            return HttpResponseRedirect(reverse('dashboard-official'))

        else:
            messages.error(request, 'Ticket creation failed!')


    else:
        form = TicketForm()

    return render(request, 'create-ticket.html', {'form': form})
    