# a - запись новых данных в файл, добавление в конец файла
import time

fw = open('file1.txt', 'a')
fw.write("file1\n")
fw.close()

# w - запись новых данных в файл, удаление данных файла перед записью
fw = open('file2.txt', 'w')
fw.write("file2\n")
fw.close()

# r - читать
fr = open('file1.txt', 'r')
text = fr.read()
fr.close()
print(text)

fr_plus = open('file1.txt', 'r+')
fr_plus.write("file3\n")
fr_plus.close()
text = fr_plus.read()
fr_plus.close()
print(text)