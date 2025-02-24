from collections import deque

def find_shortest_path(grid, start, end):
    # Получаем размеры сетки
    m = len(grid)
    n = len(grid[0])
    
    # Проверка, что начальная и конечная точки корректны
    if not (0 <= start[0] < m and 0 <= start[1] < n and grid[start[0]][start[1]] == 0):
        return []
    if not (0 <= end[0] < m and 0 <= end[1] < n and grid[end[0]][end[1]] == 0):
        return []
    
    # Направления движения
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Очередь для BFS
    queue = deque([start])
    visited = [[False] * n for _ in range(m)]
    visited[start[0]][start[1]] = True
    
    # Матрица расстояний
    distance = [[float('inf')] * n for _ in range(m)]
    distance[start[0]][start[1]] = 0
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == end:
            break
            
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
                
    # Если путь найден, восстанавливаем его
    path = []
    if distance[end[0]][end[1]] != float('inf'):
        current_x, current_y = end
        while (current_x, current_y) != start:
            path.append((current_x, current_y))
            min_dist = float('inf')
            for dx, dy in directions:
                nx, ny = current_x + dx, current_y + dy
                if 0 <= nx < m and 0 <= ny < n and distance[nx][ny] < min_dist:
                    min_dist = distance[nx][ny]
                    next_x, next_y = nx, ny
            current_x, current_y = next_x, next_y
        path.append(start)
        
    return list(reversed(path))  # Возвращаем путь от старта к финишу