sentence=[]
f=open("../data/sentence.txt", "w+", encoding="utf-8")
f2=open("../data/sentence_neg.txt", "w+", encoding="utf-8")
with open("../data/waimai.txt", "r", encoding="utf-8") as f1:
    data=f1.read().split("\n")
    for item in data:
        # print(item)
        if  "label,review" in item or len(item)==0:
            continue
        # sentence.append(item[2:])
        if item[0]=="0":
            f2.write(item[2:]+"\n")
        f.write(item[2:]+"\n")
f.close()
# print(sentence)
# with open("sentence.txt","w",encoding="utf-8") as f:
#     f.write(str(sentence))
# print("done")
