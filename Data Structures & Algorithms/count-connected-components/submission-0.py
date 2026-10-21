class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adjacency_dic = {i : [] for i in range(n)}

        for a, b in edges:
            adjacency_dic[a].append(b)
            adjacency_dic[b].append(a)

        seen = set()
        def dfs(node):
            seen.add(node)
            for nxt in adjacency_dic[node]:
                if nxt not in seen:
                    dfs(nxt)
            
        count = 0 
        for i in range(n):
            if i not in seen:
                count += 1
                dfs(i)
        
        return count

