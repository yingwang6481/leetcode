class StringUtils:
    """
    @param: originalStr: the string we want to append to
    @param: size: the target length of the string
    @param: padChar: the character to pad to the left side of the string
    @return: A string
    """
    def leftPad(self, originalStr, size, padChar=' '):
        # write your code here
        len_str = len(originalStr)
        if size<=len_str:
            return originalStr
        a=[]
        for i in range(size - len_str):
            a.append(padChar)
        a.append(originalStr)
        return ''.join(a)
a = StringUtils()
print(a.leftPad('foo',5))