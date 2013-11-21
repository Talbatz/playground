def get_multipication_table(n):
    return [[(i+1) * (j+1) for i in range(n)] for j in range (n)]

n = raw_input("multiplier? ")

print get_multipication_table(n)
