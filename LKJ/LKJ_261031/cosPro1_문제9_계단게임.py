# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
[[(guide-anchor):(한줄을 수정하시오. )]]
def func(record):
	if record == 0:
		return 1
	elif record == 1:
		return 2
	return 0

def solution(recordA, recordB):
	cnt = 0
	for i in range(len(recordA)):
		if recordA[i] == recordB[i]:
			continue
		elif recordA[i] == func(recordB[i]):
			cnt = cnt + 3
		else:
			cnt = max(cnt - 1, 0) 
	return cnt
