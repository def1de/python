dimensions = (200, 50)

print(dimensions[0]) 
print(dimensions[1])


dimensions = (200, 50) 
for dimension in dimensions:
    print(dimension)


dimensions = (200, 50) 
print("Original dimensions:") 
for dimension in dimensions: 
    print(dimension) 
dimensions = (400, 100) 
print("\nModified dimensions:") 
for dimension in dimensions: 
    print(dimension)


alien_0 = {'color': 'green', 'points': 5} 

item_0 = alien_0['points']
print(f"Ты виграл на {item_0}-м уровне")


alien_0 = {'color': 'green', 'points': 5} 

alien_0['x_position'] = 0 
alien_0['y_position'] = 25 
print(alien_0)

user_name = {}

user_name["user_1"] = "Den"
user_name["user_2"] = "Illysha"
print(user_name)
print(user_name["user_2"])


alien_0 = {'color': 'green'} 

print(f"The alien is {alien_0['color']}.") 
alien_0['color'] = 'yellow' 
print(f"The alien is now {alien_0['color']}.")
print(alien_0)


alien_0 = {'color': 'green', 'points': 5} 
print(alien_0) 

del alien_0['points'] 
print(alien_0)


alien_0 = {'color': 'green', 'speed': 'slow'} 
point_value = alien_0.get('points', 'No point value assigned.') 
print(point_value)


user_0 = { 
  'username': 'efermi', 
  'first': 'enrico', 
  'last': 'fermi', 
  }
for key, value in user_0.items(): 
    print(f"\nKey: {key}") 
    print(f"Value: {value}")


favorite_languages = { 
  'user_0': 'python', 
  'user_1': ‘js', 
  'user_2': ‘php', 
  'user_3': 'python', 
  }
for name, language in favorite_languages.items(): 
  print(f"{name.title()}'s favorite language is {language.title()}.")


favorite_languages = { 
  'user_0': 'python', 
  'user_1': ‘js', 
  'user_2': ‘php', 
  'user_3': 'python', 
  }
for name in favorite_languages.keys(): 
  print(name.title())


favorite_languages = { 
'user_0': 'python', 
'user_1': 'js', 
'user_2': 'php', 
'user_3': 'python', 
}


 
for language in favorite_languages.values(): 
  print(language.title())