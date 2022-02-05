from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import numpy as np
import os
import codecs
from sklearn.cluster import MiniBatchKMeans
from sklearn import metrics
# from nltk.tokenize import word_tokenize
import smart_open
import gensim

# data = open("data/sentence.txt",encoding="utf-8").read().split("\n")
res_x=[]
text_li=[]
def read_corpus(file_name, tokens_only=False):
    with smart_open.open(file_name, encoding='utf-8') as f:
        for i, line in enumerate(f):
            tokens = gensim.utils.simple_preprocess(line)
            # if tokens:
            #     yield tokens
            # else:
            text_li.append(line)
            if tokens:
                res_x.append(gensim.models.doc2vec.TaggedDocument(tokens, [i]))
            else:
                res_x.append(gensim.models.doc2vec.TaggedDocument(line, [i]))
train_file="data/sentence.txt"
read_corpus(train_file)
# print(res_x)
train_corpus=res_x
max_epochs = 1
vec_size = 300
alpha = 0.025
t_len=len(res_x)
model = Doc2Vec(vector_size=vec_size,
                alpha=alpha,
                min_alpha=0.00025,
                min_count=1,
                dm=1)

model.build_vocab(train_corpus)

for epoch in range(max_epochs):
    print('iteration {0}'.format(epoch))
    model.train(train_corpus,
                total_examples=model.corpus_count,
                epochs=model.epochs)
    model.alpha -= 0.0002
    model.min_alpha = model.alpha

model.save("d2v.model")
print("Model Saved")

# -------------Lets play with it----------------------
from gensim.models.doc2vec import Doc2Vec

model = Doc2Vec.load("d2v.model")
print(t_len)
res=[]
for i in range(t_len):
    res.append(list(model.docvecs[i]))
silhouette_score_li = [[],[]]
cluster_num_begin = 2
cluster_num_end = 20
cluster_num_step = 1
for cluster_num in range(cluster_num_begin, cluster_num_end, cluster_num_step):
    silhouette_score_li[0].append(cluster_num)
    print("cluster_num: %d" % cluster_num, end='\t')
    km = MiniBatchKMeans(n_clusters=cluster_num,
                        init='k-means++',
                        verbose=0)
    km.fit(res)
    Silhouette = metrics.silhouette_score(res, km.labels_, sample_size=1000)
    silhouette_score_li[1].append(Silhouette)
    print("Silhouette Coefficient: %0.3f" % Silhouette)
for cluster_num, Silhouette_Coefficient in zip(silhouette_score_li[0], silhouette_score_li[1]):
    print("cluster num = %d" % cluster_num, "Silhouette Coefficient=%.2f" % Silhouette_Coefficient)
cluster_num = 7
outfile = open("data/聚类评测结果.txt", 'wb')
print("cluster_num: %d" % cluster_num)
km = MiniBatchKMeans(n_clusters=cluster_num,
                    init='k-means++',
                    verbose=0)
km.fit(res)
for i in range(cluster_num):
    for text, label in zip(text_li, km.labels_):
        if label == i:
            out_str = u'%s\t%s\n' % (label, text)
            outfile.write(out_str.encode('utf-8', 'ignore'))
outfile.close()
