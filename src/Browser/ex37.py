# -*- coding:utf-8 -*-
'''
Created on 2017.7.5

@author: Administrator
'''
from Browser.ex35 import Lexicon
#创建一个可以抛出的异常类 ParserError
class ParserError(Exception):
    pass

#创建一个sentence类
class Sentence(object):

    def __init__(self, subject, verb, obj):
        # remember we take ('noun','princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]


#一个peek函数用来看到列表中的单词并返回单词的类型        
def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None
        
#使用 match 函数来处理单词，用它来确认预期中的单词是否是正确的类型，将它移出列表，并返回该词 
def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None   

#skip方法来跳过句子中我们不关心的单词 ，不只跳过一个单词而是跳过所有该类型的词 
#match里包含list.pop()方法可以移出指定类型元组  
def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)  
        



'''
跳过所有"stop"类型的词，然后提前获得下一个单词，并确认它是"verb"类型，如果不是，则抛出一个异常 ;
如果是"verb"类型，则使用"match"处理，将它移出列表
'''        
def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")
    
    
'''
重复操作，跳过"stop"类型的词，提前判断下一个词，决定下一个"sentence".
在函数 parse_object 中，我们需要同时处理“名词”和类似宾语的“方向”
'''       
def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")  
    
    
'''
解析主语的方法也是一样的，但是当我们处理隐藏的名词"player"的时候，我们需要用到"peek"
'''
def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")
    
#所有的方式都准备好之后，我们最后一个函数 parse_sentence
def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)
#[('stop', 'the'), ('noun', 'bear'), ('verb', 'run'), ('direction', 'north')]

wl = Lexicon().scan("the princess the kill bear")
x = parse_sentence(wl)
print x.subject +' ' + x.verb +' ' + x.object
                           