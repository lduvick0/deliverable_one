import string

thisisanint=20
thisisaString="hello world"
this_string="Potato"
print(this_string)
boolean=True
thisfloat=3.14 * 3
this_float= 3.14 ** 3
this_modulator= 11%3
this_floor= 23 // 5

#response=input("Please input a number: ")
#print(response)

#print(type(response))
#response=int(response)
#int_to_string=str(thisisanint)
#print(type(response))

new_string= "hi, i am = to" + " test python"
print(new_string)
print(new_string.upper())
print(new_string.lower())
print(new_string.capitalize())

string_with_spaces='\t     testing \t'
print(string_with_spaces)
string_with_spaces=string_with_spaces.strip()
print(string_with_spaces)

string_to_search = "   Grand Circus is great, im learning the Snake"
return_from_find = string_to_search.find("Grand")
print(return_from_find)

aList=[1,2,3,4,5,6,7,8,9]
print(aList)

for aword in aList:
    print(aword)

atuple=(1,2,3,4,5,6,7,8,9)
for anumber in atuple:
    print(anumber)
for aletter in string_to_search:
    print(aletter)

num=10
print(f'here is the value for {aList}')


astring_with_substitution="my favorite numbers are {0} and {1} and {2}".format(23,42,101)
print(astring_with_substitution)

aname="fred"


print(f'{34*3} and {34/2}or how about this {aname}')

astring_with_substitution[3]="g"

astring_with_substitution = astring_with_substitution.replace("f", "g")
print(astring_with_substitution)

print(len(astring_with_substitution))
lastletter =astring_with_substitution[len(astring_with_substitution)-1]
print(lastletter)
print(astring_with_substitution[-1])
print(astring_with_substitution[-2])
print(astring_with_substitution[-3])

sub_string = astring_with_substitution[3:11]
print(sub_string)

sub_string2 = astring_with_substitution[-3:-1]
print(sub_string2)

repeating_string =10 * "abc"
divider = 20 * "="
print("Menu")
print(divider)
print(f'{sub_string2}')

large_test = """hello everyone 
this is a paragraph
we write it like this
"""

print(large_test)

tab_string= 'hello,\teveryone'
print(tab_string)
newline='hello,\n everyone'
print(newline)
print(r'whoami\t\ntom')
print(f'hello,\n everyone')