print('''

**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************

''')

order = {'wings':0, 'cookies':0, 'spring rolls':0, 'salmon':0, 'steak':0, 'meat tornado':0, 'a literal garden':0, 'ice cream':0, 'cake':0, 'pie':0, 'coffee':0, 'tea':0, 'unicorn tears':0}

while True:
  x = input('> ').lower()
  if x == 'quit':
    break
  if x not in order:
    print('Item not in menu')
  else:
    order[x] = order[x] +1
    print(f'** {order[x]} orders of {x} have been added to your meal **')

print('** Order Summary **')
for e in order:
  if order[e] > 0:
    print(f'** {order[e]} {e} **')
print('Thanks for your business!')
