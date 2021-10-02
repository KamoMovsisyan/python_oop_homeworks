# 1
class Example:
    def __init__(self, word):
        self.word = word
        
    def make_dict(self):
        global my_dict
        my_dict = dict()
        for i in self.word:
            my_dict[i] = self.word.count(i)
        print(my_dict)

    def remove_duplicates(self):
        my_dict_new = dict()
        for (key, value) in my_dict.items():
            if value not in my_dict_new.values():
                my_dict_new[key] = value
        print(my_dict_new)

    def highest_three(self):
        my_list = list()
        for value1 in my_dict.values():
            for value2 in my_dict.values():
                if value1 >= value2:
                    my_list.append(value1)
        my_list = list(set(my_list))
        my_list = my_list[-3:]
        print(my_list)

text = Example('python')

text.make_dict()
text.remove_duplicates()
text.highest_three()

#2
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        area = math.pi * self.radius**2
        print(area)

    def get_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        print(perimeter)

my_circle = Circle(10)

my_circle.get_area()
my_circle.get_perimeter()

#3
class GetTarget:
    def __init__(self, your_list : list, target : int):
        self.your_list = your_list
        self.target = target
    
    def get_target(self):
        index_list = list()
        for i in self.your_list:
            for j in self.your_list:
                if i + j == self.target:
                    index_list.append(self.your_list.index(i))
                    index_list.append(self.your_list.index(j))
        index_list = list(set(index_list))

        print(index_list)

my_target = GetTarget([10,20,10,40,50,60,70], 50)

my_target.get_target()