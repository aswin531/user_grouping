# user/views.py
from django.shortcuts import render
from django.http import HttpResponse
from geopy.distance import geodesic

# Your view functions here


from .utils import fetch_json_data, calculate_distance, group_users

def display_grouped_users(request):
    json_url="https://ignite.zook.top/data.json"
    try:
        json_data = fetch_json_data(json_url)
        grouped_users = group_users(json_data)
        return render(request, 'grouped_users.html', {'groups': grouped_users})
    except  Exception as e:
        return render(request, 'error.html', {'error_message': str(e)})    
