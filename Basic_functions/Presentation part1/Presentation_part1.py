def foo():
    print('Hello World')
    print "Hello world"
    print 'Hello World'

#foo()

def foo2():
    name = raw_input('Name: ')
    if name == '':
        print "Hello admin"
    else:
        print 'Hello '+name

#foo2()

def foo3():
    number = raw_input('give me two numbers separated by commas: ')
    try:
        lis = number.split(",")
        print lis[0]+' + '+lis[1]+' = '+ str(float(lis[0])+float(lis[1]))
    except:
        print 'You didn\'t give me two numbers'


#foo3()

def foo4():
    #slicing
    s = 'Monty Python'
    print s[:6]+'                          '+s[6:]
    #
    print s.lower(), s.upper()
    #replace
    s2 = 'Banana'
    s3 = s2.replace('a','@')
    print s3
    #find
    letter = s2.find('n')
    print s2[letter]*100

    print 'a' in s2, 'a' in s3 


#foo4()

def listing():
    lis = list()
    for i in range(0,100,5):
        lis.append(i)
    print lis
    #assert lis[5]==4;
    a = lis.pop(5)
    lis.remove(0)
    print a ,'\n' ,lis

#listing()

def dictioning():
    purse = dict()
    purse['money'] = None
    purse['candy'] = 2
    purse['tissues'] = 'one'
    print purse
    print purse.get('money1',10)
    print purse.keys() , '\n', purse.items(), '\n', purse.values()


print range(0,100,5)
    