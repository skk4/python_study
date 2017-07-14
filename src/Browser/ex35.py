# _*_ coding:utf-8 _*_
__author__ = 'oukohou'
class Lexicon(object):

    def __init__(self):
        self.directions = ('south','north','west','east','center')
        self.verbs = ('go','kill','eat','run','tell','shoot','sing','love')
        self.stops = ('a','the','in','of','to','via')
        self.nouns = ('bear','princess','MissHei','tiger','dragon','door')
        self.sen = []

    def scan(self,sentence):
        self.sentence = sentence
        sentence = self.sentence.split(' ') # 断句。
        self.sen = [] # 由于使用的是同一个实例‘lexicon’的变量sen进行测试，
                      # 为了能够多次测试，需要在每次scan函数开始时将sen置空。

        for word in sentence:
            try:
                if word.lower() in self.directions:
                    self.sen.append(('direction',word.lower()))
                elif word.lower() in self.verbs:
                    self.sen.append(('verb',word.lower()))
                elif word.lower() in self.stops:
                    self.sen.append(('stop',word.lower()))
                elif word.lower() in self.nouns:
                    self.sen.append(('noun',word))
                elif word.isdigit() == True: # 不是字符串，则认为是数字
                    #word.isdigit()
                    self.sen.append(('number',word))
                else:
                    raise ValueError
            except ValueError: # 捕获到int（）函数的异常，则为error
                self.sen.append(('error',word))
        return self.sen

lexicon = Lexicon() # 注意到给出的test代码中是直接调用lexicon.scan("north"),
                    # scan为unbound函数，则显然lexicon是一个实例，需要先实例化
#print lexicon.scan('kill the bear')                  
#print lexicon.scan('kill the bear').pop(0)                  