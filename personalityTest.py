
def pQuestion(list, text: str):
	print(text)
	retry = True
	while retry:
		match input().upper():
			case '1' | 'A':
				return list[0]
			case '2' | 'B':
				return list[1]
			case '3' | 'C':
				return list[2]
			case '4' | 'D':
				return list[3]

hiddenVal = 0

hiddenVal += pQuestion([15,0, -20, 100],
	"""Pick a letter:
	A. Apples
	B. Bananas
	C. Corn
	D. Dollar bills"""
)

if hiddenVal < 0:
	print('You are a shark. Have fun in the ocean!')
elif hiddenVal == 0:
	print('You are a zombie..')
elif hiddenVal > 50:
	print('''You are a billionaire! Now what?''')
else:
	print('''You are a tree.
		The winds grace you with their presence.''')
