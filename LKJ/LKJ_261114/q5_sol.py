def solution(n):
    answer = 0

    #빈 보드 만들기
    board = [[0] * n for _ in range(n)]


    #이동시키도록 방향 설정 (오 > 아 > 왼> 위)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    

    #초기값
    row, col = 0, 0
    direction = 0
    
    for number in range(1, n * n + 1):
        board[row][col] = number  #1부터 n*n+1 까지 숫자를 채워주기

        if number == n * n:
            break
        
        #다음 칸의 위치 계산
        next_row = row + dr[dicrection]
        next_col = col + dc[dicrection]

        #다음 칸이 보드 밖이거나 숫자가 존재한다면 인덱스 번호 바꿔서 돌도록
        if (not (0 <= next_row < n and 0 <= next_col < n ) or board[next_row][next_col] != 0):
            dircetion = (direction + 1) % 4

        #실제 위치 값 계산
        row += dr[direction]
        col += dc[dircetion]

    #대각선 값 총합
    for i in range(n):
        answer += board[i][i]
    
    return answer









n1 = 3
ret1 = solution(n1)

print("solution 함수의 반환 값은", ret1, "입니다.")
    
n2 = 2
ret2 = solution(n2)

print("solution 함수의 반환 값은", ret2, "입니다.")
