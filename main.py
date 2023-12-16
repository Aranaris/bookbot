with open('books/frankenstein.txt','r') as file:
	book_contents = file.read()
	print(str(len(book_contents.split())) + ' words found in the document.\n')
	count = {}
	for char in book_contents:
		if char.lower() not in count:
			count[char.lower()] = 1
		else:
			count[char.lower()] += 1

	sorted_alpha_list = []
	for key in count:
		if key.isalpha():
			if len(sorted_alpha_list) == 0:
				sorted_alpha_list.append(key)
			else:
				for i in range(len(sorted_alpha_list)):
					if count[sorted_alpha_list[i]] < count[key]:
						sorted_alpha_list.insert(i, key)
						break
					elif i == len(sorted_alpha_list) - 1:
						sorted_alpha_list.append(key)

	for char in sorted_alpha_list:
		print(f'The "{char}" character was found {count[char]} times.')

