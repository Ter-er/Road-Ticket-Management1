from django.db import models
from django.contrib.auth.models import User
from vehicles.models import Vehicle
from django.utils import timezone
import random
from django.core.exceptions import ValidationError

class Offence(models.Model):
    ticket_infringement = models.CharField(max_length=255)
    code = models.CharField(max_length=4)
    points = models.IntegerField()
    penalty = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ticket_infringement}"
    

class Ticket(models.Model):
    motorist = models.ForeignKey(User, related_name = "tickets_received", on_delete=models.CASCADE)
    official = models.ForeignKey(User, related_name="tickets_issued", on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, related_name="tickets", on_delete=models.CASCADE)
    offence = models.ForeignKey(Offence,related_name="tickets", on_delete=models.CASCADE)
    ticket_no = models.CharField(max_length=1000, unique=True, blank=True)    
    issue_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=14))
    is_paid = models.BooleanField(default=False)


    def generate_ticket_no(self):
        
        current_year = timezone.now().year
        random_number = random.randint(100000, 999999)  # Random number for uniqueness
        return f"{current_year}-{random_number}"

    def save(self, *args, **kwargs):

        if not self.ticket_no:
            self.ticket_no = self.generate_ticket_no()
        
        # Ensure the ticket number is unique before saving
        self.full_clean()  # This validates the model, including the uniqueness of ticket_number
        
        super().save(*args, **kwargs)  # Call the parent class save method


    def __str__(self):
        
        return f"Ticket {self.ticket_no} issued to {self.motorist.username} by {self.official.username}"

    def clean(self):
        # Ensure ticket number is unique.
        if Ticket.objects.filter(ticket_no=self.ticket_no).exists():
            raise ValidationError(f"Ticket number {self.ticket_no} already exists. Please try again.")