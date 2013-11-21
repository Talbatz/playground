gimetric_value = {
                 "a" : 1,
                 "b" : 2,
                 "c" : 3,
                 "d" : 4,
                 "e" : 5,
                 "f" : 6,
                 "g" : 7,
                 "h" : 8,
                 "i" : 9,
                 "j" : 10,
                 "k" : 20,
                 "l" : 30,
                 "m" : 40,
                 "n" : 50,
                 "o" : 60,
                 "p" : 70,
                 "q" : 80,
                 "r" : 90,
                 "t" : 100,
                 "u" : 200,
                 "v" : 300,
                 "w" : 400,
                 "y" : 500,
                 "z" : 600
                 }


def map():
    inp = raw_input("Your word?")
    count = 0
    for i in range(len(inp)):
        count += gimetric_value[inp[i]]
    return count



print map()
