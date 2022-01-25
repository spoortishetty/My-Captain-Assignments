text="you cannot end a sentence with because because because is a conjuction."
print(text)

#Converts the first character to upper case
print(text.capitalize())

txt="YOU CANNOT END A SENTENCE WITH BECAUSE BECAUSE BECAUSE IS A CONJUNCTION."
#Converts string into lower case
print(txt.casefold())

txt="BECAUSE"
#Returns a centered string
print(txt.center(70))

#Returns the number of times a specified value occurs in a string
print(text.count("because"))

txt="Чѳц cаппѳт ёпд а $ёптёпcё щїтн бёcац$ё бёcац$ё бёcац$ё ї$ а cѳпjцcтїѳп."
#Returns an encoded version of the string
print(txt.encode())
print(text.encode())

#Returns true if the string ends with the specified value
x = text.endswith("conjuction")
y = text.endswith(".")
z = text.endswith("conjuction.")
print(x,y,z)

#Sets the tab size of the string
txt = "B\te\tc\ta\tu\ts\te"
print(txt)
print(txt.expandtabs(5))

#Searches the string for a specified value and returns the position of where it was found
print(text.find("sentence"))
print(text.find(" a ",16, 60))
 
txt="{You} cannot {end} a sentence with because because because is a conjuction."
#Formats specified values in a string
print(txt.format(You="We",end="terminate"))

class Default(dict):
    def __missing__(self, key):
        return key
#Formats specified values in a string mappings are used directly and not copied to a dictionary 
print(txt.format_map(Default(You='I')))
#print(txt.format(end="I"))  ------> will give error because it’s copying the provided mappings to a new dict object.

#Searches the string for a specified value and returns the position of where it was found
print(text.index('conjuction'))
print(text.index('because',45,60))

#Returns True if all characters in the string are alphanumeric
print(text.isalnum())
#as space does not come under alphanumeric...so, value is false for the above one
txt="Because32222224"
print(txt.isalnum())
print()

#Returns True if all characters in the string are in the alphabet
txt="Because32222224"
print(txt.isalpha())
txt="Because"
print(txt.isalpha())
print()

#Returns True if all characters in the string are decimals
x = "\u0030" #unicode for 0
y = "\u0047" #unicode for G
print(x.isdecimal())
print(y.isdecimal())
print()

#Returns True if all characters in the string are digits
txt = "453235235"
print(txt.isdigit())
print(text.isdigit())
print()

#Returns True if the string is an identifier
print("Because_Conjuction".isidentifier())
print("__Because7889".isidentifier())
print("Because@conjuction".isidentifier())
print("Because conjuction".isidentifier())
print()

#Returns True if all characters in the string are lower case
print(text.islower())
print("BeCaUsE".islower())
print()

#Returns True if all characters in the string are numeric
print("4331".isnumeric())
print("¾".isnumeric())
print("²".isnumeric())
print("9.5".isnumeric())
print("-4".isnumeric())
print()

#Returns True if all characters in the string are printable
print("Because is a conjuction".isprintable())
print("Because is a\nconjuction".isprintable())
print()

#Returns True if all characters in the string are whitespaces
print("     ".isspace())
print(text.isspace())
print()

#Returns True if the string follows the rules of a title
print("Because Is Conjuction".istitle())
print("Error 404!".istitle())
print("Because Is CONJUCTION".istitle())
print("Because is Conjuction".istitle())
print()

#Returns True if all characters in the string are upper case
print("BECAUSE IS A CONJUCTION".isupper())
print(text.isupper())
print()

Adrenaline=("Flight","Fight","Fear")
#Joins the elements of an iterable to the end of the string
print(" & ".join(Adrenaline))

#Returns a left justified version of the string
print("Because".ljust(20, "~"), "is a Conjuction.")

#Converts a string into lower case
print("BECaUsE iS a cONJUCTION".lower())

#Returns a left trim version of the string
print("I know that","         'because'        ".lstrip(),"is a conjuction")

#Returns a translation table to be used in translations
txt = "Because is a Donjuction!"
print(txt.translate(txt.maketrans("D","C")))

#Returns a tuple where the string is parted into three parts
print(text.partition("with"))

#Returns a string where a specified value is replaced with a specified value
print(text.replace("end","conclude"))

#Searches the string for a specified value and returns the last position of where it was found
print(text.rfind("because"))
print(text.rfind("u"))

#Searches the string for a specified value and returns the last position of where it was found
print(text.rindex("with"))

#Returns a right justified version of the string
print("Because".rjust(30, "✿"))

#Returns a tuple where the string is parted into three parts
print(text.rpartition("with"))

#Splits the string at the specified separator, and returns a list
print("flight,fight,fear".rsplit(",",1))

#Returns a right trim version of the string
print("I know that","         'because'        ".rstrip(),"is a conjuction")

#Splits the string at the specified separator, and returns a list
print("Because is a@conjuction".split("@"))

#Splits the string at line breaks and returns a list
txt="you cannot end a sentence with because\nbecause is a conjuction."
print(txt.splitlines())

#Returns true if the string starts with the specified value
print(text.startswith("you"))

#Returns a trimmed version of the string
print("I know that","         'because'        ".strip(),"is a conjuction")

#Swaps cases, lower case becomes upper case and vice versa
print("BECaUsE iS a cONJUCTION".swapcase())

#Converts the first character of each word to upper case
print(text.title())

#Returns a translated string
mydict = {68:  67}
print("Because is a Donjuction!".translate(mydict))

#Converts a string into upper case
print(text.upper())

#Fills the string with a specified number of 0 values at the beginning
print("Because".zfill(20))




#∘˚˳°∘° ҉✿∘˚˳°∘˚˳°∘° ҉✿∘˚˳°∘˚˳°∘° ҉✿∘˚˳°∘˚˳°∘° ҉✿∘˚˳°∘˚˳°∘° ҉✿∘˚˳°∘˚˳°∘° ҉✿∘˚˳°∘˚˳°∘° ҉✿∘˚˳°∘˚˳°∘° ҉✿∘˚˳°∘˚˳°∘° ҉✿∘˚˳°







