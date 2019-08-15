from cpp.Waterman import waterman
import numpy as np

coords, faces = waterman(5)

assert (max(max(faces))==coords.shape[0]-1)

print(f'coords shape:{coords.shape}, max index:{max(max(faces))}\n')
print(f'coords:{coords}\n\nfaces:{faces}')
print(f'max:{np.max(coords)}, min:{np.min(coords)}')

# traverse
print('traverse faces')
for face in faces:
    for ic in face:
        print(coords[ic], end=', ')
    print()

print('\n\nok')
