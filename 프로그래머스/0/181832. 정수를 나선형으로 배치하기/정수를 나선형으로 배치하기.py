def solution(n):
    dir = 'right'
    x = 0
    y = 0
    num = 1

    answer = [[0] * n for _ in range(n)]

    while num <= n * n:
        answer[y][x] = num

        # 마지막 숫자까지 넣었으면 더 이동하지 말고 끝
        if num == n * n:
            break

        if dir == 'right':
            # 오른쪽이 벽이거나 이미 숫자가 있으면 아래로 방향 전환
            if x + 1 >= n or answer[y][x + 1] != 0:
                dir = 'down'
                y += 1
            else:
                x += 1

        elif dir == 'down':
            # 아래쪽이 벽이거나 이미 숫자가 있으면 왼쪽으로 방향 전환
            if y + 1 >= n or answer[y + 1][x] != 0:
                dir = 'left'
                x -= 1
            else:
                y += 1

        elif dir == 'left':
            # 왼쪽이 벽이거나 이미 숫자가 있으면 위로 방향 전환
            if x - 1 < 0 or answer[y][x - 1] != 0:
                dir = 'up'
                y -= 1
            else:
                x -= 1

        elif dir == 'up':
            # 위쪽이 벽이거나 이미 숫자가 있으면 오른쪽으로 방향 전환
            if y - 1 < 0 or answer[y - 1][x] != 0:
                dir = 'right'
                x += 1
            else:
                y -= 1

        num += 1

    return answer