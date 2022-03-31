#Material from: https://books.trinket.io/pfe/04-functions.html
import random
import math


#The max and min functions give us the largest and smallest values in a list, respectively:
print("Max value in a list \"Hello World is\": " + str(max('Hello world')))
print("Min value in a list \"Hello World is\": " + str(min('Hello world')))

#Another very common built-in function is the len function which tells us how many items are in its argument. If the argument to len is a string, it returns the number of characters in the string.
print("Length of Hello world is: " + str(len('Hello world')))

#The int function takes any value and converts it to an integer, if it can, or complains otherwise:
print(int('32'))

try:
    print(int('Hello world'))
except:
    print("Cant convert to int, value in not number")

# The function random returns a random float between 0.0 and 1.0 (including 0.0 but not 1.0). Each time you call random, you get the next number in a long series. To see a sample, run this loop:

for i in range(10):
    x = random.random()
    print(str(i) + " randon value with function random: "+str(x))

#The random function is only one of many functions that handle random numbers. The function randint takes the parameters low and high, and returns an integer between low and high (including both).
x = random.randint(1,100)
print("Randon value with function randint: "+str(x))

#To choose an element from a sequence at random, you can use choice:
choise = "Hello world, Serhii!!!"
print("Random value chosen from list \"Hello world, Serhii!!!\" is: "+random.choice(choise))

#Python has a math module that provides most of the familiar mathematical functions. Before we can use the module, we have to import it:
print(math)
signal_power = input("Provide signal power: ")
noise_power = input("Provide signal power: ")
try:
    ratio = float(signal_power)/float(noise_power)
    decibels = 10 * math.log10(ratio)
except:
    print("Provided numbers in not a numbers")
print("Ratio power is: "+str(ratio)+". Decibel is: "+str(decibels))

try:
    sqrt = float(input("Provide value to get sqrt: "))
except:
    print("Provided number in not a numbers")
print("Sqrt from "+str(sqrt)+" is: "+str(math.sqrt(sqrt)))

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

print_lyrics()

print()



def repeat_lyrycs():
    print_lyrics()
    print_lyrics()

repeat_lyrycs()

def print_twice(word_to_print):
    print(word_to_print)
    print(word_to_print)

print_twice(input("Print something, we will repeat it tiwce it: ")*4)
