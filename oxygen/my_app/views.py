# my_app/views.py
from django.shortcuts import render
from firebase_admin import db

def fetch_data(request):
    ref = db.reference('/')  # Reference to the root of your Firebase database
    data = ref.get()  # Fetch data from Firebase
    
    return render(request, 'data_display.html', {'data': data})
