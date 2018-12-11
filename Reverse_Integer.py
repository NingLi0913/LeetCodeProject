class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sig = (x > 0) - (x < 0)
        x *= sig
        length = len(str(x))
        y = []
        s = 0
        for i in range(length):
            y.append(x // pow(10, length - i - 1))
            x = x % pow(10, length - i - 1)
            s = y[i] * pow(10, i) + s
        result = sig * s
        if result > pow(2, 31) - 1 or result < -pow(2, 31):
            result = 0
        return result

if __name__ == '__main__':
    demo = Solution()
    Input = -1234
    Output = demo.reverse(Input)
    print(Output)



