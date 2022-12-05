import re
import copy


with open("day5\source.txt", "r") as f:
    boxes, moves = f.read().split('\n\n')
    moves = [[int(i) for i in re.findall(r'\d+', move)]
             for move in moves.split('\n')]
    boxes = [row[1::4] for row in boxes.split('\n')[:-1]]
    boxes = [[box for box in col[::-1] if box != ' '] for col in zip(*boxes)]


def move_boxes(boxes, moves, cratemover9001):
    arr = copy.deepcopy(boxes)
    for amount, start, end in moves:
        selected = arr[start-1][-amount:]
        if not cratemover9001:
            selected = selected[::-1]
        arr[end-1] += selected
        del arr[start-1][-amount:]
    top = ''.join(stack[-1] for stack in arr)
    return top


print(move_boxes(boxes, moves, cratemover9001=False))
print(move_boxes(boxes, moves, cratemover9001=True))
