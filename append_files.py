
appending_in_file = open("student.txt", "a")

print(appending_in_file.write("\nArun - 11803056"))

appending_in_file.close()


# \n না দিলে অন্য লাইনে যাবে না । সোজা একই লাইনে লেখা এড হয়ে যাবে।
# প্রতিবার রান করলে একবার করে এড হবে। 