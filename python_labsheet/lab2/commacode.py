
# Comma code

spam = [
    'apples', 'bananas', 'oranges', 'grapes', 'watermelons', 'blueberries', 
    'strawberries', 'kiwis', 'pears', 'peaches', 'mangoes', 'pineapples',
    'cherries', 'plums', 'lemons', 'limes', 'cantaloupes', 'honeydews', 
    'papayas', 'passion fruit', 'dragon fruit', 'pomegranates', 'blackberries', 
    'raspberries', 'coconuts', 'avocados', 'figs', 'dates', 'jackfruit', 
    'guavas', 'lychees', 'tangerines', 'nectarines', 'cucumbers', 'tomatoes', 
    'bell peppers', 'spinach', 'kale', 'broccoli', 'cauliflower', 'carrots',
    'potatoes', 'sweet potatoes', 'pumpkins', 'zucchinis', 'squash', 'onions',
    'garlic', 'ginger', 'radishes', 'beets', 'turnips', 'parsnips', 'peas', 
    'beans', 'lentils', 'corn', 'asparagus', 'brussels sprouts', 'celery', 
    'cabbage', 'lettuce', 'eggplant', 'mushrooms'
]


def commaCode(list):
	return ', '.join([*spam[:-1], f'and {spam[-1]}'])


result = commaCode(spam)
print(result)



