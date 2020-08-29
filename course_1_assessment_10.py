

# 1.For each word in the list verbs, add an -ing ending. Save this new list in a new list, ing.
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
ing=[]
for word in verbs:
    ing.append(word+"ing")

# **********************************************************************************************************************************

# 2.Given the list of numbers, numbs, create a new list of those same numbers increased by 5. Save this new list to the variable newlist.
numbs = [5, 10, 15, 20, 25]
newlist=[]
for num in numbs:
    newlist.append(num+5)

# **********************************************************************************************************************************

# 3.Challenge Now do the same as in the previous problem, but do not create a new list. Overwrite the list numbs so that each of the
#  original numbers are increased by 5.
numbs = [5, 10, 15, 20, 25]
for index in range(len(numbs)):
    numbs[index]=numbs[index]+5
print(numbs)

# **********************************************************************************************************************************

#4.For each number in lst_nums, multiply that number by 2 and append it to a new list called larger_nums.
lst_nums = [4, 29, 5.3, 10, 2, 1817, 1967, 9, 31.32]
larger_nums=[]
for num in lst_nums:
    larger_nums.append(num*2)



                                # The Accumulator Pattern with Strings
# 1.For each character in the string already saved in the variable str1, add each character to a list called chars.
str1 = "I love python"
# HINT: what's the accumulator? That should go here.
chars=[]
for char in str1:
    chars.append(char)

 # **********************************************************************************************************************************

# 2.Assign an empty string to the variable output. Using the range function, write code to make it so that the 
# variable output has 35 a s inside it (like "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"). Hint: use the accumulation pattern!
output=""
for i in range(35):
    output+="a"

# **********************************************************************************************************************************

                # GRADED ASSESSMENT 10
# 1.Currently there is a string called str1. Write code to create a list called chars which should contain the characters from str1.
#  Each character in str1 should be its own element in the list chars
str1 = "I love python"
# HINT: what's the accumulator? That should go here.
chars=[]
for char in str1:
    chars.append(char)

# **********************************************************************************************************************************


                         # GRADED ASSESSMENT 11
#1.For each character in the string saved in ael, append that character to a list that should be saved in a variable app.
ael = "python!"
app=[]
for char in ael:
    app.append(char)

# **********************************************************************************************************************************
#2For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense). Save these past tense words to
# a list called past_wrds.
wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds=[]
for word in wrds:
    past_wrds.append(word+'ed')



