print('#8.3')
def make_shirt(size, text):
    print(f'You choosen {size} size with text \"{text}\"')
size=str(input('Your size: '))
text=str(input('Your text: '))
make_shirt(size, text)
input('Press ENTER')

print('\n#8.4')
def make_shirt2(size, text):
    size2 = 'L'
    text2 = 'I love phyton'
    print(f'You choosen {size} size with text \"{text}\"')
print(f'{make_shirt2(size, text)} by default.\nChoose your size and text')
size=str(input('Your size: '))
text=str(input('Your text: '))
make_shirt2(size, text)
input('Press ENTER')

print('\n#8.5')
def describeCity (city, country):
    print(f'{city.title()} is in {country.title()}')
city = str(input('city: '))
country = str(input('country: '))
describeCity (city, country)
input('Press ENTER')

print('\n#8.6')
def cityCountry (cityy, countryy):
    print(f'{cityy.title()}, {countryy.title()}')
i=0
while i<4:
    cityy = str(input('city: '))
    countryy = str(input('country: '))
    cityCountry (cityy, countryy)
    i+=1
input('Press ENTER')

print('\n#8.7')
playlist = ''
def makeAlbum(music, autor):
    album = f'{music} - {autor}\n'
    return album
music = str(input('music: '))
autor = str(input('autor: '))
playlist=makeAlbum(music, autor)
print (playlist)
input('Press ENTER')
playlist = ''
def makeAlbum(music, autor):
    album = f'{music} - {autor}\n'
    return album
while True:
    music = str(input('music: '))
    autor = str(input('autor: '))
    if music == 'quit' or album == 'quit':
        break
    else:
        playlist=makeAlbum(music, autor)
print (playlist)
print('\n#8.8')
playlist = ''
def makeAlbum(music, autor):
    song = f'{music} - {autor}\n'
    return song
while True:
    music = str(input('music: '))
    autor = str(input('autor: '))
    if music == 'quit':
        break
    elif music == 'quit':
        break
    else:
        album=makeAlbum(music, autor)
        playlist+=album
print (playlist)
input('Press ENTER')
