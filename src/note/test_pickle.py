# -*- coding:gbk -*-
import pickle
a_list = {'a':1, 'b':2}
pickle_file = open('my_list.pkl', 'wb')
pickle.dump(a_list, pickle_file)
