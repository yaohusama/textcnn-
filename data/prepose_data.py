pos=[]
neg=[]
import pandas as pd
with open("waimai.txt",encoding="utf-8") as f:
    data=f.read().split("\n")
    for item in data:
        if "label,review" in item:
            continue
        if len(item)==0:
            continue
        if item[0]=="0":
            neg.append(item[2:])
        else:
            pos.append(item[2:])
print(len(neg))
print(len(pos))
f1=open("waimai.train.txt","w+",encoding="utf-8")
f2=open("waimai.test.txt","w+",encoding="utf-8")
f3=open("waimai.val.txt","w+",encoding="utf-8")
for item in neg[:int(len(neg)*0.7)]:
    f1.write("0\t"+item+"\n")
for item in pos[:int(len(pos)*0.7)]:
    f1.write("1\t"+item+"\n")
for item in neg[int(len(neg)*0.7):int(len(neg)*0.9)]:
    f2.write("0\t"+item+"\n")
for item in pos[int(len(pos)*0.7):int(len(pos)*0.9)]:
    f2.write("1\t"+item+"\n")
for item in neg[int(len(neg)*0.9):]:
    f3.write("0\t"+item+"\n")
for item in pos[int(len(pos)*0.9):]:
    f3.write("1\t"+item+"\n")
f1.close()
f2.close()
f3.close()
'''data=pd.read_csv("online_shopping_10_cats.csv",encoding="utf-8")
cat_dict={}
cat_neg={}
for item in zip(data["cat"],data["label"],data["review"]):
    # print(item)
    if item[0] not in cat_dict and item[1]==1:
        cat_dict[item[0]]=[item[2]]
    elif item[0] not in cat_neg and item[1]==0:
            cat_neg[item[0]]=[item[2]]
    elif item[0] in cat_dict and item[1]==1:
        cat_dict[item[0]].append(item[2])
    elif item[0] in cat_dict and item[1]==0:
        cat_neg[item[0]].append(item[2])

print(cat_dict)
print(cat_neg)
f1=open("train.txt","w+",encoding="utf-8")
f2=open("val.txt","w+",encoding="utf-8")
f3=open("test.txt","w+",encoding="utf-8")
train= {}
text= {}
val= {}
for item in zip(data["cat"],data["label"],data["review"]):
    if item[1]==0:
        if 0 not in train.keys():
            train[0]=[]
        if len(train[0])<cat_neg[item[0]]*0.6:
            train[0].append(item[2])
        elif len(train[0])<cat
f1.close()
f2.close()
f3.close()
'''