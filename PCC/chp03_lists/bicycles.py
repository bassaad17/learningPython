#first item of list starts with an index of 0

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[2])
print(bicycles[-1]) #access the last element in the list

msg = "My first bicycle was a " + bicycles[0].title() + "."
print(msg)