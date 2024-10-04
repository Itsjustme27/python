
# Comma code

spam = ['apples', 'bananas', 'tofu', 'cats']

def func(list):
	print(', '.join([*spam[:-1], f'and {spam[-1]}']))


func(spam)


