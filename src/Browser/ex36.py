# -*- coding:utf-8 -*-
'''
Created on 2017.7.4

@author: Administrator
'''
from Browser.ex35 import Lexicon
class ParserError(Exception):
    pass


class Sentence(object):

    def __init__(self, subject, verb, object):
        # remember we take ('noun','princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]


def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

'''
移除对应类型单词“the a in”
返回stop类数据
'''
def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            print word_list
            return word
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)
        print match(word_list, word_type)


def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")


def parse_object(word_list):
    skip(word_list, 'stop')
    next = peek(word_list)

    if next == 'noun':
        return match(word_list, 'noun')
    if next == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")


def parse_subject(word_list, subj):
    verb = parse_verb(word_list)
    obj = parse_object(word_list)
    print Sentence(subj, verb, obj)

    return Sentence(subj, verb, obj)


def parse_sentence(word_list):
    #忽略stop类单词，并移处word_list
    skip(word_list, 'stop')
    

    #获取word_list第一个单词
    start = peek(word_list)

    if start == 'noun':
        #查找到‘noun’单词，并移出word_list
        #subj为返回的noun类单词
        subj = match(word_list, 'noun')
        return parse_subject(word_list, subj)
    elif start == 'verb':
        # assume the subject is the player then
        return parse_subject(word_list, ('noun', 'player'))
    else:
        raise ParserError("Must start with subject, object, or verb not: %s" % start)
    
wl = Lexicon().scan("kill the north")
print 'wl:',wl
print 'start,peek(wl):', peek(wl)
print 'match(wl, "stop"):', match(wl, 'stop')

x = parse_sentence(wl)
print x

