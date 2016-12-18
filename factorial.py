import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
#logging.disable(logging.CRITICAL)
#DEBUG, INFO, WARNING, ERROR, CRITICAL
def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug('i is %s, total is %s' % (i,total))
    return total
print(factorial(5))
logging.debug('End of program')
