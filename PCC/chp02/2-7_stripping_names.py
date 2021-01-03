firstName = "Jennifer  "
middleName = "  Lee  "
lastName = "  Assaad"
fullName = firstName + " " + middleName + " " + lastName
print("Unedited:",fullName)

firstName = firstName.rstrip()
middleName = middleName.strip()
lastName = lastName.lstrip()
fullName = firstName + " " + middleName + " " + lastName
print("Edited:",fullName)
