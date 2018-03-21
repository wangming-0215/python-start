sandwich_orders = ['sandwich 01', 'sandwich 02',
                   'sandwich 03', 'sandwich 04', 'sandwich 05']

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print('I made your ' + current_sandwich)

print('\nFinish Orders\n')
for finished_sandwich in finished_sandwiches:
    print('\t' + finished_sandwich)
