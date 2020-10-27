class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s = []
        temp = chars[0]
        count = 1
        j = 1

        for i in range(j,len(chars)):
          if(temp == chars[i]):
            count += 1
          else:
            s.append(temp)
            if(count != 1):
              for x in str(count):
                s.append(str(x))
              
            temp = chars[i]
            count = 1
            j = i

        s.append(temp)
        if(count != 1):
          for x in str(count):
            s.append(str(x))

        del chars[:]
        chars.extend(s)
        return len(chars)