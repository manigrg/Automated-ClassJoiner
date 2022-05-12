#regex
# a followed by zero or more b.
# a followed by one or more b's.
# a followed by exactly 3 b's.
# a followed by 3 or more b's.
# sequence of lowercase joined with underscore.
# sequence of one uppercase followed by lowercase letter.
# starting with a followed by anything ending with b.
# match word at end of string.
#replace white space with__.



#1 import re
# text= str(input("enter the text match:"))
# pattern= '^a(b*)$'
#
# if re.search(pattern,text):
#     print("Matched")
# else:
#     print("Sorry, Unmatched")


#2. import re
# text=str(input("enter the text match:"))
# pattern = '^a(b+)$'
#
# if re.search(pattern,text):
#  print("Matched")
# else:
#  print("Unmatched")

#3. import re
# text=str(input("enter the text match:"))
# pattern = '^a(b{3})$'
# if re.search(pattern,text):
#   print("Matched")
# else:
#     print("Unmatched")


#4. import re
# text=str(input("enter the text match:"))
# pattern = '^a(b{3}|b+)$'
#
# if re.search(pattern,text):
#  print("Matched")
# else:
#  print("Unmatched")



#5. import re
# text=str(input("enter the text match:"))
# pattern = '[a-z]+_[a-z]+$'
#
# if re.search(pattern,text):
#  print("Matched")
# else:
#  print("Unmatched")

#6. import re
# text=str(input("enter the text match:"))
# pattern = '[A-Z]+_[a-z]+$'
#
# if re.search(pattern,text):
#  print("Matched")
# else:
#  print("Unmatched")



#7. import re
# text=str(input("enter the text match:"))
# pattern = '^a.*b$'
#
# if re.search(pattern,text):
#  print("Matched")
# else:
#  print("Unmatched")

#8. import re
# text=str(input("enter the text match:"))
# pattern = '^a.*b$'
#
# if re.search(pattern,text):
# print("Matched")
# else:
# print("Unmatched")

#9. import re
# text=str(input("enter the text match:"))
# pattern = '\w+\S*$'
#
# if re.search(pattern,text):
# print("Matched")
# else:
# print("Unmatched")


#10 text=str(input("enter the text match:"))
#
# text= text.replace(" ","_")
# print(text)







