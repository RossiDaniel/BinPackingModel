def tc_sfida():
	item_list = []
	bin_list = []

	bin_list.append(BP.Bin(2.70, 13.5, 2.45))
	bin_list.append(BP.Bin(0, 0, 0))

	for i in range(0,6):
		item = BP.Item(i, 0.10*i+0.1,0.3*i+0.1, 0.20*i+0.1)
		item.stackable = False
		item.order_id = 1
		item.weight = 4
		item_list.append(item)

	return item_list, bin_list
