def tc_sfida():
	item_list = []
	bin_list = []

	bin_list.append(BP.Bin(2.70, 13.5, 2.45))
	bin_list.append(BP.Bin(0, 0, 0))

	for i in range(0,2):
		item = BP.Item(i, 2,1, 1.5)
		item.stackable = False
		item.order_id = 1
		item.weight = 4
		item_list.append(item)

	for i in range(2,4):
		item = BP.Item(i, 0.5, 0.5, 2)
		item.stackable = False
		item.order_id = 1
		item.weight = 4
		item_list.append(item)

	for i in range(4,6):
		item = BP.Item(i, 0.5, 0.5, 1)
		item.stackable = False
		item.order_id = 1
		item.weight = 4
		item_list.append(item)

	return item_list, bin_list
