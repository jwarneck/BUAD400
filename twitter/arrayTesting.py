'''i = 0
list1 = {"tom", "jerry", "robin"}
list2 = {1, 2, 3, 4}
list3 = {"bert", "ernie", "bruce"}
list4 = {"clark", "jones", "homie"}
list5 = {"monster", "skoal", "seiko"}
list6 = {"XD", "jax", "Thelma"}
list7 = {"Gerber", "Glock", "ACP"}
array = [list1, list2, list3, list4, list5, list6, list7]
print array'''

phone_number = "3439907"
length = len(phone_number)
numberArray = []


for x in range (0, length - 1):
	r = 0
	print("Number =")
	number = phone_number[r:]
	r = r + 1
	print("j + 1")
	print("Appending to array")
	numberArray.append([number])
	print("J = ", r)
	print(numberArray)