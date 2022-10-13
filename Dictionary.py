#DIctionary
#Empty Dictionary
d= {}
print(d)
print(type(d))


#Create a dictionary
d={'usn':'01','name':'alen','branch':'ise'}
print (d)

#Traversing of dict
d={'usn':'01','name':'alen','branch':'ise'} 
for key in d:
    print(key,":",d[key])

#Adding elements inside the dict

d={1:10,2:20,3:30}
d[4]=40
print(d)

#Update element inside the dictionary 
d={'usn':'01','name':'alen','branch':'ise'}
print(len(d))#lenghth

d['name']= 'bob'
print(d)


#old_dic.update (new_dictionary)
d1= {1:10,2:20,3:30}
d2={4:40,5:50}
d1.update(d2)
print(d1)

#difference or -
s1 ={10,20,30,40,50}
s2= {40,50,60,70}
print(s1.difference(s2))
print(s1-s2)