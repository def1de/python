def gen(lang):
    for i in lang:
        yield i

lang = ["Python", "C++", "C#"]
t = gen(lang)
for i in t:
    print(i)
