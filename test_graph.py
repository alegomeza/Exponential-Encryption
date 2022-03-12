from graphs import *

def s_a(mess = None):
    print(mess , 'sa')
    ans = str(input('1 o 2? '))
    return ans , mess

def s_b(mess = None):
    print(mess , 'sb')
    ans = str(input('1 o 2? '))
    return ans , mess

def s_1(mess = None):
    print(mess, 's1')
    ans = str(input('A o B? ')).lower()
    return ans , mess

def s_2(mess = None):
    print(mess, 's2')
    ans = str(input('A o B? ')).lower()
    return ans , mess


sa , sb = Node(s_a,'test') , Node(s_b)
s1 , s2 = Node(s_1) , Node(s_2)

sa.next = {'1':s1, '2':s2}
sb.next = {'1':s1, '2':s2}
s1.next = {'a':sa, 'b':sb}
s2.next = {'a':sa, 'b':sb}

g = Graph(sa)
g.run()
