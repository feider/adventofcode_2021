import numpy as np

boards = []
numbers = []
lines = []

#with open ('input_test.txt', 'r') as f:
with open ('input.txt', 'r') as f:
    for l in f:
        lines.append(l.strip())

numbers = [int(n) for n in lines[0].split(',')]

for i_l in range(1, len(lines), 6):
    board = np.zeros([5, 5])
    for i in range(5):
        l = [int(l) for l in lines[i_l+i+1].replace('  ', ' ').split(' ')]
        board[i, :] = np.asarray(l)
    boards.append(board)

markeds = [np.zeros([5, 5]) for i in range(len(boards))]


def check_boards(masks):
    winning_boards = []
    for i, m in enumerate(masks):
        if np.max(np.sum(m, 0)) == 5:
            winning_boards.append(i)
        elif np.max(np.sum(m, 1)) == 5:
            winning_boards.append(i)
    return winning_boards

wb = []
winnum = -1
for num in numbers:
    wb = check_boards(markeds)
    if len(wb) > 0:
        break
    winnum = num
    for b, m in zip(boards, markeds):
        mask = b==num
        mask = mask.astype(int)
        m += mask

b = boards[wb[0]]
m = markeds[wb[0]]

u = b*m
u = b-u
s = np.sum(u[:])
print(s)
print(winnum)
print(int(s*winnum))
