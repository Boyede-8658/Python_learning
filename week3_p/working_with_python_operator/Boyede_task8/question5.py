#Create Dictionary
store = {'Book': 10, 'Pen': 20, 'Bag': 5}
store_copy = store.copy()
item_to_buy = input('Enter item you want to buy: ')
item_quantity = int(input('Enter quantity you want to buy: '))
store[item_to_buy] -= item_quantity
print(f'Original Dictionary: {store_copy}')
print(f'Dictionary After: {store}')