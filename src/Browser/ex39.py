'''
Created on 2017.7.6

@author: Administrator
'''
'''
list = [('type', 'id=wk'), ('search', 'id=su')]
l_len = len(list)
for i in range(l_len):
    list[i]
    print list[i]
print l_len
print list[0][0]
'''
class parse_action(object):
    def parse_list(self, word_list):

        for i in range(len(word_list)):
            
            if word_list[i][0] == 'type':
                
                print 'type run id %s' %word_list[i][1]
            elif word_list[i][0] ==  'search':
                print 'search run id %s' %word_list[i][1]
            #return word_list[i]
   
    def key_action(self, word_list):
        self.word_list = word_list
        if self.word_list[0][0] == 'type':
            print 'type run'
        elif self.word_list[0][0] == 'search':
            print 'search run'
            
        else:
            print 'unreconige run'
            
p = parse_action()
a_list = [('type', 'id=wk'), ('search', 'id=su')]
pp = p.parse_list(a_list)
#p.key_action(pp)

#p.key_action(a_list)      