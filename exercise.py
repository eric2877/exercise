
import fileinput as file
from operator import le
import random as rand


def generate_exercise(num, num_line):
    col = num / num_line
   
    arr = []
    while len(arr)< num :
        a = rand.randint(1,19)
        b = rand.randint(1,19)
        c = rand.randint(1,2)
        d = 0
        if c == 2 and a > b :
            d = a -b
        else:
            d = a + b
        if d >20 :
            continue
        s = str(a)
        s += " - " if c == 2 and a > b else " + "
        s += str(b)
        s += " ="
        if s in arr :
            continue
        else:
            arr.append(s)

    index = 1
    list2 = []
    for s in arr :
        if index < col:
            index += 1
            s += ' '*(15 - len(s))
        else :
            s += '\n'
            index= 1
        list2.append(s)

    return str.join("" , list2)


def generate_combine(num, num_line):
    col  = num/ num_line
    arr = []
    while len(arr) < num :
        a = rand.randint(1,9)
        b = rand.randint(1,9)
        o1 = rand.randint(1,2);
        o2 =  rand.randint(1,2);
        c = 0
        if  o1 > 1 and a > b and o2 >1 :
            c = rand.randint(0, a-b)
        elif o2 > 1:
            c = rand.randint(0, a+b)
        else :
            c = rand.randint(0, 9)
        s = str(a)
        s += " - " if o1 > 1 and a > b else " + "
        s += str(b)
        s += " - " if o2 > 1 else " + "
        s += str(c)
        s += " ="
        if s in arr :
            continue
        else:
            arr.append(s)
    index = 1
    list2 = []
    for s in arr :
        if index < col:
            index += 1
            s += '\t'
        else :
            s += '\n'
            index= 1
        list2.append(s)
    
    return str.join("" , list2)

if __name__ == '__main__':
    with open("output.txt", 'w') as target:
        target.write(generate_exercise(100, 20))
        # target.write(generate_combine(20, 5))
    