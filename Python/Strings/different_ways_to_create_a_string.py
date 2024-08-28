string1 = 'Hello, My name is Sravani'
print(string1)

string2 = "Hello, My name is Sravani"
print(string2)

string3 = '''Hello, My name is Sravani'''
print(string3)

string4 = """Hello, My name is Sravani"""
print(string4)

num = 155
string5 = str(num)
print(string5)

string6 = 'Hello' + ', ' + 'My name is Sravani'
print(string6)

name = 'My name is Sravani'
string7 = f'Hello, {name}!'
print(string7)

string8 = 'Hello, {}!'.format(name)
print(string8)

words = ['Hello', 'My name is Sravani']
string9 = ' '.join(words)
print(string9)

string10 = repr('Hello, My name is Sravani')
print(string10)

string11 = bytes('Hello, My name is Sravani', encoding='utf-8')
print(string11)

string12 = ''.join([chr(i) for i in range(60, 90)])
print(string12)

string13 = 'Hello! ' * 3
print(string13)
