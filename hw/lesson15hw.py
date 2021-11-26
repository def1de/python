name=str(input('Enter your First Name: '))
surname=str(input('Enter your Last Name: '))
n=f"{name.title()} {surname.title()}"
a=int(input('Enter your Age: '))
l=str(input('Enter your Location: '))
user_0 = {
    'name': n,
    'age': a,
    'location': l.title(),
}
print (f"=================user-info=================")
for i,j in user_0.items():
    print (f"\t{i}: {j}")
print (f"===========================================")