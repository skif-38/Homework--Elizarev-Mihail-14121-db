import heapq

def main():
    print("Введите данные как указано в задании: ")
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    srow, scol = map(int, input().split())
    crow, ccol = map(int, input().split())
    erow, ecol = map(int, input().split())
    
    INF = 10**9
    dist = [[[INF, INF] for _ in range(M)] for _ in range(N)]
    dist[srow][scol][0] = 0
    heap = [(0, srow, scol, 0)]
    
    while heap:
        d, r, c, cargo = heapq.heappop(heap)
        if d > dist[r][c][cargo]:
            continue
        if r == erow and c == ecol and cargo == 1:
            print(f"-----{d} метров необходимо проехать роботу, чтобы доставить груз в конечную клетку")
            return
        
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < N and 0 <= nc < M:
                if abs(grid[r][c] - grid[nr][nc]) <= 100:
                    new_cargo = cargo
                    if nr == crow and nc == ccol:
                        new_cargo = 1
                    if d + 1 < dist[nr][nc][new_cargo]:
                        dist[nr][nc][new_cargo] = d + 1
                        heapq.heappush(heap, (d + 1, nr, nc, new_cargo))

if __name__ == "__main__":
    main()