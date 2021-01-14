string_list = ['blubber','nitwit','3','twit','sleeve','1','4','moral','-14','clue','access','2.72','9.99','generation','525600','valentine','1984','potion','0','7','-13','relief','19','19','wheel','stress','hammer','1729','shark']

#This code checks the first digit of the string to see if it is a negative sign, a decimal point, or a number.
#If so, we assume that string is a number. Otherwise, we call it a string.
def is_num(something):
  number_chars = ['-','.','0','1','2','3','4','5','6','7','8','9']
#look at the first value of the string
  start = something[0]
  if start in number_chars:
    return True
  else:
    return False

#This version of the function checks EACH value in the string to see if it belongs to the list of symbols allowed in a number.
def is_num2(something):
  number_chars = ['-','.','0','1','2','3','4','5','6','7','8','9']
  #This is an example of something called list comprehension
  are_they_numbers = [vals in number_chars for vals in something]
  if all(are_they_numbers):
    return True
  else:
    return False

#Here is an example of how we can use list comprehension.
small_list = ['hell0','apples','bananas','1234']

are_they_numbers = []
for word in small_list:
  are_they_numbers.append(is_num(word))

#This is called list comprehension 
#and does the same thing as lines 27-29
are_they_numbers2 = [is_num(word) for word in small_list]

#Notice we get the same output.
print(are_they_numbers)
print(are_they_numbers2)

#This method for separating words and numbers works,
#but is not the way Python would do it.
word_list = []
num_list = []
for word in string_list:
  if is_num(word):
    num_list.append(word)
  else:
    word_list.append(word)

print(word_list)
print(num_list)

#This is the way to accomplish the same tasks as lines 41-47 using conditional list comprehension.
num_list2 = [word for word in string_list if is_num(word)== True]
word_list2 = [word for word in string_list if is_num(word) == False]
print(num_list2)
print(word_list2)