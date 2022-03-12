from graphs import Node, Graph

def s_a(mess = None):
    if mess:
        mess += 'a'
    print(mess , 'sa')
    ans = str(input('B o C? ')).lower()
    return ans , mess

def s_b(mess = None):
    if mess:
        mess += 'b'
    print(mess , 'sb')
    ans = str(input('A o C? ')).lower()
    return ans , mess

def s_c(mess = None):
    if mess:
        mess += 'c'
    print(mess, 's1')
    ans = str(input('A o B? ')).lower()
    return ans , mess

def exit_(data = None):
    exit()
    return ' ' , data

sa = Node(s_a,'~ ')
# sa = Node(s_a)
sb = Node(s_b)
sc = Node(s_c)
ex = Node(exit_)

sa.next = {'b':sb, 'c':sc, 'e':ex}
sb.next = {'a':sa, 'c':sc, 'e':ex}
sc.next = {'a':sa, 'b':sb, 'e':ex}
ex.next = {' ':ex}

g = Graph(sa)
g.run()

