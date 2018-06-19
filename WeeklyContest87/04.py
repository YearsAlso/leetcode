from itertools import combinations



class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        if n < 2:
            return 0
        dsts = [[1e9 for i in range(n)] for j in range(n)]
        for i in range(n):
            dsts[i][i] = 0
            for j in graph[i]:
                dsts[i][j] = 1
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dsts[i][j] = min(dsts[i][j], dsts[i][k] + dsts[k][j])
        D = {}
        for i in range(n):
            D[(1 << i, i)] = 0
        best_path = 1e9
        for ss_size in range(2, n + 1):
            for ss in combinations(range(n), ss_size):
                bitset = 0
                for v in ss:
                    bitset |= 1 << v
                for v in ss:
                    bitset_1 = bitset ^ (1 << v)
                    D[(bitset, v)] = min([D[(bitset_1, v1)] + dsts[v1][v] for v1 in ss if v1 != v])
                    if ss_size == n:
                        best_path = min(best_path, D[(bitset, v)])
        return best_path


def main():
    sol = Solution()

if __name__ == '__main__':
    main()