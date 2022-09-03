# -*- coding: utf-8 -*-
"""

@author: Manea Loredana b1
"""

import random
from sympy.ntheory import jacobi_symbol

def jacobi(a, n):
        assert(n > a > 0 and n%2 == 1)
        t = 1
        while a != 0:
            while a % 2 == 0:
                a /= 2
                r = n % 8
                if r == 3 or r == 5:
                    t = -t
            a, n = n, a
            if a % 4 == n % 4 == 3:
                t = -t
            a %= n
        if n == 1:
            return t
        else:
            return 0
 



N = 1000
for _ in range(1000):
    
   a =random.randrange(1, N)
   n = random.randrange(a+1, 2*N)
   if n%2 == 0:
       n += 1
       j1 = jacobi_symbol(a, n)
       j2 = jacobi(a, n)
   if j1 == j2:
      print(a, n, j1, j2)
      
      
      
      
      