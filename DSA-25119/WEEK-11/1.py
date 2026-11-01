size = 10
# Separate Chaining
def separate_chaining(keys): 
    table = [[] for _ in range(size)] 
    for key in keys:
        index = key % size 
        table[index].append(key)

    print("\nSeparate Chaining:") 
    for i in range(size):
        print(i, ":", table[i])

# Linear Probing
def linear_probing(keys): 
    table = [None] * size 
    for key in keys:
        index = key % size
        
        while table[index] is not None: 
            index = (index + 1) % size

        table[index] = key

    print("\nLinear Probing:") 
    for i in range(size):
        print(i, ":", table[i])

# Quadratic Probing
def quadratic_probing(keys): 
    table = [None] * size 
    for key in keys:
        index = key % size
        i = 0
        
        while i < size:
            new_index = (index + i * i) % size

            if table[new_index] is None: 
                table[new_index] = key 
                break
            i += 1

    print("\nQuadratic Probing:") 
    for i in range(size):
        print(i, ":", table[i]) 

# Main program
keys = list(map(int, input("Enter the keys (separated by space): ").split())) 
separate_chaining(keys) 
linear_probing(keys) 
quadratic_probing(keys)
