class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        triangle = []
        for i in range(numRows):
            cur_row = []
            for j in range(i + 1):
                if not j:
                    cur_row.append(1)
                elif j == i:
                    cur_row.append(1)
                else:
                    cur_row.append(sum(triangle[i - 1][j - 1: j + 1]))
            triangle.append(cur_row)
        return triangle
