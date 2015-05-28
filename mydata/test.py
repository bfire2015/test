#!/usr/bin/env python
# -*- coding: utf-8 -*-

#name = raw_input('please enter your name:')
#print 'hello:',name
print '=============this is start ==============='
print 'hello, world'
print "this english "
print "this 中文 "
print "亲爱的%s 您好，你%d月的话费是%.2f元,余额是%.2f元,话费使用率%.2f%%" %('bfire',5,78.5,28.1,(78.5/(78.5+28.1))*100)
print '\n'
print '=============this is list and tuple ==============='
print '>>>>>01、this is list<<<<<'
classmates = ['michael','bob','tcacy']
print 'outprint classmates'
print classmates
print 'this is classmates len'
print len(classmates)
print 'this is classmates[1]'
print classmates[1]
print 'this is classmates[-1]'
print classmates[-1]
print 'this is classmates.append("adam")'
classmates.append("adam")
print classmates
print "this is classmates.insert(1,'jack') "
classmates.insert(1,'jack')
print classmates
print 'this is classmates.pop()'
classmates.pop()
print classmates
print 'this is classmates.pop(1)'
classmates.pop(1)
print classmates
print 'this is classmates[1]="sarah"'
classmates[1]="sarah"
print classmates
print 'this is p = ["asp","php"]'
print 'this is s = ["python","java",p,"scheme"]'
p = ["asp","php"]
s = ["python","java",p,"scheme"]
print p;
print s;
print '\n'
print '>>>>>02、this is tuple<<<<<'
print 'this is classmates '
classmates = ('micleal','bob','tracy')
print classmates
print 'tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：'
print '>>> t = (1, 2)'
t = (1, 2)
print t
print '如果要定义一个空的tuple，可以写成()：'
print '>>> t = ()'
t = ()
print t
print '但是，要定义一个只有1个元素的tuple，如果你这么定义：'
print '>>> t = (1)'
t = (1)
print t
print '定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。'
print '所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：'
print '>>> t = (1,)'
t = (1,)
print t
print 'Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。'
print '最后来看一个“可变的”tuple：'
print ">>> t = ('a', 'b', ['A', 'B'])"
print ">>> t[2][0] = 'X'"
print ">>> t[2][1] = 'Y'"
t = ('a', 'b', ['A', 'B'])
print t
t[2][0] = 'X'
t[2][1] = 'Y'
print t
print "这个tuple定义的时候有3个元素，分别是'a'，'b'和一个list。不是说tuple一旦定义后就不可变了吗？怎么后来又变了？"
print "别急，我们先看看定义的时候tuple包含的3个元素："
print "tuple-0"
print "当我们把list的元素'A'和'B'修改为'X'和'Y'后，tuple变为："
print "tuple-1"
print "表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。"
print "tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。"
print "即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！"
print '\n'
print '=============this is if and for ==============='
print '>>>>>01、this is if<<<<<'
print 'this is if'
print "age = 20"
print "if age >= 18:"
print "    print 'your age is', age"
print "    print 'adult'"
age = 20
if age >= 18:
    print 'your age is', age
    print 'adult'
print '\n'
print 'this is if,else'
print "age = 3"
print "if age >= 18:"
print "    print 'your age is', age"
print "    print 'adult'"
print "else:"
print "    print 'your age is', age"
print "    print 'teenager'"
age = 3
if age >= 18:
    print 'your age is', age
    print 'adult'
else:
    print 'your age is', age
    print 'teenager'
print '\n'
print 'this is if,elif,else'
print "age = 3"
print "if age >= 18:"
print "    print 'adult'"
print "elif age >= 6:"
print "    print 'teenager'"
print "else:"
print "    print 'kid'"
age = 3
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
else:
    print 'kid'
print '\n'
print '>>>>>02、this is for<<<<<'
print 'Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来，看例子：'
print "names = ['Michael', 'Bob', 'Tracy']"
print "for name in names:"
print "    print name"
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name
print "sum = 0"
print "for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:"
print "    sum = sum + x"
print "print sum"
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print sum
print 'range(101)就可以生成0-100的整数序列，计算如下：'
print "sum = 0"
print "for x in range(101):"
print "    sum = sum + x"
print "print sum"
sum = 0
for x in range(101):
    sum = sum + x
print sum
print "第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现："
print "sum = 0"
print "n = 99"
print "while n > 0:"
print "    sum = sum + n"
print "    n = n - 2"
print "print sum"
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum
print "再议raw_input"
print "birth = int(raw_input('birth: '))"
print "if birth < 2000:"
print "    print '00前'"
print "else:"
print "    print '00后'"
birth = int(raw_input('birth: '))
if birth < 2000:
    print '00前'
else:
    print '00后'
print '\n'
print '=============this is dict(map) and set ==============='
print '>>>>>01、this is dict<<<<<'
print "如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。用Python写一个dict如下："
print ">>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}"
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d['Michael']
print "把数据放入dict的方法，除了初始化时指定外，还可以通过key放入："
print ">>> d['Adam'] = 67"
d['Adam'] = 67
print d['Adam']
print "由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉"
print "如果key不存在，dict就会报错："
print "要避免key不存在的错误，有两种办法，一是通过in判断key是否存在："
print ">>> 'Thomas' in d"
'Thomas' in d
print "二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value："
print ">>> d.get('Thomas')"
print ">>> d.get('Thomas', -1)"
d.get('Thomas')
d.get('Thomas', -1)
print "注意：返回None的时候Python的交互式命令行不显示结果。"
print "要删除一个key，用pop(key)方法，对应的value也会从dict中删除："
print ">>> d.pop('Bob')"
d.pop('Bob')
print ">>> d"
print d
print '\n'
print "请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。"
print "和list比较，dict有以下几个特点："
print "查找和插入的速度极快，不会随着key的增加而增加；"
print "需要占用大量的内存，内存浪费多。"
print "而list相反："
print "查找和插入的时间随着元素的增加而增加；"
print "占用空间小，浪费内存很少。"
print "所以，dict是用空间来换取时间的一种方法。"
print "dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。"
print "这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。"
print "要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key："
print '\n'
print '>>>>>02、this is set<<<<<'
print "set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。"
print "要创建一个set，需要提供一个list作为输入集"
print ">>> s = set([1, 2, 3])"
s = set([1, 2, 3])
print s
print "注意，传入的参数[1, 2, 3]是一个list，而显示的set([1, 2, 3])只是告诉你这个set内部有1，2，3这3个元素，显示的[]不表示这是一个list。"
print "重复元素在set中自动被过滤："
print ">>> s = set([1, 1, 2, 2, 3, 3])"
s = set([1, 1, 2, 2, 3, 3])
print s
print "通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果："
print ">>> s.add(4)"
s.add(4)
print s
print ">>> s.add(4)"
s.add(4)
print s
print "通过remove(key)方法可以删除元素："
print ">>> s.remove(4)"
s.remove(4)
print s
print "set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作："
print ">>> s1 = set([1, 2, 3])"
print ">>> s2 = set([2, 3, 4])"
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print ">>> s1 & s2"
print s1 & s2
print ">>> s1 | s2"
print s1 | s2
print "set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错"

print "再议不可变对象"
print ">>> a = 'abc'"
a = 'abc'
print ">>> b = a.replace('a', 'A')"
b = a.replace('a', 'A')
print ">>> b"
print b
print ">>> a"
print a
print '\n'
print '=============this is 函数 ==============='
print '>>>>>01、this is 调用函数<<<<<'
print "绝对值的函数"
print ">>> abs(-20)"
print abs(-20)
print "而比较函数cmp(x, y)就需要两个参数，如果x<y，返回-1，如果x==y，返回0，如果x>y，返回1："
print ">>> cmp(1, 2)"
print cmp(1, 2)
print ">>> cmp(2, 1)"
print cmp(2, 1)
print ">>> cmp(3, 3)"
print cmp(3, 3)
print "数据类型转换"
print "Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数："
print ">>> int('123')"
print int('123')
print ">>> int(12.34)"
print int(12.34)
print ">>> float('12.34')"
print float('12.34')
print ">>> str(1.23)"
print str(1.23)
print ">>> unicode(100)"
print unicode(100)
print ">>> bool(1)"
print bool(1)
print ">>> bool('')"
print bool('')
print "函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”："
print ">>> a = abs # 变量a指向abs函数"
print ">>> a(-1) # 所以也可以通过a调用abs函数"
a = abs
print a(-1)
print '\n'
print '>>>>>02、this is 定义函数<<<<<'
print "在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。"
print "我们以自定义一个求绝对值的my_abs函数为例："
print "def my_abs(x):"
print "    if x >= 0:"
print "        return x"
print "    else:"
print "        return -x"
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print "请自行测试并调用my_abs看看返回结果是否正确。"
print "请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。"
print "如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。"
print "return None可以简写为return。"
print "空函数"
print "如果想定义一个什么事也不做的空函数，可以用pass语句："
print "def nop():"
print "    pass"
def nop():
    pass
print "pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。"
print "pass还可以用在其他语句里，比如："
print "if age >= 18:"
print "    pass"
if age >= 18:
    pass
print "缺少了pass，代码运行就会有语法错误。"
print "参数检查"
print "调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError："
print ">>> my_abs(1, 2)"
print "但是如果参数类型不对，Python解释器就无法帮我们检查。试试my_abs和内置函数abs的差别："
print ">>> my_abs('A')"
print ">>> abs('A')"
print "当传入了不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的my_abs没有参数检查，所以，这个函数定义不够完善。"
print "让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance实现："
print "def my_abs(x):"
print "    if not isinstance(x, (int, float)):"
print "        raise TypeError('bad operand type')"
print "    if x >= 0:"
print "        return x"
print "    else:"
print "        return -x"
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print "添加了参数检查后，如果传入错误的参数类型，函数就可以抛出一个错误："
print ">>> my_abs('A')"
print my_abs('A')
print "错误和异常处理将在后续讲到。"
print "返回多个值"
print "函数可以返回多个值吗？答案是肯定的。"
print "比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标："
print "import math"
print "def move(x, y, step, angle=0):"
print "    nx = x + step * math.cos(angle)"
print "    ny = y - step * math.sin(angle)"
print "    return nx, ny"
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
print "这样我们就可以同时获得返回值："
print ">>> x, y = move(100, 100, 60, math.pi / 6)"
print ">>> print x, y"
x, y = move(100, 100, 60, math.pi / 6)
print x, y
print "但其实这只是一种假象，Python函数返回的仍然是单一值："
print ">>> r = move(100, 100, 60, math.pi / 6)"
print ">>> print r"
r = move(100, 100, 60, math.pi / 6)
print r
print "原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。"
print '\n'
print '>>>>>03、this is 函数的参数<<<<<'
print "默认参数"
print "这个时候，默认参数就排上用场了。由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2："
print "def power(x, n=2):"
print "    s = 1"
print "    while n > 0:"
print "        n = n - 1"
print "        s = s * x"
print "    return s"
print "这样，当我们调用power(5)时，相当于调用power(5, 2)："
print ">>> power(5)"
print ">>> power(5, 2)"
print "而对于n > 2的其他情况，就必须明确地传入n，比如power(5, 3)。"
print "从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意："
print "一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；"
print "二是如何设置默认参数。"
print "当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。"
print "使用默认参数有什么好处？最大的好处是能降低调用函数的难度。"
print "举个例子，我们写个一年级小学生注册的函数，需要传入name和gender两个参数："
print "def enroll(name, gender):"
print "    print 'name:', name"
print "    print 'gender:', gender"
def enroll(name, gender):
    print 'name:', name
    print 'gender:', gender
print "这样，调用enroll()函数只需要传入两个参数："
print ">>> enroll('Sarah', 'F')"
print enroll
print "如果要继续传入年龄、城市等信息怎么办？这样会使得调用函数的复杂度大大增加。"
print "我们可以把年龄和城市设为默认参数："
print "def enroll(name, gender, age=6, city='Beijing'):"
print "    print 'name:', name"
print "    print 'gender:', gender"
print "    print 'age:', age"
print "    print 'city:', city"
print "这样，大多数学生注册时不需要提供年龄和城市，只提供必须的两个参数："
def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city
print ">>> enroll('Sarah', 'F')"
print enroll
print "只有与默认参数不符的学生才需要提供额外的信息："
print "enroll('Bob', 'M', 7)"
print enroll('Bob', 'M', 7)
print "enroll('Adam', 'M', city='Tianjin')"
print enroll('Adam', 'M', city='Tianjin')
print "可见，默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，又可以传递更多的参数来实现。无论是简单调用还是复杂调用，函数只需要定义一个。"
print "有多个默认参数时，调用的时候，既可以按顺序提供默认参数，比如调用enroll('Bob', 'M', 7)，意思是，除了name，gender这两个参数外，最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。"
print "也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。比如调用enroll('Adam', 'M', city='Tianjin')，意思是，city参数用传进去的值，其他默认参数继续使用默认值。"
print "默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下："
print "先定义一个函数，传入一个list，添加一个END再返回："
print "def add_end(L=[]):"
print "    L.append('END')"
print "    return L"
print "当你正常调用时，结果似乎不错："
def add_end(L=[]):
    L.append('END')
    return L
print ">>> add_end([1, 2, 3])"
print add_end([1, 2, 3])
print ">>> add_end(['x', 'y', 'z'])"
print add_end(['x', 'y', 'z'])
print "当你使用默认参数调用时，一开始结果也是对的："
print ">>> add_end()"
print add_end()
print "但是，再次调用add_end()时，结果就不对了："
print ">>> add_end()"
print add_end()
print ">>> add_end()"
print add_end()
print "很多初学者很疑惑，默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。"
print "原因解释如下："
print "Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。"
print "所以，定义默认参数要牢记一点：默认参数必须指向不变对象！"
print "要修改上面的例子，我们可以用None这个不变对象来实现："
print "def add_end(L=None):"
print "    if L is None:"
print "        L = []"
print "    L.append('END')"
print "    return L"
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print "现在，无论调用多少次，都不会有问题："
print ">>> add_end()"
print add_end()
print ">>> add_end()"
print add_end()
print "为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。"
print "可变参数"
print "在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。"
print "我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。"
print "要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下："
print "def calc(numbers):"
print "    sum = 0"
print "    for n in numbers:"
print "        sum = sum + n * n"
print "    return sum"
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print "但是调用的时候，需要先组装出一个list或tuple："
print ">>> calc([1, 2, 3])"
print calc([1, 2, 3])
print ">>> calc((1, 3, 5, 7))"
print calc((1, 3, 5, 7))
print "如果利用可变参数，调用函数的方式可以简化成这样："
print ">>> calc(1, 2, 3)"
print calc(1, 2, 3)
print ">>> calc(1, 3, 5, 7)"
print calc(1, 3, 5, 7)
print "所以，我们把函数的参数改为可变参数："
print "def calc(*numbers):"
print "    sum = 0"
print "    for n in numbers:"
print "        sum = sum + n * n"
print "    return sum"
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print "定义可变参数和定义list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数："
print ">>> calc(1, 2)"
print calc(1, 2)
print ">>> calc()"
print calc()
print "如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做："
print ">>> nums = [1, 2, 3]"
print ">>> calc(nums[0], nums[1], nums[2])"
nums = [1, 2, 3]
print nums
print calc(nums[0], nums[1], nums[2])
print "这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去："
print ">>> nums = [1, 2, 3]"
print ">>> calc(*nums)"
nums = [1, 2, 3]
print nums
print calc(*nums)
print "这种写法相当有用，而且很常见。"
print "关键字参数"
print "可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例："
print "def person(name, age, **kw):"
print "    print 'name:', name, 'age:', age, 'other:', kw"
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw
print "函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数："
print ">>> person('Michael', 30)"
print person('Michael', 30)
print "也可以传入任意个数的关键字参数："
print ">>> person('Bob', 35, city='Beijing')"
print person('Bob', 35, city='Beijing')
print ">>> person('Adam', 45, gender='M', job='Engineer')"
print person('Adam', 45, gender='M', job='Engineer')
print "关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。"
print "和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去："
print ">>> kw = {'city': 'Beijing', 'job': 'Engineer'}"
print ">>> person('Jack', 24, city=kw['city'], job=kw['job'])"
kw = {'city': 'Beijing', 'job': 'Engineer'}
print kw
print person('Jack', 24, city=kw['city'], job=kw['job'])
print "当然，上面复杂的调用可以用简化的写法："
print ">>> kw = {'city': 'Beijing', 'job': 'Engineer'}"
print ">>> person('Jack', 24, **kw)"
kw = {'city': 'Beijing', 'job': 'Engineer'}
print kw
print person('Jack', 24, **kw)
print "参数组合"
print "在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。"
print "比如定义一个函数，包含上述4种参数："
print "def func(a, b, c=0, *args, **kw):"
print "    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw"
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
print "在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。"
print ">>> func(1, 2)"
print func(1, 2)
print ">>> func(1, 2, c=3)"
print func(1, 2, c=3)
print ">>> func(1, 2, 3, 'a', 'b')"
print func(1, 2, 3, 'a', 'b')
print ">>> func(1, 2, 3, 'a', 'b', x=99)"
print func(1, 2, 3, 'a', 'b', x=99)
print "最神奇的是通过一个tuple和dict，你也可以调用该函数："
print ">>> args = (1, 2, 3, 4)"
args = (1, 2, 3, 4)
print args
print ">>> kw = {'x': 99}"
kw = {'x': 99}
print kw
print ">>> func(*args, **kw)"
print func(*args, **kw)
print "所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。"




print '=============this is dict and set ==============='
print '>>>>>01、this is dict<<<<<'
print '\n'
print '>>>>>02、this is set<<<<<'