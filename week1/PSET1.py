'''
PSET1
'''

# ==============================================================================

# 1.1

# Write a program that counts up the number of vowels contained in the string

numVowels = 0

for letter in s:
	if letter in ('a','e','i','o','u'):
		numVowels += 1

print(numVowels)


# ======================================================================
# 1.2

# Write a program that prints the number of times the string 'bob' occurs

i1 = 0
count = 0
for letter in range(len(s)-2):
    i2 = i1 + 1
    i3 = i1+2
    if s[i1] == 'b' and s[i2] == 'o' and s[i3] == 'b':
        count += 1
    i1 += 1
    
print("Number of times bob occurs is: " + ' ' + str(count))


# =====================================================================
# 1.3

# s is a predefined variable set to a string value

s = 'efghksierbsndjforthefghijklmnopqrstu'

# first we can define two substrings to be evaluated

sstest = ''
ssfinal = ''
# these two substrings will be evaluated in which one is the longest

# it is gonna work like the golden section algorithm 

#
for i in range(len(s)):
 if (s[i] >= s[i-1]):
  sstest += s[i]
 else:
  sstest = s[i]
 if len(sstest) > len(ssfinal):
  ssfinal = sstest
print("Longest substring in alphabetical order is: " + ssfinal)

#  ==============================================

# another solution to pset1.3

s = 'efghksierbsndjforthefghijklmnopqrstu'


string = ""

count = 0

longestCount = 0

longestString = ""

for i in range(len(s)):

    # if i at the first character, automatically add the character to string

    if i == 0:

        string += s[i]

        count += 1

    # if the current character is more than or equals to (in alphabeticall order) the previous number

    elif s[i] >= s[i - 1]:

        string += s[i]

        count += 1

    # if the current character is less than (in alphabeticall order) the previous number   

    elif s[i] < s[i - 1]:

        if count > longestCount:

            longestCount = count

            longestString = string

        # reset count, then count is incremented by one for current character.

        count = 0

        count = 1

        # reset string, then current character is added to string.

        string = ""

        string += s[i]

    # if i is at the last character, and the current character is continuation of a series of alphabets in ascending order, 

    # it has not been compared with longestCount yet.

    if i == len(s) - 1:

        if count > 1:

            if count > longestCount:

                longestCount = count

                longestString = string

print("Longest substring in alphabetical order is: " + longestString)
        
    
