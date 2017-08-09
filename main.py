import progressbar

raw_file = open('raw.img', 'rb')

raw_file.seek(0, 2)
length = raw_file.tell()
raw_file.seek(0, 0)

check = [0xff, 0xd8, 0xff, 0xe0, 0xe1]
bufer = []
namefile = 0
bar = progressbar.ProgressBar(max_value=length)
i = 0
while i < length:
	bufer = raw_file.read(4)
	if (bufer[0] == check[0] and bufer[1] == check[1] and
		bufer[2] == check[2] and (bufer[3] == check[3] or bufer[3] == check[4])):
		picture = open(str(namefile)+'.jpg','wb')
		namefile += 1
	try:
		picture.write(bufer)
	except:
		pass
	i += 1
	bar.update(i)



