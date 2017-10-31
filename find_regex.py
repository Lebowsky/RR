import re

# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('Мой номер 978-735-7784')
# print(mo.group(0))
# print(mo.group(1))
# print(mo.group(2))
# print(mo.groups())
#
# phoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('Мой номер (978)-735-7784')
# print(mo.group(1))
# print(mo.group(2))

"""
\d - любая цифра
\w - любая буква
\s - любой пробельный символ или \t или \n
"""

# phoneNumRegex = re.compile(r'(\+\d\s*)?(\(?\d\d\d\)?)\s*-?\s*(\d\d\d\s*-?\s*\d\d\s*-?\s*\d\d)')
# # mo = phoneNumRegex.search('Мой номер +7(978)735-77-84; +79787776622')
# mo = phoneNumRegex.findall('Мой номер +7(978)735-77-84; +79787776622')
# if mo:
#     # print(mo.group())
#     print(mo)
#     print("".join(mo[0]))

#Замена строк
# namesRegex = re.compile(r'Agent \w+', re.I)
# print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents'))

def getBaseNames(text):
    nameBaseRegex = re.compile(r'\[.*\]')
    return nameBaseRegex.findall(text)