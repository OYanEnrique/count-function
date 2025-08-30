# Counter function
print('------Counter function------')
from time import sleep

def counter(beginning, end, step):
	print(f'Counting from {beginning} to {end} by {step}s')
	sleep(1)
	if step == 0:
		step = 1
	if step < 0:
		step *= -1
	if beginning < end:
		for c in range(beginning, end + 1, step):
			print(f'{c} ', end='', flush=True)
			sleep(0.5)
			
	else:
		for c in range(beginning, end - 1, - step):
			print(f'{c} ', end='', flush=True)
			sleep(0.5)
	print('END!')
	
counter(1, 10, 1)
counter(10, 0, 2)
counter(10, -10, 2)