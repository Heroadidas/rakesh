facts = {
    'burger': 'food',
    'pizza': 'food',
    'sandwich': 'lunch',
    'pizza': 'dinner'
}
rules = {
    'food': 'meal',
}
query = 'sandwich'

def is_dinner(item):
    if facts.get(item) == 'food' and rules.get('food') == 'meal':
        return True
    elif facts.get(item) == 'dinner':
        return True
    else:
        return False
print(is_dinner(query))
