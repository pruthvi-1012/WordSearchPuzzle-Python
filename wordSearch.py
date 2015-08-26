import sys

# Check for the argument:
# If file name is not given as inputfile it will print error message and system will exit

if (len(sys.argv) <2):
        print("Input file is not given")
        print("Please enter the names of input file")
        print("for example: wordSearch.py inputFileName.plz")
        sys.exit()

# open input file to read the inputs and devide them into
# grid and list of words

with open(sys.argv[1], "r") as file:
    grid_latters,list_words = file.read().split("\n\n")

# give output file same name as input file with .out extension
# and open file to write output data on it

opFile= sys.argv[1].split('.')
outputFile= open(opFile[0]+'.out',"a")


# Main function of program it checks every col and row with its starting position
# and then it will call searchWordFromGrid function
# which will check if the word is in the grid at the starting position

def searchWord(grid,word):
    (rows, cols) = (len(grid), len(grid[0]))
    for row in xrange(rows):
        for col in xrange(cols):
            result = searchWordFromGrid(grid, word, col, row)
            if (result != None):                
                return result
        
    return outputFile.write(word + " not found\n" )


# With starting col and row position following function searchWordFromGrid will search word in every possible
# direction and it returns direction with end position col and row defined with value 0


def searchWordFromGrid(grid, word, colStart, rowStart):
    (colEnd,rowEnd)=(0,0)
    
    for dir in xrange(4):
        result = searchWordFromGridInDirection(grid, word, colStart, rowStart, dir, colEnd, rowEnd)
        if (result != None):
            return result
       
    return None

        
# Following function searchWordFromGridInDirection is given specific starting col and row,
# directions (dRow,dCol) and end col and row
# This function will check if the word matches in the given grid starting at given starting location
# and heading to given direction

def searchWordFromGridInDirection(grid, word, colStart, rowStart, dir, colEnd, rowEnd):
    (rows, cols) = (len(grid), len(grid[0]))
    dirs = [ (-1,0), (0,-1),
             (0,+1), (+1,0) ]
    dirNames = [ "up", "left",
                 "right", "down" ]
    
    (drow,dcol) = dirs[dir]    
    for i in xrange(len(word)):
        row = rowStart + i*drow
        col = colStart + i*dcol
        if ((row < 0) or (row >= rows) or (col < 0) or (col >= cols) or
            (grid[row][col] != word[i])):
            return None

    if (dirNames[dir] =='right'):
            (colEnd, rowEnd) = (colStart+ len(word), rowStart+1)
    elif (dirNames[dir] =='down'):
            (colEnd, rowEnd) = (colStart+1, len(word)+rowStart)
    elif (dirNames[dir] =='left'):
            (colEnd, rowEnd) = ((colStart+1)-len(word)+1 ,rowStart +1)
    elif (dirNames[dir] =='up'):
            (colEnd, rowEnd) = (colStart+1 ,(rowStart+1)-len(word)+1)
#   print word, (colStart+1, rowStart+1),(colEnd,rowEnd)
    outputFile.write (word + " (" + str(colStart+1) + "," + str(rowStart+1) +") (" + str(colEnd) + "," + str(rowEnd)+ ")\n" )
    return word
    

# Convert the grid and word from input file in list
grid_latters= grid_latters.split()
list_words= list_words.split()

# Convert list of grid in nested list by separatin each latter in String
new_grid= []
for line in grid_latters:
    string= line.split()
    numbers= [(n) for n in string]
    new_grid.append(list(line.rstrip()))

    
# Check condition if given input is N*N grid
isMatrixSquare=True
for i in xrange(len(grid_latters)):
    if not (len(grid_latters[i]) == len(grid_latters)):
        isMatrixSquare=False
        
# If grid is not N*N print error message otherwise call the searchWord function
# by giving each grid of latter and String of words by calling each word and removing
# repeat words

if (isMatrixSquare==False):
    print("OOPS your grid is not SQUARE (N*N)")
    exit

else:
        
# Remove duplicates
    for word in list_words:

        if (list_words.count(word) >=2):
            list_words.remove(word)

    for word in list_words:
                searchWord(new_grid,word)
