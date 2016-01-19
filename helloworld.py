# replace the contents of this comment with your full name

# write a program that:
# 1. greets the user in English
# 2. asks the user to choose from 1 of 3 spoken languages (pick your favorite languages!) 
# 3. displays the greeting in the chosen language
# 4. exits

# make sure that your code contains comments explaining your logic!

# Nicholas Ivey 1/19/2016

print('Hello World') # print hello
print("Choose a language and I'll greet you in that language!") #prompt for lang input
print('1. Spanish')
print('2. Italian')
print('3. French')

try:
    num = int(raw_input())      # ask for input and store it as variable num
except ValueError:
    print('Invalid Entry')      # if 1,2,3 is not entered in print invalid

if (num == 1):                  # if 1 entered reply in spanish
        print('Hola')
if (num == 2):                  # if 2 entered reply in italian
        print('Ciao')
if (num == 3):                  # if 3 entered reply in french
        print('Salut')

exit()


