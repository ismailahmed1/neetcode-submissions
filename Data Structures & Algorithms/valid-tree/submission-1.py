class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adjacency_dic = {i: [] for i in range(n)}  
        
        for a, b in edges:
            adjacency_dic[a].append(b)
            adjacency_dic[b].append(a)
        
        seen = set()
        def dfs(node, parent):
            if node in seen:
                return False
            
            seen.add(node)
            for nxt in adjacency_dic[node]:
                if nxt == parent:
                    continue
                if not dfs(nxt, node):
                    return False
            
            return True
        
        return dfs(0, -1) and len(seen) == n

