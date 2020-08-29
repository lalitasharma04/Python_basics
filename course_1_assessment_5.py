# Write a program that extracts the last three items in the list sports and assigns it to the variable last. Make sure to write
#  your code so that it works no matter how many items are in the list.
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
last=sports[:-4:-1][::-1]


# Write code that combines the following variables so that the sentence “You are doing a great job, keep it up!” is assigned to the
#  variable message. Do not edit the values assigned to by, az, io, or qy.
by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"
message=by+' '+az+io+', '+qy

# **************************************************************************************************************************************

                    # Lists and for loops
fruits = ["apple", "orange", "banana", "cherry"]
for afruit in fruits:     # by item
    print(afruit)


print("This will execute first")
for _ in range(3):
    print("This line will execute three times")
    print("This line will also execute three times")

print("Now we are outside of the for loop!")

#******************************************************************************************************************************

                    # The Accumulator Pattern
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
accum = 0
for w in nums:
    accum = accum + w
print(accum)

# --------------------------------------------------------------------------------------------------------------------------------

accum = 0
for w in range(11):
    accum = accum + w
print(accum)
# or, if you use two inputs for the range function
sec_accum = 0
for w in range(1,11):
    sec_accum = sec_accum + w
print(sec_accum)

# ---------------------------------------------------------------------------------------------------------------------------------
# Write code to create a list of integers from 0 through 52 and assign that list to the variable numbers. You should use a special 
# Python function – do not type out the whole list yourself. HINT: You can do this in one line of code!
numbers=list(range(0,53))

# ----------------------------------------------------------------------------------------------------------------------------------

# Count the number of characters in string str1. Do not use len(). Save the number in variable numbs.
str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."
numbs=0
for char in str1:
    numbs+=1
# ----------------------------------------------------------------------------------------------------------------------------------

# Create a list of numbers 0 through 40 and assign this list to the variable numbers. Then, accumulate the 
# total of the list’s values and assign that sum to the variable sum1.
numbers=list(range(0,41))
sum1=0
for num in numbers:
    sum1+=num

# -----------------------------------------------------------------------------------------------------------------------------------

