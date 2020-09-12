import numpy as np 

def main():
    """
    Prints out the largest palindrome made from the product of two 3-digit numbers. 
    """
    ls = np.arange(100, 1000, 1)
    palindromes = []
    for i in ls: 
        for j in ls:
            product = i*j
            if IsPalindrome(product):
                palindromes.append(product)

    print(f'The largest palindrome made from the product of two 3-digit numbers is {max(palindromes):,}.')
    
def IsPalindrome(number):
    """
    The function checks whether the number is palindrome or not. 
    Input: 3-digit number
    Output: Boolean -- True when the number is palindrome. 
    """
    palindrome = True 
    number = str(number)
    if number != number[:: -1]: 
        palindrome = False 
    return palindrome

if __name__ == '__main__':
    main()