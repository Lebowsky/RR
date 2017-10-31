import os
import find_regex

path = r'C:\Users\User\AppData\Roaming\1C\1CEStart'
file_name = 'ibases.v8i'
full_path_name = (os.path.join(path, file_name))
# print(os.path)
# print(os.path.abspath('.'))#рабочий каталог абсолютный путь
# print(os.path.isabs('.')) #False
# print(os.path.isabs(os.path.abspath('.'))) #True
# print(os.getcwd()) #рабочий каталог
# os.chdir('path')
# os.makedirs('path')
# print(os.path.dirname(path)) #C:\Users\User\AppData\Roaming\1C
# print(os.path.basename(path)) #1CEStart
# print(path.split(os.path.sep)) #['C:', 'Users', 'User', 'AppData', 'Roaming', '1C', '1CEStart']
# print(os.path.getsize(full_path_name))
# print(os.listdir(path))
# if os.path.exists(path):
#     sizes = [os.path.getsize(os.path.join(path, f)) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))] #подсчитаем суммарный размер файлов в папке
#     print(sum(sizes))

copy_file = 'ibases_copy.v8i_'                                        #Получим список всех баз и папок
full_path_name = os.path.join(path, copy_file)
with open(full_path_name, encoding='utf-8')as file_ibases:
    bases = (find_regex.getBaseNames(file_ibases.read()))

# with open('bases.txt', 'w', encoding='utf-8') as file_bases:
#     file_bases.write('\n'.join(bases))

import shelve
import pprint
# with shelve.open('shelve_bases') as shelveFile:
#     shelveFile['bases'] = bases

with shelve.open('shelve_bases') as shelveFile:
    print(pprint.pformat(shelveFile['bases']))
