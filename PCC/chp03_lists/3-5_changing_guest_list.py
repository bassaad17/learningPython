guest_list = ['Jennifer', 'Sofia', 'Eric', 'Carter']
print("This is a list of guests attending the event:")
print("\t- " + guest_list[0])
print("\t- " + guest_list[1])
print("\t- " + guest_list[2])
print("\t- " + guest_list[3])

print("Unfortunately, " + guest_list[2].title() + " won't be able to attend.")
print("This is a revised list of guests attending the event:")
guest_list[2] = 'John'
print("\t- " + guest_list[0])
print("\t- " + guest_list[1])
print("\t- " + guest_list[2])
print("\t- " + guest_list[3])