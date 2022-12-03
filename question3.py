# By Ming Kang u2004991


# Note that the row and column has interchanged. 
# i = row and j = columns in python versus i = columns and j = row in hand writing

# Initialise an array storing values. initially all values are 0
u = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]
# Initialise an array storing errors 
u_e = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]

# Apply boundary conditions
u[0][1]=75
u[0][2]=75
u[0][3]=75
u[1][4]=100
u[2][4]=100
u[3][4]=100
u[1][0]=50
u[2][0]=50
u[3][0]=50
u[4][1]=100
u[4][2]=100
u[4][3]=100
end = False
count = 0

# Perform iterations until the relative error for all terms < 1%
while (end == False):
    count += 1

    u[1][1] = (125 + u[2][1] + u[1][2])/4
    u[2][1] = (50 + u[3][1] + u[1][1] + u[2][2])/4
    u[3][1] = (150 + u[2][1] + u[3][2])/4

    u[1][3] = (175 + u[2][3] + u[1][2])/4
    u[3][3] = (200 + u[2][3] + u[3][2])/4
    u[1][2] = (75 + u[2][2] + u[1][3] + u[1][1])/4

    u[2][3] = (100 + u[3][3] + u[1][3] + u[2][2])/4
    u[2][2] = (u[3][2] + u[1][2] + u[2][3] + u[2][1])/4
    u[3][2] = (100 + u[2][2] + u[3][3] + u[3][1])/4

    # Calculate the errors for each term
    end = True
    for i in range (1,4):
        for j in range (1,4):
            val = u[i+1][j] + u[i-1][j] + u[i][j+1] + u[i][j-1] - 4*u[i][j]
            error = val*100
            if error >= 1:
                end = False
            u_e[i][j] = error


print("Number of Iterations: " + str(count))