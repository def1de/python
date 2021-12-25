def loading_start():
    i = "Loading started..."
    yield i

def loading_main():
    for i in range (0, 101, 5):
        i2 = f"{i}%"
        yield i2
def loading_end():
    i = "Loading ended."
    yield i

t = loading_start()
for i in t:
    print(i)
t = loading_main()
for i in t:
    print(i)
t = loading_end()
for i in t:
    print(i)

