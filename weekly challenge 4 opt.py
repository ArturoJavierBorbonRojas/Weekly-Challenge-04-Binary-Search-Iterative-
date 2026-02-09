import numpy as np

# Weekly challenge 4: Binary Search (Iterative)
# Autor: Ing. Arturo Javier Borbon Rojas

# 1 Generate pseudo random values
#n= 15 # Number of objects in the list
n= np.random.randint(0,100)
norder_list= np.random.randint(0,100, n) # Disorganized list
order_list= np.sort(norder_list)  # Ordenated list

# 2 Define a random objective
objective= np.random.randint(0,100)

# 3 Print our pseudo random values
print("-----------------------")
print("Our pseudo random values")
print("Our objective: ", objective)
print("Our number of objects in list: ", n)
print("Our disorganized list: ", norder_list)
print("Our organized list: ", order_list)
print("-----------------------")

# 4 Define function
def binary_search(arr,x):
    low=0
    high= len(arr)-1
    attempts=0

    while low <= high:
        attempts +=1
        mid= (low + high) // 2 # With this operation we find the half
        guess=arr[mid]

        print(f"Attempts:{attempts}. Index {mid}(valor¨{guess})...") 

        if guess==x:
            return f"\n Found it! The number:{x} is in the index:{mid}. Attempts:{attempts}""\n-----------"
        if guess > x: 
            high= mid - 1 # The objective is minor, we will rule it out on the right
        else:
            low= mid + 1 # The objective is bigger, we will rule it out on the left
    return f"\n The number objective: {objective} does not exist in the list. Total attempts: {attempts}""\n-----------"    

# 4 Execute the algorithnm
print(binary_search(order_list, objective))
