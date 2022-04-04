#a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value
def two_sum(numbers, target):
    for x in range(len(numbers)):
        if numbers.count(target-numbers[x]):
            return [x,numbers[x+1:].index(target-numbers[x])+x+1]
