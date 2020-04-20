slovo = input("введите слово и оно добавится в файл:")
f = open('text.txt', 'r+')
f.writelines('/n' + slovo)
f.close()
