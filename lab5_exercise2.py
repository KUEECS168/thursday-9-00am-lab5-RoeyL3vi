'''
Author: Roey Levi
KUID: 3200438
Date: 3/5/2026
Lab: lab05
Last modified: 3/5/2026
Purpose: be able to create and manipulate lists
'''
mission_status = 'n'
planets_visited = []

while mission_status.lower() == 'n':
    planets_visited.append(input('Enter planet name: ').lower())
    mission_status = input("Is the mission over? (y/n): ")


i = planets_visited.index(input('Which planet do you want the neighbors for?: ').lower())
print(f'Planets neighboring {planets_visited[i]}:')
if i>0:
    print(f'\t{planets_visited[i-1]}')
if i+1 < len(planets_visited):
    print(f'\t{planets_visited[i+1]}')
print('Program ending...')