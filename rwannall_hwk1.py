
def fib(n):

    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    elif (n < 0):
        return 0
    else:
        sum = 1
        a = 1
        b = 1
        for x in range(2, n):
            sum = a + b
            b = a
            a = sum
            print(x+1,sum)
            # print(sum)
        return sum

print(fib(14))

# f = fib(10)
# # print(f)

# print("########################################################################################################################")
########################################################################################################################

def reversed(list):
    length = len(list)
    newList = [0]*length

    i = 0
    for x in range(length, 0, -1):
        j = x - 1
        newList[i] = list[j]
        i = i+1

    # print(newList)
    return newList

# myList = [1,2,3,4,5]
#
# reversed(myList)

# print("########################################################################################################################")
########################################################################################################################

def is_prime(n):

    if n < 2:
        return False
    test = n-1
    for x in range(2,n):
        if n%x == 0:
            return False

    return True

# print(is_prime(-2))

# print("########################################################################################################################")
########################################################################################################################

def nub(xs):
    newList = list()

    length = len(xs)

    for x in range(0, length):
        length2 = len(newList)
        found = False
        for y in range(0,length2):
            if (newList[y] == xs[x]):
                found = True

        if found == False:
            newList.append(xs[x])

    # print(xs)
    # print(newList)
    return newList

# put = [4,2,5,1,3,2,2,2,3,3,3,4,4,4,5,5,5]
# print(nub(put))

# print("########################################################################################################################")
########################################################################################################################


def add(x,y):
    return x+y

def zip_with(f,xs,ys):
    length = 0
    if (len(xs) > len(ys)):
        length = len(ys)
    else:
        length = len(xs)

    gotIt = [0]*length
    for x in range(0,length):
        gotIt[x] = f(xs[x], ys[x])
    # print(gotIt)

    return gotIt

# xs = [1,2,3,4]
# ys = [1,2,3,4]

# print(put)
# zip_with(add, put ,put)

# print("########################################################################################################################")
########################################################################################################################

def collatz(n):
    coll = list()
    coll.append(n)
    while n != 1:
        # check if n is even or odd

        # EVEN
        if (n%2 == 0):
            n = n/2
            num = int(n)
            coll.append(num)
        # ODD
        else:
            n = 3*n
            n = n+1
            num = int(n)
            coll.append(num)

    # print(coll)
    return coll

# collatz(33)

# print("########################################################################################################################")
########################################################################################################################

#        [[1,2,3, 4,5,6, 7,8,9],
# 		 [4,5,6, 7,8,9, 1,2,3],
# 		 [7,8,9, 1,2,3, 4,5,6],
#
# 		 [2,3,4, 5,6,7, 8,9,1],
# 		 [5,6,7, 8,9,1, 2,3,4],
# 		 [8,9,1, 2,3,4, 5,6,7],
#
# 		 [3,4,5, 6,7,8, 9,1,2],
# 		 [6,7,8, 9,1,2, 3,4,5],
# 		 [9,1,2, 3,4,5, 6,7,8],
# 		]
#
# Check each row in the group of 3.
# Make 9 different lists for each of the columns......
#     if one of the rows is not good then stop......
#
# then check each column (list) at the end of the whole thing

def check_list(n):
    if (len(n) != 9):
        return False

    passList = [1,2,3,4,5,6,7,8,9]

    if (set(passList) == set(n)):
        return True
    else:
        return False


# check1 = [4,5,6,7,8,9,1,2,3]
# print(check_list(check1))
#
# grid  = [[1,2,3, 4,5,6, 7,8,9],
# 		 [4,5,6, 7,8,9, 1,2,3],
# 		 [7,8,9, 1,2,3, 4,5,6],
#
# 		 [2,3,4, 5,6,7, 8,9,1],
# 		 [5,6,7, 8,9,1, 2,3,4],
# 		 [8,9,1, 2,3,4, 5,6,7],
#
# 		 [3,4,5, 6,7,8, 9,1,2],
# 		 [6,7,8, 9,1,2, 3,4,5],
# 		 [9,1,2, 3,4,5, 6,7,8],
# 		]
#
# grid_rows_bad = [[1,2,3, 1,2,3, 1,2,3],
# 		 [4,5,6, 4,5,6, 4,5,6],
# 		 [7,8,9, 7,8,9, 7,8,9],
#
# 		 [2,3,4, 2,3,4, 2,3,4],
# 		 [5,6,7, 5,6,7, 5,6,7],
# 		 [8,9,1, 8,9,1, 8,9,1],
#
# 		 [3,4,5, 3,4,5, 3,4,5],
# 		 [6,7,8, 6,7,8, 6,7,8],
# 		 [9,1,2, 9,1,2, 9,1,2],
# 		]
#
# grid_cols_bad = [[1,2,3, 4,5,6, 7,8,9],
# 		 [4,5,6, 7,8,9, 1,2,3],
# 		 [7,8,9, 1,2,3, 4,5,6],
#
# 		 [1,2,3, 4,5,6, 7,8,9],
# 		 [4,5,6, 7,8,9, 1,2,3],
# 		 [7,8,9, 1,2,3, 4,5,6],
#
# 		 [1,2,3, 4,5,6, 7,8,9],
# 		 [4,5,6, 7,8,9, 1,2,3],
# 		 [7,8,9, 1,2,3, 4,5,6],
# 		]
#
# grid_grps_bad = [[1,2,3, 4,5,6, 7,8,9],
# 		        [2,3,4, 5,6,7, 8,9,1],
# 		        [3,4,5, 6,7,8, 9,1,2],
#
# 		 [4,5,6, 7,8,9, 1,2,3],
# 		 [5,6,7, 8,9,1, 2,3,4],
# 		 [6,7,8, 9,1,2, 3,4,5],
#
# 		 [7,8,9, 1,2,3, 4,5,6],
# 		 [8,9,1, 2,3,4, 5,6,7],
# 		 [9,1,2, 3,4,5, 6,7,8],
# 		]


def check_sudoku(grid):
    # ONLY STOP IF IT IS A FAIL

    passList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Checking by rows is easier, so I will swap the colums into rows.....
    # This creates 9x9 grid of all 0's
    gridSwap = [[0, 0, 0, 0, 0, 0, 0, 0, 0]] * 9



    # print('before')
    for x in range(1,10):
        # This is the temporary row.....
        rowList = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        # If it is wrong then it should just return false...so it ends
        if (set(grid[x-1]) != set(passList)):
            # print('ROW PROBLEM')
            return False
        # Just because the rows are equal does not mean that the columns are...
        # else:
        #     print('all equal')


        # NO MATTER WHAT - I want to flip the columns and rows
        # I need a second for loop in order to do that......
        for y in range(1,10):
            rowList[y-1] = grid[y-1][x-1]
            # print(rowList)

        # after that for loop, the row has been made into a column.....
        # Now inside the outter loop, need to put that into the gridSwap......
        # IT WORKS! The rows have swapped
        gridSwap[x-1] = rowList

    # print(gridSwap)
    # SAME THING AS BEFORE!!!
    for x in range(1,10):
        # If it is wrong then it should just return false...so it ends
        if (set(gridSwap[x-1]) != set(passList)):
            # print('COLUMN PROBLEM')
            return False
        # Just because the rows are equal does not mean that the columns are...
        # else:
        #     print('all equal AGAIN')


    ###################################################
    # I FORGOT ABOUT THE 3 GROUPS THINGS....
    # So instead of starting over, I just created an extra check at the end for it.....
    ###################################################
    groupList = list()

    # print(grid)
    # print(grid[1][1])
    for z in range(0,3):
        for a in range(0,3):
            groupList.append(grid[z][a])

    if (set(groupList) != set(passList)):
        # print('1st NOT GROUP WORKING')
        return False

    groupList = list()
    for z in range(0, 3):
        for b in range(3,6):
            groupList.append(grid[z][b])
    if (set(groupList) != set(passList)):
        # print('1st NOT GROUP WORKING')
        return False


    groupList = list()
    for z in range(0, 3):
        for c in range(6,9):
            groupList.append(grid[z][c])
    if (set(groupList) != set(passList)):
        # print('1st NOT GROUP WORKING')
        return False



    groupList = list()
    for z in range(3, 6):
        for a in range(0, 3):
            groupList.append(grid[z][a])
    if (set(groupList) != set(passList)):
        # print('2nd NOT GROUP WORKING')
        return False

    groupList = list()
    for z in range(3, 6):
        for b in range(3, 6):
            groupList.append(grid[z][b])
    if (set(groupList) != set(passList)):
        # print('2nd NOT GROUP WORKING')
        return False

    groupList = list()
    for z in range(3, 6):
        for c in range(6, 9):
            groupList.append(grid[z][c])
    if (set(groupList) != set(passList)):
        # print('2nd NOT GROUP WORKING')
        return False

    groupList = list()
    for z in range(6, 9):
        for a in range(0, 3):
            # print(grid[z][a])
            groupList.append(grid[z][a])
    if (set(groupList) != set(passList)):
        # print('3rd NOT GROUP WORKING')
        # print('sup')
        return False

    groupList = list()
    for z in range(6, 9):
        for b in range(3, 6):
            groupList.append(grid[z][b])
    if (set(groupList) != set(passList)):
        # print('3rd NOT GROUP WORKING')
        # print('hey')

        return False

    groupList = list()
    for z in range(6, 9):
        for c in range(6, 9):
            groupList.append(grid[z][c])
    if (set(groupList) != set(passList)):
        # print('3rd NOT GROUP WORKING')
        # print('dude')
        return False

    ################################
    # Got through all of them.....
    # print('IT WORKS')
    return True


# grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
#         [4, 5, 6, 7, 8, 9, 1, 2, 3],
#         [7, 8, 9, 1, 2, 3, 4, 5, 6],
#
#         [2, 3, 4, 5, 6, 7, 8, 9, 1],
#         [5, 6, 7, 8, 9, 1, 2, 3, 4],
#         [8, 9, 1, 2, 3, 4, 5, 6, 7],
#
#         [3, 4, 5, 6, 7, 8, 9, 1, 2],
#         [6, 7, 8, 9, 1, 2, 3, 4, 5],
#         [9, 1, 2, 3, 4, 5, 6, 7, 8],
#         ]
# # print(check_sudoku(grid))

# check_sudoku(grid)
# check_sudoku(grid_rows_bad)
# check_sudoku(grid_cols_bad)
# check_sudoku(grid_grps_bad)


# print("########################################################################################################################")
########################################################################################################################

def make_file(msg, filename="data.txt"):
    f = open(filename, 'w')
    f.write(msg)
    f.close()



def file_report(filename):
    # This makes the list of the numbers
    # with open("data.txt", "r") as myfile:
    #     data = myfile.readlines()
    #     print(data)

    f = open(filename,"r")
    numList = []
    for line in f:
        numList.append(int(line.strip()))

    mean = 0
    median = 0
    mode = []

    # print(numList)

    # Finding the summation
    sum = 0
    for x in range(0,len(numList)):
        # print(x)
        sum = sum+numList[x]
    # print(sum)

    # get the mean
    mean = 0
    mean = sum/len(numList)


    # SORT THE ELEMENTS
    numList.sort()
    # print(numList)
    middle = len(numList)/2
    # print(middle)
    # print(int(middle))

    # odd number, has true middle....so just cast to int to get rid of the .5
    if (len(numList)%2 != 0):
        # print("odd number")
        mid = int(len(numList)/2)
        # print(mid)
        # print(numList[mid])
        median = numList[mid]
    # this is even, so the middle given, need that one plus the position 1 above it to average
    else:
        mid1 = len(numList)/2
        mid2 = mid1-1
        median = (numList[int(mid1)] + numList[int(mid2)])/2
        # print(median)

    ###### FINDING THE MODE!!!!
    max = 0
    currMax = 0
    numbers = []
    prevNum = 0
    for x in range(0, len(numList)):
        if (x == 0):
            # The first one, is currently the max....so put it in the list
            max = 1
            currMax = 1
            prevNum = numList[x]
            numbers.append(numList[x])

        # Case 1 - it's a new number......so it can't be the max again....
        elif (prevNum != numList[x]):
            currMax = 1
            prevNum = numList[x]
            # BUTTTT - If it has the same.....for this new number (for example putting all with 1 occurence...then append...max stays same
            if (currMax == max):
                numbers.append(numList[x])

        # Case 2 - another 1 to the max
        elif (prevNum == numList[x]):
            currMax = currMax + 1
            # If its the same, don't need to add to the list....but max goes up
            # IF THAT CURR MAX IS NOW BIGGER THEN RESET THE LIST
            if (currMax == max):
                max = currMax
                # numbers = []
                numbers.append(numList[x])
            # Before it was just thi
            elif (currMax > max):
                max = currMax
                numbers = []
                numbers.append(numList[x])

    # test = mode([1,1,1,1,2])
    # print(test)
    ### FIND THE MODE

    # print(mean)
    # print(median)
    # print(mode)
    # print("--------------------------------------")

    # print(numList)
    mode = numbers
    # print(mode)
    finalList = [mean, median, mode]
    # print(finalList)
    return(mean, median, mode)


# make_file("1\n2\n3\n")
# file_report("data.txt")
# make_file("5\n5\n5\n25\n")

make_file(("1\n3\n2\n3\n1\n"))
file_report("data.txt")
#
# make_file("13\n6\n13\n3\n7\n29\n12\n1\n2\n14\n")
# file_report("data.txt")

