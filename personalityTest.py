
def pQuestion(list, text: str):
	retry = True
	while retry:
		print(text)
		try:
			match input().upper():
				# case '1' | 'A' <-- how to do cases with multiple triggers
				case 'A':
					return list[0]
				case 'B':
					return list[1]
				case 'C':
					return list[2]
				case 'D':
					return list[3]
				case _:
					print("Invalid input, try again")
		except Exception as e:
			print("Invalid input, try again")


print(
	"""
--------------------------------------------------------------------
| Welcome to my personality test! I'll tell you what organic thing |
|                you're most closely aligned with!                 | 
--------------------------------------------------------------------

"""
)

aura = 0

aura += pQuestion([4, 2, -4, 15],
	"""

Pick a food:
 A. Apples
 B. Bananas
 C. Corn
 D. Steak"""
)

aura += pQuestion([-3, -10, 3, 6],
	"""

What did the last person you encounter do:
 A. Wave
 B. Scream
 C. Do their own thing
 D. Talk to you"""
)

aura += pQuestion([0, 4, 6, -5],
	"""

What's your favorite game in this list?
 A. Minecraft
 B. Pokemon
 C. Apex Legends
 D. Undertale"""
)

aura += pQuestion([5, 1, -6, 8],
	"""

You suddenly have a bit of free time, what will you do?
 A. Work, errands, or chores
 B. Play a game
 C. Cook
 D. Some form of exercise

 """
)

if aura < 0:
	print('You are a shark. Have fun in the ocean!')
elif aura == 0:
	print('You are a zombie.. uh oh..')
else:
	if aura % 2 == 0:
		print("You're a lemon! I guess life gave you!")
	else:
		print('You are a tree. The winds grace you with their presence.')
