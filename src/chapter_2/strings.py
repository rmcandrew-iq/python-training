#strings can be:
"My string"
'My string'
#and both are equivalent
#since both are, can do things like:
"My string has 'apos' in it"
'My string has "quotes" in it'
#also this but it's not discussed in the book:
'''My 
    string1
'''

# my new change

#accessing functions on strings
name = "Ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#not discussed in this chapter but also can do this:
print("ada lovelace".title())

#using fstrings with variables
first_name = "Ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}")
#also could assign the message to a variable 
message = f"Hello, {full_name.title()}"
print(message)

#not discussed in book but concatentation is usually like this:
full = first_name + " " + last_name

#using escaped characters
print('Python')
#tab
print('\tPython')
#new line
print('\nPython')

#stripping whitespace
string_to_strip = "   my test "
print(string_to_strip.strip()) #book shows rstrip() and lstrip(), as well.
#calling strip does not change the string, it just returns the stripped version, it has to be assigned to the variable to take effect
string_to_strip = string_to_strip.strip()

nostarch_url = "https://nostarch.com" 
simplified_url = nostarch_url.removeprefix('https://')
print(simplified_url)