items_1 = {'color' : 'red', 'speed' : 'medium', 'coins' : 15};
items_2 = {'color' : 'blue', 'speed' : 'fast', 'coins' : 25};
items_3 = {'color' : 'white', 'speed' : 'fast', 'coins' : 50};
gamers = [items_1, items_2, items_3];
for i in gamers:
    print(i);

gamers = [];
for i in range(0, 150):
    a = {'color' : 'red', 'speed' : 'medium', 'coins' : 15};
    gamers.append(a);
for a in gamers[4:9]:
    if a['color']=='red':
        a['color']='blue';
        a['speed']='fast';
        a['coins']=35;
    if a['color']=='blue':
        a['color']='white';
        a['speed']='super-fast';
        a['coins']=50;
for b in gamers:
    print(b);
print("--------------------------------------------------------");
print(f"Всего {len(gamers)} игроков");

dict={
    'Illia':['task-1','task-2'],
    'Alexey':['task-1','task-2','task-3'],
    'Yaroslave':['task-1'],
    'Rom4ik':['task-1','task-2'],
    'Artemik':['task-1','task-2','task-3','task-4']
    }
for i,b in dict.items():
    print("----------------------------------------------------")
    print(f"{i} решил такие задачи:")
    for a in b:
        print(f"{a}")

dict={
    'user_0':{
        'name':'Alexey',
        'surname':'Kosenko',
        'housenumber':14.5,
        'yourage':14
        },
    'user_1'{
        'name':'Illia',
        'surname':'Katerinych',
        'housenumber':13.7,
        'yourage':15
        }
    }