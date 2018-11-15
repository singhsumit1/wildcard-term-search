import os 
import random
import bisect
import math
import operator 
import json 
import xlrd 
import operator 
import re
import nltk

class Ele :
    def __init__(self,num):
        self.left_chlid = None
        self.right_child = None
        self.content = num 
    def new_ele(self,num):
        self.content = num    


class Node :
    def __init__(self) :
        self.isleaf = True
        self.parent = None
        self.chunk = []	
        self.order = 4
        self.next =  None
        self.pre =  None
    def isroot(self):
        if self.parent is None :
            return True
        else :
            return False	
    def isfull(self):	
        if	len(self.chunk) == self.order-1 : # isful
            return True
        else :
            return False
    
    def split_leaf_root(self):
        t = self.order - 1
        t1 = int(math.ceil((t-1)/2))
        node_1 = Node()
        node_2 = Node()
        node_1.next = node_2
        node_2.pre = node_1
        node_2.next = self.next
        if self.pre != None : 
            self.pre.next = node_1
        node_1.isleaf = True
        node_2.isleaf = True
        node_1.chunk = self.chunk[0:t1] 	
        node_2.chunk = self.chunk[t1:t] 
        node_r = Node()
        node_r.isleaf = False
        node_r.chunk.append(self.chunk[t1])
        node_r.chunk[0].left_child = node_1
        node_r.chunk[0].right_child = node_2
        node_1.parent = node_r
        node_2.parent = node_r
        return node_r
                                               # isful
    
    def split_leaf(self):
        t = self.order - 1
        t1 = int(math.ceil((t-1)/2))
        node_1 = Node()
        node_2 = Node()
        node_1.next = node_2
        node_2.next = self.next
        node_2.pre = node_1
        if self.pre != None : 
            self.pre.next = node_1
        
        node_1.isleaf = True
        node_2.isleaf = True
        node_1.chunk = self.chunk[0:t1] 	
        node_2.chunk = self.chunk[t1:t] 
        node_1.parent = self.parent
        node_2.parent = self.parent
        l=[]
        i = -1
        for i in self.parent.chunk :
            l.append(i.content)
        index = bisect.bisect(l,self.chunk[t1].content)
		
        
        
        
        self.parent.chunk.insert(index,self.chunk[t1])	
        
        
        self.parent.chunk[index].left_child = node_1
        self.parent.chunk[index].right_child = node_2		
        if index == 0 :
            self.parent.chunk[(index+1)].left_child = node_2
        elif index == len(self.parent.chunk)-1 :
            self.parent.chunk[(index-1)].right_child = node_1
        else :
            self.parent.chunk[(index+1)].left_child = node_2
            self.parent.chunk[(index-1)].right_child = node_1
        return self.parent
           
    def split_non_leaf(self) :
        t = self.order - 1
        t1 = int(math.ceil(t/2)-1)
        node_1 = Node()
        node_2 = Node()
        node_1.isleaf = False
        node_2.isleaf = False
        
        node_1.chunk = self.chunk[0:t1] 	
        node_2.chunk = self.chunk[t1+1:t] 
        node_1.parent = self.parent
        node_2.parent = self.parent
        i=0
        l = []
        for i in self.parent.chunk :
            l.append(i.content)                                                           # isful
        index = bisect.bisect(l,self.chunk[t1].content)
        self.parent.chunk.insert(index,self.chunk[t1])		
        self.parent.chunk[index].left_child = node_1
        self.parent.chunk[index].right_child = node_2
        if index == 0 :
            self.parent.chunk[(index+1)].left_child = node_2
        elif index == len(self.parent.chunk)-1 :
            self.parent.chunk[(index-1)].right_child = node_1
        else :
            self.parent.chunk[(index+1)].left_child = node_2
            self.parent.chunk[(index-1)].right_child = node_1
        for i in node_1.chunk :
            i.left_child.parent = node_1
            i.right_child.parent = node_1
        for i in node_2.chunk :
            i.left_child.parent = node_2
            i.right_child.parent = node_2
        return self.parent
  
    def split_non_leaf_root(self)  :
        t = self.order - 1
        t1 = int(math.ceil(t/2)-1)
        node_1 = Node()
        node_2 = Node()
        node_p = Node()
        node_1.isleaf = False
        node_2.isleaf = False
        node_p.isleaf = False
        node_1.chunk = self.chunk[0:t1] 	
        node_2.chunk = self.chunk[t1+1:t] 
        node_1.parent = node_p
        node_2.parent = node_p
        self.chunk[t1].left_child = node_1
        self.chunk[t1].right_child = node_2		
        node_p.chunk.append(self.chunk[t1])
        for i in node_1.chunk :
            i.left_child.parent = node_1
            i.right_child.parent = node_1
        for i in node_2.chunk :
            i.left_child.parent = node_2
            i.right_child.parent = node_2
        return node_p
	    
    def add_obj(self,obj)	:
        l = []
        for i in self.chunk :
            l.append(i.content)
        index = bisect.bisect(l,obj.content)
        self.chunk.insert(index,obj)
		
		
		
    def insert(self,num_obj):
        	
        
        
        if self.chunk is None   :                    # empty leaf  node
            
            self.chunk.append(num_obj)
            
        elif self.isleaf and self.parent is None:    #leaf root node  
            
            self.add_obj(num_obj)   
                     
        elif self.isleaf and not(self.isroot()):    #leaf non root
            if self.isfull() :
               
                
                new_self = self.split_leaf()
              
                
                
                   
                flag = 0
                for i in range(len(new_self.chunk)) :
                    if num_obj.content < new_self.chunk[i].content :
                        flag = 1
                        break
                if flag == 1:
                    new_self.chunk[i].left_child.insert(num_obj)
                else :
                    new_self.chunk[i].right_child.insert(num_obj)
            else :
                self.add_obj(num_obj)
            			
			

        elif not(self.isleaf) :    # non leaf no   	de   non leaf non root
            if self.isfull() :
                new_self = self.split_non_leaf()
                flag = 0
                for i in range(len(new_self.chunk)):
                    if num_obj.content < new_self.chunk[i].content :
                        flag = 1
                        break
                if flag == 1:
                    new_self.chunk[i].left_child.insert(num_obj)
                else :
                    new_self.chunk[i].right_child.insert(num_obj)
               
            else :
                flag = 0
                for i in range(len(self.chunk)):
                    if num_obj.content < self.chunk[i].content:
                        flag = 1
                        break
               
                if flag == 1:
                    self.chunk[i].left_child.insert(num_obj)
                    
                else :
                    self.chunk[i].right_child.insert(num_obj)
                    
        
    def q_print(self,q1,q2,final_list) :
        l=[]
        for i in self.chunk :
            if i.content >= q1 and i.content <= q2 :
                final_list = final_list.append(i.content)
                l.append(i.content)	
            else :
                break
        
    
		
    
    def q_trevel(self,q1,q2,final_list) :
        if self.isleaf :
            
            self.q_print(q1,q2,final_list)
        else :
            for i in self.chunk :
                i.left_child.q_trevel(q1,q2,final_list)	
            i.right_child.q_trevel(q1,q2,final_list)
   
   
			

####### code for dictionary for dand prakria file#######
			

			

# Python code to remove duplicate elements 
def d_remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 



flag = 1
f_list = list()
diction = dict()
sol = list()# use for adding boolean query 
  
# To open Workbook 
wb = xlrd.open_workbook('Dand_Prakriya.xlsx') 
sheet = wb.sheet_by_index(0) 
list_of_list = list()  # it is list of document list associated with each word
# For row 0 and column 0 
#print(sheet.cell_value(0, 0))
#print(sheet.nrows , sheet.ncols)
n_row = 2275 #sheet.nrows
for n in range(n_row) :
    i = 0
    str = sheet.cell_value(n,0)
    s=re.split(',|;|\s|\(|\)|\.|\[|\]|-|:|\"|\*',str)
    s= list(filter(None , s)) 
    for st in s :
        
        s[i] = st
       # print(s[i])
        i = i + 1
    for rm in s :
   
        if rm == 'whom' or rm == 'what' or rm == 'to' or rm == '"' or rm == 'is' or rm == 'am' or rm == 'are' or rm == 'a' or rm == 'the' or rm == 'The' or rm == 'Are' or rm == 'A' or rm == 'of' or rm == 'to' or rm == 'and':
            s.remove(rm)  # for remove general word
        else :
            f_list.append(rm)   # list of   all tokens  		
    list_of_list.append(s)


f_list = d_remove(f_list)
f_list.sort()


     
for w in f_list :
    k=0
    t_list = []
    for l in list_of_list :
        if w in l :
            t_list.append(k)  # t_list is posting list for w
            k = k + 1
        else :
            k = k + 1
    diction[w] = t_list # diction is dictionary [ word to list of document]
#print(diction)

			#######code for implimenting b + tree ##########
root = Node()

for i in f_list:
    
    if root.isleaf :
        if root.isfull() :
            root = root.split_leaf_root()
    else :
        if root.isfull() :  
        		root = root.split_non_leaf_root()
                      
    
        
    root.insert(Ele( i ))
        	
ifh = open('query_eng.txt','r')

qf = ifh.read() 
qm = qf.split()
q = qm[0]
ifh.close()
#q = input('Enter the query')
l = len(q)
q1 = q[0:l-1]
q2 = q1 + 'z'
final_list = []
root.q_trevel(q1,q2,final_list)

document_list = dict()
for i in final_list :
    document_list[i] = diction[i] 
ofh = open('OUT_ENGLISH.txt','w')  #outputfile
#print(document_list)
json.dump(document_list,ofh)
ofh.close()

    
