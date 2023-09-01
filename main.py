def first_column(matrix):
    """
    This function returns the first column (as a list) of any non-    
    empty matrix with this limitations:
    - The matrix must be not empty and the matrix's
    lists or rows must have at least one value or element.
    """
    first_column = []
    for i in range(0, len(matrix)):
        first_column.append(matrix[i][0])
    return first_column

def largest_width(column_array):
    """
    Input: non-empty array (i.e., at least one element).
    Output: largest string's length of a given column.
    Note: all array's elements must be able to convert to string.
    """
    largest = -1
    for i in column_array:
        if (len(str(i)) > largest):
            largest = len(str(i))
            answer = str(i)
    return len(answer)

def generate_spaces(num):
    #Return a string with n number of spaces.
    string = ""
    for i in range(num + 1):
        string = string + " "
    return string

def divide_string(string):
    #return a list of n-number-character pieces of a given string  
    chunks = [(string[i:i + 54]) for i in range(0, len(string), 54)]
    return chunks
