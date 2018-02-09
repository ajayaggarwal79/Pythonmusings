"""
SCRIPT TO READ THROUGH THE TRACE OF A MATRIX AND SUM THE VALUES


"""

NUM_ROWS = 25
NUM_COLS = 25

# construct a matrix
my_matrix = []
for row in range(NUM_ROWS):
    new_row = []
    for col in range(NUM_COLS):
        new_row.append(row * col)
    my_matrix.append(new_row)
 
# print the matrix
##for row in my_matrix:
##    print(row)
acc=0
x=0
#print (my_matrix[4][4])
while x <NUM_COLS:
    acc=my_matrix[x][x]+acc
    x=x+1
print(acc)
##    
