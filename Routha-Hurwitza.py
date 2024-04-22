import sympy as sp

def determinant(matrix):
    # Function to calculate the determinant of a matrix

    n = len(matrix)
    
    if n == 1:
        # Base case: if the matrix is 1x1, return its only element
        return matrix[0][0]
    else:
        det = 0
        sign = 1
        # Iterate over each column of the first row
        for i in range(n):
            # Generate the submatrix by removing the current row and column
            submatrix = [row[:i] + row[i+1:] for row in matrix[1:]]
            # Recursive call to calculate the determinant of the submatrix
            sub_det = determinant(submatrix)
            # Add the determinant of the submatrix multiplied by the current element and its sign
            det += sign * matrix[0][i] * sub_det
            # Change the sign for the next iteration
            sign *= -1
        return det

def calculate_determinants(matrix, max_power):
    # Function to calculate determinants for each power from 1 to max_power

    determinants = []
    for power in range(1, max_power + 1):
        # Extract submatrix based on the current power
        submatrix = [row[:power] for row in matrix[:power]]
        # Calculate determinant for the submatrix
        det = determinant(submatrix)
        determinants.append(det)

    return determinants

def check_positive_coefficients(coefficients):
    # Function to check if all coefficients are positive
    return all(coef > 0 for coef in coefficients)

def criterion_routh_hurwitz(matrix):
    max_power = len(matrix)
    determinants = calculate_determinants(matrix, max_power)

    all_positive = all(det > 0 for det in determinants)
    has_zero = any(det == 0 for det in determinants)

    if all_positive:
        print("The system is stable.")
    elif has_zero:
        print("The stability can't be recognized.")
    else:
        print("The system is unstable.")


def main():
    s = sp.Symbol('s')
    M = s**4 + 6*s**3 + 13*s**2 + 12*s + 4
    
    # Extract coefficients from the polynomial M
    coefficients = sp.Poly(M, s).all_coeffs()
    
    # Determine the size of the matrix
    size_power = len(coefficients) - 1 
    
    # Initialize the matrix
    matrix = []
    for i in range(size_power):
        row = []
        for j in range(size_power):
            index = size_power - 3 - i + 2*j
            if index >= 0 and index < len(coefficients):
                row.append(coefficients[index])
            else:
                row.append(0)
        matrix.append(row)
        
    # Print the matrix
    print(f'Size power: {size_power}')
    print("Matrix:")
    for row in matrix:
        print(row)

    if check_positive_coefficients(coefficients):
        criterion_routh_hurwitz(matrix)
    else:
        print("The system is unstable due to negative coefficients.")
        
    
    
if __name__ == "__main__":
    main()
