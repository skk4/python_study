# -*- coding:utf-8 -*-
import pickle
t = 'xieshangji'
pickle_f = open('d:\\precord.pkl', 'wb')
pickle.dump(t, pickle_f)
pickle_f.close()


picket_f2 = open('d:\\precord.pkl', 'rb')

t2 = pickle.load(picket_f2)
print t2
picket_f2.close()

