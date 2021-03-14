"""
- implement one or more of the integer multiplication algorithms described in lecture.
- multiply only pairs of single-digit numbers.  
- You can implement the grade-school algorithm if you want, 
    but to get the most out of the assignment you'll want to implement recursive integer multiplication and/or Karatsuba's algorithm.

So: what's the product of the following two 64-digit numbers?
3141592653589793238462643383279502884197169399375105820974944592
2718281828459045235360287471352662497757247093699959574966967627

- before submitting, first test the correctness of your program on some small test cases of your own devising

Food for thought: the number of digits in each input number is a power of 2.  Does this make your life easier?  
Does it depend on which algorithm you're implementing?
"""

"""
Karatsuba multiplication
x = 10^(n//2).a + b
y = 10^(n//2).c + d
x.y = 10^n a.c + 10^(n//2) a.d + b.c + b.d  .... eqn(*)

step 1: recursively compute a.c
step 2: ... b.d
step 3: ... (a + b)(c + d)
step 4:  step 3 - step 2 - step 1 = a.d + b.c
solve eqn(*)

base case: if single digits, multiply, return value

"""

class Solution:

    def KaratsubaMx(self, x:int, y:int):

        # get number of digits
        n = 0
        tmp = x
        while tmp > 0:
            n += 1
            tmp //= 10

        return self.KaratsubaMxHelper(x,y,n)



    def KaratsubaMxHelper(self,x:int, y:int, n:int) -> int:

        # base case
        if n == 1:
            return x*y

        # find a, b, c, d
        n = n//2
        a = x//10**n
        b = x % 10**n
        c = y//10**n
        d = y % 10**n

        # recursive calls
        ac = self.KaratsubaMxHelper(a,c,n)
        bd = self.KaratsubaMxHelper(b,d,n)
        apb_cpd = self.KaratsubaMxHelper( a+b, c+d, n)

        # compute product
        return 10**(2*n) * ac + 10**n *(apb_cpd -ac - bd) + bd


def main():
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627

    soln = Solution()

    print("x*y = ", x*y)
    print("Karatsuba solution: ", soln.KaratsubaMx(x,y))
    print("Correct? ", x*y == soln.KaratsubaMx(x,y))


main()
