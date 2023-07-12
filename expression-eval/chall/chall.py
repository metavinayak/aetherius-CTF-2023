import os
import math
import random

class Expression(object):
    OPS = ['+', '-', '*','%']

    GROUP_PROB = 0.3

    MIN_NUM, MAX_NUM = 1, 100

    def __init__(self, maxNumbers, _maxdepth=None, _depth=0):
        """
        maxNumbers has to be a power of 2
        """
        if _maxdepth is None:
            _maxdepth = math.log(maxNumbers, 2) - 1

        if _depth < _maxdepth and random.randint(0, _maxdepth) > _depth:
            self.left = Expression(maxNumbers, _maxdepth, _depth + 1)
        else:
            self.left = random.randint(Expression.MIN_NUM, Expression.MAX_NUM)

        if _depth < _maxdepth and random.randint(0, _maxdepth) > _depth:
            self.right = Expression(maxNumbers, _maxdepth, _depth + 1)
        else:
            self.right = random.randint(Expression.MIN_NUM, Expression.MAX_NUM)

        self.grouped = random.random() < Expression.GROUP_PROB
        self.operator = random.choice(Expression.OPS)

    def __str__(self):
        s = '{0!s} {1} {2!s}'.format(self.left, self.operator, self.right)
        if self.grouped:
            return '({0})'.format(s)
        else:
            return s


def main():
    # The flag is in the environment variable. The below one is NOT the real flag.
    flag = os.environ.get('FLAG', 'ctf{***REDACTED***} Contact author if this is displayed')
    print('Evaluate the below till you get the flag')
    print('Hint: Don\'t do it manually :)\n')

    solved=1
    for _ in range(50):
        # x=str(Expression(5,5))
        x=str(Expression(5,2))

        val=eval(x)
        print(x)
        
        try:
            cmd = input('> ').strip()
            if(cmd==str(val)):
                pass
            else:
                solved=0
                exit()
        except:
            print("Nope")
            exit()
    if(solved):
        print(flag)

if __name__ == '__main__':
    main()

