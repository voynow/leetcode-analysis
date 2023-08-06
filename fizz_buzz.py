class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        answer = []
        for i in range(1, n + 1):
            string = ""

            if not i % 3 or not i % 5:
                if not i % 3:
                    string += "Fizz"
                if not i % 5:
                    string += "Buzz"
            else:
                string += str(i)
            answer.append(string)
        return answer