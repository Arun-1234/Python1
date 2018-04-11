print (["Movies", "Games", "Python"])
print ("I like " +["Movies", "Games", "Python"][0])
print ("I like " +["Movies", "Games", "Python"][1])
print ("I like " +["Movies", "Games", "Python"][2])
print ("I like " +["Movies", "16", "Python"][1])
print({"Name":"Nick", "Age":"27", "Hobby":"Code"})
print({"Name":"Nick", "Age":"27", "Hobby":"Code"}["Name"])
print({"Name":"Nick", "Age":"27", "Hobby":"Code"}["Age"])
print({"Name":"Nick", "Age":"27", "Hobby":"Code"}["Hobby"])

greeting="Hello All"
print(greeting)
greeting=greeting.split(" ")[0]
print(greeting)

print("Hi")
print(str(5))
print(str(5.003))
print(str(True))
print(int(4))
print(float(3.17))
print(bool(True))

print(len("Hello all"))
print(len([1,23,4,5,2,3,89,5,7,5,3]))
print(len(["Hello", "Nick"][0]))
print(sorted(["B", "R", "2", "A", "W", "2.3", "a", "t"]))


def my_function():
    print("Hello, This is inside my_function")
    print("This is the second line inside my_function")
my_function()


def func1(i,j):
    print(i)
    print(j)
func1(10,20)

def func2(*people):
    for names in people:
        print("This person is", names)
func2("Albert", "Brad", "Catherine", "Daisy", "Ellen")