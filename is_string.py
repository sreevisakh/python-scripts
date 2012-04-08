
strings=[]
queries=[]


def read_input():
    string_no = int(raw_input())
    for i in range(string_no):
        strings.append(raw_input())
    
    query_no = int(raw_input())
    for i in range(query_no):
        queries.append(int(raw_input()))

read_input()
counter=0
stringlist=[]
for string in strings:
    for i in range(0,len(string)+1):
        for j in range(i+1,len(string)+1):
            res = string[i:j]
            if res not in stringlist:
                stringlist.append(res)

stringlist = sorted(list(set(stringlist)))

for query in queries:
    try:
        result = stringlist[query-1]
        print result
    except IndexError :
        print 'INVALID'

