lucky_numbers = [3,4,7,34,77,38,97]
friends = ["Dhrubo" , "Amdadul" , "Dhruboish" , "Kaosar" , "Tasnim" , "Dhruboish"]


print(lucky_numbers)
print(friends)

# Adding lucky_numbers after all elements of friends 
friends.extend(lucky_numbers)
print(friends)


# append() will add element at last of the list ; but it will add only 1 element
friends.append("Momin")
print(friends)


# You can insert in any index number position by using .insert function 
friends.insert(2,"Chagol Beda")
# That is I want to add "Chagol Beda" in index 2 
print(friends)



# Remove element by useing function .remove(str)
friends.remove("Momin")
print(friends)
# remove() takes exactly one argument

# Remove only last element of the list using .pop() function 
friends.pop()
print(friends)


# Know how many times an element have in a list 
print(friends.count("Dhruboish"))

# .reverse() will reverse the list 
friends.reverse()
print(friends)


# We can copy a list in another list using .copy function
new_friends = friends.copy()
print(new_friends)

# We can clear all elements from a list using .clear()
friends.clear()
print(friends)
# It will give an empty list 




