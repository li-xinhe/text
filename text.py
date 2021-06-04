import re ##调用正则表达式的包
class match2Words(object):
    lines=0
    def __init__(self,path,word1,word2):
        self.path = path
        self.word1 = word1
        self.word2 = word2
    def key_match(self):
        with open(self.path,'rb') as f:
            buffer = f.read()
        pattern = re.compile(self.word1+b'(.*)'+self.word2,re.S)
        result = pattern.findall(buffer)
        if result != []:
            result = re.sub(r'\\n|b', ' ', str(result).replace('[','').replace(']',''))
            return result
        else:
            print ("none")
            article=[]
section=[]
chapter=[] ##创建3个空list
alltitle=[]
word_file=open('Cape Verde_2002.txt')
for line in word_file.readlines(): ##分别读取每一行
    if bool(re.search('-', line)) == True: ##如果这一行里有“-”说明这行是标题
        if bool(re.search('Article', line)) or bool(re.search('Section', line)) or bool(re.search('Chapter', line)) ==True:

            alltitle.append(line.strip())    
            text=[]
path = 'Cape Verde_2002.txt'

for i in range(len(alltitle)-1):
    word1 = str(alltitle[i]).encode('utf-8')
    word2 = str(alltitle[i+1]).encode('utf-8')
    matchWords = match2Words(path, word1, word2)
    textc=matchWords.key_match()
    text.append(textc)
    text=[]
