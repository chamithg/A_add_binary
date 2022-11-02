class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return self.dec2Bin(self.bin2dec(a)+self.bin2dec(b))

    def bin2dec(self,str):
        decNo = 0
        for i in range(len(str)):
            decNo += int(str[i])* (2**(len(str)-1-i))
        print(decNo)
        return decNo

    def dec2Bin(self,num):
        if num == 0:
            return "0"
        bin =""
        while num>=1:
            bin = str(num%2) + bin
            num = num//2
        print(bin)

        return bin

obj = Solution()
a = "1010"
b = "1011"

print(obj.addBinary(a,b))