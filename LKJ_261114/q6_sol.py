#체스판을 0 시작으로 초기화
row = int(pos[1]) - 1
col = ord(pos[0]) - ord("A")

#나이트의 움직일 수 있는 경우
moves = [
    (-2,-1),(-2, 1),
    (-1, -2), (-1, 2),
    (1, -2), (1, 2),
    (2, -1), (2, 1)
    ]

# 다음 위치 값 계산
for dc, dr in moves:
    next_col = col + dc
    next_row = row + dr

    if 0 <= next_col < 8 and 0 <= next_row < 8:
        answer +=1


return answer
