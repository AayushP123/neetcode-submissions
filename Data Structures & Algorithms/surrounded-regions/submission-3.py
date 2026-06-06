class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs():
            q = deque()
            for r in range(rows):
                for c in range(cols):
                    if (board[r][c] == "O" and 
                        (r == rows - 1 or r == 0 or c == cols - 1 or c == 0)):
                        q.append((r, c))
            while q:
                r, c = q.popleft()
                if board[r][c] == "O":
                    board[r][c] = "T"
                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            q.append((nr, nc))
        bfs()
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"