#importar intruccion directamente del management
from django.core.management.base import BaseCommand
#from django.contrib.auth.models import User
from academics.models import User
import json



class Command(BaseCommand):
    #configurar ayuda informacion 
    help = 'Make a database backuop in JSON format'
    def handle(self, *args, **options ):
        #GET data from User model
        users = User.objects.all()

        #convert data to dictionaries
        data = [
            {'id': user.id,
             'email': user.email,
             'password':user.password,
             'status': user.status
            }
            for user in users
            
        ]
        # Save to JSON format 
        with open('backup_bd.json','w') as file:
            json.dump(data, file, indent=4)
