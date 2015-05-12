# ----------

# takes an email and returns the provider-host
def provider(email):
    papaki = email.find('@')
    if papaki == -1 : return 'Not an e-mail'
    fullProvider = email[papaki+1:]
    teleia = fullProvider.find('.')
    provider1 = fullProvider[:teleia]
    return provider1

#
def countLines(handler):
    count = 0
    for line in handler:
        count +=1
    return count

def countWords(handler):
    words = handler.read()
    return len(words)

# takes the handler and returns a dict with the providers and the times each encountered
def calcProviders(handler):
    d = dict()
    for line in handler:
        words = line.split()
        t = provider(words[2])
        d[t] = d.get(t,0) +1
    return d

# takes a dict, puts the values first and sorts in reversed, then returns the list with the tuples
def reverseAndSort(d):
    lis = list()
    lis = d.items()
    reversed = list()
    for k,v in lis:
        reversed.append((v,k))
    reversed.sort(reverse=True)
    return reversed

# takes a handler and a string==provider and for each person with this provider it creates a txt file with name the name of the person and content his e-mail
def makeTxt(name, toCompare):
    count=0
    fhandler = open(name)
    for line in fhandler:
        words = line.split()
        if provider(words[2]) == toCompare:
            count +=1
            with open('tests/'+words[0]+' '+words[1]+'.txt','w') as f:
                f.write(words[2]) 
                f.close()
    print 'your ' , count, 'files are ready'

def main():
    name = raw_input("Enter the name of the file: ")
    if len(name) <= 2 : name = 'emails.txt'
    fhandler = open(name)
    providers = dict()
    providers = calcProviders(fhandler)
    #print providers
    top = reverseAndSort(providers)
    for v,k in top:
        print k,v
    makeTxt(name, 'gmail')
    



    

print provider('josphine_villanue@hotmail.com')
main()