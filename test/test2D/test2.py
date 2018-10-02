
'''

test con 9 item
0.5,0.5, 1 : 3
1, 0.8, 1.2 : 3
0.5, 0.9, 0.75 : 3

'''


def tc_sfida():
	item_list = []
	bin_list = []

	bin_list.append(BP.Bin(2.70, 13.5, 2.45))
	bin_list.append(BP.Bin(0, 0, 0))

	for i in range(0,3):
		item = BP.Item(i, 0.5,0.5, 1)
		item.stackable = False
		item.order_id = 1
		item.weight = 4
		item_list.append(item)

	for i in range(3,6):
		item = BP.Item(i, 1, 0.8, 1.2)
		item.stackable = False
		item.order_id = 1
		item.weight = 4
		item_list.append(item)

	for i in range(6,9):
		item = BP.Item(i, 0.5, 0.9, 0.75)
		item.stackable = False
		item.order_id = 1
		item.weight = 4
		item_list.append(item)

	return item_list, bin_list
