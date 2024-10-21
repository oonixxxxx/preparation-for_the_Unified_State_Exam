class Test:
    def test_1(self):
        n = 5
        if factorial(n) == 120:
            print('Test passed')
        else:
            print('Test failed')
    
    def test_2(self):
        n = 6
        if factorial(n) == 720:
            print('Test passed')
        else:
            print('Test failed')
            

    def test_3(self):
        n = 7
        if factorial(n) == 5040:
            print('Test passed')
        else:
            print('Test failed')
        
def factorial(n):
    """return factorial

    Args:
        n (intenger): number to calculate factorial

    Returns:
        intenger: factorial of n
    """
    result = 1
    
    for i in range(1, n+1):
        result = result * i
        
    return result


if __name__ == '__main__':
    
    test = Test()
    test.test_1()
    test.test_2()
    test.test_3()
    
'''
for commit
'''