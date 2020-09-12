
def main():
    """
    The function prints the least number for which the proportion of bouncy numbers is 0.99,
    where bouncy numbers are neither increasing nor decreasing numbers such as 155349.

    """
    number = 99
    bouncy_n  = 0
    while True:
        number += 1
        if IsBouncy(number):
            bouncy_n += 1
            proportion = (bouncy_n / number)
            if proportion == 0.99:
                print(f'The least number when the proportion of bouncy numbers is 99% is {number:,}')
                break

def IsIncreasing(num):
    """
    Input: number
    Output: Boolean -- True when the number is increasing
    """
    num = str(num)
    increasing = True 
    for i in range(len(num)-1):
        if int(num[i]) > int(num[i +1]):
            increasing = False 
    return increasing
 

def IsDecreasing(num):
    """
    Input: number
    Output: Boolean -- True when the number is decreasing
        """
    num = str(num)
    decreasing = True
    for i in range(len(num)-1):
        if int(num[i]) < int(num[i +1]):
            decreasing = False 
    return decreasing

def IsBouncy(num):
    """
    Input: number
    Output: Boolean -- True when the number is bouncy
        """
    bouncy = True 
    if IsIncreasing(num) or IsDecreasing(num):
        bouncy = False
    return bouncy 


if __name__ == '__main__':
    main()

