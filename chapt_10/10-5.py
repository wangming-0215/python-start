import re
file_name = 'README.md'

try:
    with open(file_name, encoding='utf-8') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = 'The file ' + file_name + ' dose not exist.'
else:
    # 这里是精髓，[\u4e00-\u9fa5]是匹配所有中文的正则，因为是unicode形式，所以也要转为ur
    # p = re.compile(r'[\u4e00-\u9fa5]')
    words = contents.split()
    print(contents)
    num_words = len(words)
    print('The file ' + file_name + ' has about ' + str(num_words) + ' words.')
