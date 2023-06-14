import re
import numpy as np

with open('time_used_log.txt', 'r') as f:
    lines = ''.join(f.readlines())

time_useds = re.findall('([0-9]*)ms', lines)

nData = 9
load_image = data_aug = load_pc = processing = 0
times = np.array([0 for _ in range(nData)])
for i, time_used in enumerate(time_useds):
    times[i % nData] += int(time_used)
times = times / (len(time_useds) / nData)
total = (times[:2] + times[7:]).sum()

print('Average time used:')
print(f'load image: {times[0]:.0f}ms {times[0] / total * 100:.1f}%')
print(f'data augmentation: {times[1]:.0f}ms {times[1] / total * 100:.1f}%')
print(f'    - get aug param: {times[2]:.0f}ms {times[2] / times[2:7].sum() * 100:.1f}%')
print(f'    - flip: {times[3]:.0f}ms {times[3] / times[2:7].sum() * 100:.1f}%')
print(f'    - affine input: {times[4]:.0f}ms {times[4] / times[2:7].sum() * 100:.1f}%')
print(f'    - affine output: {times[5]:.0f}ms {times[5] / times[2:7].sum() * 100:.1f}%')
print(f'    - get input: {times[6]:.0f}ms {times[6] / times[2:7].sum() * 100:.1f}%')
print(f'load point cloud: {times[7]:.0f}ms {times[7] / total * 100:.1f}%')
print(f'processing return: {times[8]:.0f}ms {times[8] / total * 100:.1f}%')
print(f'Total: {total:.0f}ms')