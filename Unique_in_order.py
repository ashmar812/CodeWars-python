#funtion that takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.
def unique_in_order(iterable):
    count = 0
    catched=''
    result=[]
    for x in iterable:
        if x != catched:
            count =0
        if count==0:
            result.append(x)
            count+=1
            catched = x
    return result
