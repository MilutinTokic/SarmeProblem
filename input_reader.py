import math

def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
        # Ovdje dodajte kod za obradu ulaznih podataka
    return processed_data

def calculate_distance(point1, point2):
   x1, y1 = point1
   x2, y2 = point2
   distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
   return distance
