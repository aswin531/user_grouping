# user/utils.py
import requests
from geopy.distance import geodesic


def fetch_json_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch JSON data")



def calculate_distance(coord1, coord2):
    # Function to calculate the distance between two coordinates using geodesic
    return geodesic(coord1, coord2).kilometers

def group_users(users):
    # Function to group users based on their coordinates within a certain distance
    # For example, group users within 1000 kilometers of each other
    grouped_users = []
    for user in users:
        user_coords = (user['address']['geo']['latitude'], user['address']['geo']['longitude'])
        added_to_group = False
        for group in grouped_users:
            if any(calculate_distance(user_coords, group_user['coords']) <= 1000 for group_user in group):
                group.append({'name': user['fullName'], 'coords': user_coords})
                added_to_group = True
                break
        if not added_to_group:
            grouped_users.append([{'name': user['fullName'], 'coords': user_coords}])
    return grouped_users
