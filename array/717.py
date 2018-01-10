class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        l = len(bits)-2
        while(bits[l]>0 and l>=0):
            l-=1
        return (len(bits)-l)%2==0
    #找出第二个0与第一个0之间的1个数 0必为charcater结尾