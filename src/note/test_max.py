'''
���б���ȡ��һ���������������ֵmax��Ȼ���б�������ֵ�Ƚ�each��max�Ƚ�:
����б�����eachֵ����max����ô��each��ֵ��max��max = each��
����б���û��eachֵ����max����ômax�϶������
'''
def max(x):
    max_one = x[0]
    for each in x:
        if each > max_one:
            max_one = each
    return max_one                     