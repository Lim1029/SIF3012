# By Ming Kang u2004991


# Note that the row and column has interchanged. 
# i = row and j = columns in python versus i = columns and j = row in hand writing

# Initialise an array storing values. initially all values are 0
T = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

#Apply boundary conditions
for j in range (10):
    T[0][j] = 100

for j in range (10):
    T[5][j] = 25

for i in range (1,5):
    T[i][0] = 20

#define all constants 
k = 54
rho = 7800
c_p = 490
alpha = k/(rho*c_p)
delta_t = 3
delta_x = 0.01

#Explicit Method
for j in range (9):
    for i in range (1,5):
        T[i][j+1] = T[i][j] + ((alpha*delta_t)/(delta_x)**2)*(T[i-1][j]-2*T[i][j]+T[i+1][j])

#print out each row in T, where the columns show different t and rows show differnt x
for i in T:
    print(i)