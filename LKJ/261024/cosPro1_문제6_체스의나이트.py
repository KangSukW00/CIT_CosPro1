def solution(pos):
    answer = 0

    # 나이트의 경로 경우의 수 
    moves = [(-2,-1), (-2,1),
             (-1,-2), (-1,2),
             (1, -2), (1, 2),
             (2, -1), (2, 1)
    ]

    # 체스판을 0행0열 기준으로 계산하기 편하게 변환
    col = ord(pos[0]) - ord('A')
    row = int(pos[1]) - 1

    # 각 경우 계산 후 체스 판 내에 있는지 판단
    for dc, dr in moves:
        next_col = col + dc
        next_row = row + dr

        if 0 <= next_col < 8 and 0 <= next_row < 8:
            answer += 1

    return answer
