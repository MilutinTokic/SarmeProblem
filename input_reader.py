import math

def read_input(file_path):

  circles = []
  radius = 0

  with open(file_path) as file:
    lines = file.readlines()

  radius = int(lines[0])  

  for line in lines[1:]:
    x, y = line.split()
    x = int(x) 
    y = int(y)
    
    circles.append([x, y])

  return circles, radius



def calculate_distance(point1, point2):

  x1, y1 = point1
  x2, y2 = point2

  distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

  return distance

def find_closest(circle, circles):

  closest_distance = float('inf')
  closest_circle = None

  for other in circles:
    if other != circle:
      distance = calculate_distance(circle, other)
      
      if distance < closest_distance:
        closest_distance = distance 
        closest_circle = other
        
  return closest_circle


