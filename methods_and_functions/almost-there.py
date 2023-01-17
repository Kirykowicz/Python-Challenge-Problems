def almost_there(n):
   return abs(100 - n) <= 10 or abs(200 - n) <= 10
        

print(almost_there(190))

def trip_planner(first_destination, second_destination, final_destination = 'Codecademy HQ'):
  print('Here is what your trip will look like!')
  print(f'First we will stop in {first_destination}, then {second_destination}, and lastly {final_destination}')

trip_planner('France', 'Germany', 'Denmark')