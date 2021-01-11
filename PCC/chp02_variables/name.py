# to add comments, use the hashtag # symbol
name = "ada lovelace"
# making use of methods to print name in various formats
print(name.title())
print(name.upper())
print(name.lower())

# concatenation of strings with plus + symbol
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")

msg = "Hello, " + full_name.title() + "!!"
print(msg)

# to add tab to text use \t
# to add newline to text use \n 
print("Languages:\n\tPython\n\tC\n\tJavascript")

# stripping whitespace, right, left, and both sides
fav_language = "python  "
print(fav_language)
fav_language = fav_language.rstrip()
print(fav_language)

fav_language = "  python"
print(fav_language)
fav_language = fav_language.lstrip()
print(fav_language)

fav_language = "  python  "
print(fav_language)
fav_language = fav_language.strip()
print(fav_language)