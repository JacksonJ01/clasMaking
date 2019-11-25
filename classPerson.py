# Jackson J.
# 11/23/19
# This is the Person class


class Person:

    def __init__(self, first, last, age, weight, height):
        self.first = first
        self.last = last
        self.age = age
        self.weight = weight
        self.height = height

    def details(self):
        return self.first + " " + self.last + " is " + self.age + " and weighs " + self.weight + " pounds " + " and stands at " + self.height + " inches tall"
