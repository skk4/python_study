#-*-coding=utf-8-*-
class GrandPa:
    def __init__(self):
        print('I\'m GrandPa')


class Father(GrandPa):
    def __init__(self):
        print('I\'m Father!')

class Son(Father):
    """A simple example class"""
    i = 12345
    def __init__(self):
        print('���ǹ��캯��,son')
    def sayHello(self):
        return 'hello world'

if __name__ == '__main__':
    son = Son()
    # ���Ͱ�����Ϣ 
    print('���Ͱ�����Ϣ: ',Son.__doc__)
    #��������
    print('��������:',Son.__name__)
    #�������̳еĻ���
    print('�������̳еĻ���:',Son.__bases__)
    #�����ֵ�
    print('�����ֵ�:',Son.__dict__)
    #��������ģ��
    print('��������ģ��:',Son.__module__)
    #ʵ������
    print('ʵ������:',Son().__class__)