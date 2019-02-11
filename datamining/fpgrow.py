import operator
import copy
import sys
sys.stdout = open("output.txt" , "w")
NoOfObjects = 200
support = 1000
INF = 1000000
Vec = []
transact = []
dict1 = {}
class Sort(object):
    def __init__(self , x , y):
        self.x = x
        self.y = y
class StoreNode(object):
    def __init__(self , val):
        self.L = []
        self.ct = 0
        self.val = val
    
class TrieNode(object):
    
    def __init__(self, num , counter = 1):
        self.num = num
        self.children = []
        self.list_finished = False
        self.parent = None
        self.counter = counter
    

def add(root, trans):
   
    node = root
    for num in trans:
        found_in_child = False
        for child in node.children:
            if child.num == num:
                child.counter += 1
                node = child
                found_in_child = True
                break

        if not found_in_child:
            new_node = TrieNode(num)
            node.children.append(new_node)
            new_node.parent = node
            node = new_node
            Vec[num].L.append(node)

    node.list_finished = True

def add1(root, trans , inc):
    
    node = root
    for num in trans:
        found_in_child = False
        for child in node.children:
            if child.num == num:
                child.counter += inc
                node = child
                found_in_child = True
                break

        if not found_in_child:
            
            new_node = TrieNode(num , inc)
            node.children.append(new_node)
            new_node.parent = node
            node = new_node
            #Vec[num].L.append(node)
    # if(inc == 4):
    #     print(trans , node.num , node.parent.list_finished)
    node.list_finished = True

def is_bit_set(num, bit):
    return num & (1 << bit) > 0

def all_subsets(curr):
    s = []
    for i in curr:
        s.append(i[0])
    ln = len(s)
    for i in range(1 , 1 << (ln )):
        subset = [s[bit] for bit in range(len(s)) if is_bit_set(i, bit)]
        min1 = INF
        for bit in range(len(s)):
            if(is_bit_set(i , bit)):
                var = int(curr[bit][1])
                min1 = min(min1 , var)
        #print(subset)
        str1 = ','.join(str(e) for e in subset)
        #print("whack " ,str1 , min1)
        if(dict1.get(str1) == None):
            dict1[str1] = min1
        else:
            dict1[str1] += min1

        


def PrintTrie(root , curr):
    #print(root.list_finished , root.num ,curr)
    if(len(root.children) == 0):
        if(len(curr) > 0):
            #print(curr)
            all_subsets(curr)
    node = root
    for child in node.children:
        # if(child.counter < support):
        #     tem = TrieNode(0)
        #     tem.list_finished = True
        #     PrintTrie(tem , curr)
        #     continue
        var = copy.deepcopy(curr)
        var.append((child.num , child.counter))
        PrintTrie(child , var)
    
    return

def GetSuffix(root , number):
    Store = []
    root1 = TrieNode(INF)
    if(Vec[number].ct < support):
        return
    for neighbour in Vec[number].L:
        temp = []
        cnt = neighbour.counter
        while(neighbour.num < INF):
            neighbour = neighbour.parent
            if(neighbour.parent == None):
                break
            if(neighbour.counter >= support):
                temp.append((neighbour.num , cnt))

        if(len(temp) > 0):
            temp.reverse()
            temp1 = []
            for i in temp:
                temp1.append(i[0])
            var = int(temp[0][1])
            #print(temp1 , var)
            add1(root1 , temp1 , var)
            Store.append(temp)

    if(len(Store) > 0):
        print(number)
        dict1.clear()
        PrintTrie(root1 , [])
        for key in dict1:
            if(dict1[key] >= support):
                print("{",key,",",number, "}: " , dict1[key])

        print("\n")
        #print(Store)
    return Store


if __name__ == "__main__":
    file = open('mushroom.txt' , "r")
    tempL1 = file.readlines()
    for i in range(NoOfObjects):
        temp = StoreNode(i + 1)
        Vec.append(temp)

    for line in tempL1:
        temp = line.split(',')
        
        temp[len(temp) - 1] = temp[len(temp) - 1][:-1]
        #print(temp)
        var = []
        for iter1 in temp:
            l1 = int(iter1[:])
            Vec[l1].ct += 1
            var.append(l1)
        transact.append(var)

    root = TrieNode(INF)
    for i in transact:
        temp = []
        for j in i:
            ins = Sort(j , Vec[j].ct)
            #print(j , Vec[j].ct)
            temp.append(ins)
        temp.sort(key = operator.attrgetter('y') , reverse = True)
        rem = []
        for j in temp:
            rem.append(j.x)
            #print(j.x , j.y)
        #print(rem)
        add(root , rem)

keep = []    
for i in range(NoOfObjects):
    if(Vec[i].ct >= support):
        keep.append((i , Vec[i].ct))

keep.sort(key = lambda x: x[1])
#print(keep)
#GetSuffix(root , 2)
for i in keep:
    GetSuffix(root , i[0])