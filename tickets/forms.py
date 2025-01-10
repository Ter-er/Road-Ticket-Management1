from django import forms
from .models import Ticket
from django.contrib.auth.models import User
from vehicles.models import Vehicle
from .models import Offence
from django.utils import timezone

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['motorist', 'official', 'vehicle', 'offence', 'is_paid']  # Only the editable fields

    # You may want to manually handle the issue_date and due_date (like in admin.py)
    issue_date = forms.DateTimeField(initial=timezone.now, widget=forms.HiddenInput(), required=False)
    due_date = forms.DateTimeField(initial=timezone.now() + timezone.timedelta(days=14), widget=forms.HiddenInput(), required=False)
    
    # You can also handle the ticket_no as a hidden field to make it non-editable
    ticket_no = forms.CharField(widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the logged-in user from the view
        super().__init__(*args, **kwargs)
        
        if user:
            # Set the initial value of the 'official' field to the logged-in user
            self.fields['official'].initial = user

    # You can also add custom validation if required.
    def clean_motorist(self):
        motorist = self.cleaned_data.get('motorist')
        # Any custom validation for motorist if necessary
        return motorist

    def clean_offence(self):
        offence = self.cleaned_data.get('offence')
        # Any custom validation for offence if necessary
        return offence

    def save(self, commit=True):
        # If no ticket_no is provided, automatically generate one
        if not self.instance.ticket_no:
            self.instance.ticket_no = self.instance.generate_ticket_no()
        
        # Set issue_date and due_date if not provided (same behavior as in admin.py)
        if not self.instance.issue_date:
            self.instance.issue_date = timezone.now()
        if not self.instance.due_date:
            self.instance.due_date = timezone.now() + timezone.timedelta(days=14)

        return super().save(commit=commit)