1��hotel_review.txt���ݵ�ַ��https://raw.githubusercontent.com/SophonPlus/ChineseNlpCorpus/master/datasets/ChnSentiCorp_htl_all/ChnSentiCorp_htl_all.csv


2����������waimai.txt��Ӧ��https://raw.githubusercontent.com/SophonPlus/ChineseNlpCorpus/master/datasets/waimai_10k/waimai_10k.csv


###��������
pyhanlp==0.1.44
tensorflow==2.0.0
## ��з���
0��>python data/process_data.py�����ݻ���Ϊѵ���������Լ�����֤��������1�����������0��������
1������train_word2vec.pyѵ��������
2������text_train.py��textcnnѵ��
3������text_test.py�жϲ��Լ�׼ȷ�ʡ��ٻ��ʵȡ�
##��ȡ�ؼ��ʻ��ƴ���ͼ
�ȷִʣ���tfidf��textrank���ѡȡ�ؼ��ʣ������ݹؼ��ʵ�Ȩ�ػ��ƴ���ͼ��

>python word_cloud.py

���Ϊdata/output.png���ǻ��ƵĴ���ͼ��data/keyword.pkl���Ǳ����keyword��Ȩ�صĹؼ���

## �۵���ȡ
1��ͨ������䷨��������ȡ��Ҫ�ġ������ṹ�����������ϵ������������ϵ�������ݹؼ������ҵ����ڲ��֣�����ݺ��Ĵ���ȡ�۵㡣
������ȡ������ؼ��ʵĹ۵㣬����������Ҫ�Ĺ�ϵ����ȡ���Ĵ�ƴ�ӳɹ۵㡣ʹ��O(n^2)�ķ����ֱ���ÿ���۵�Ϊ�����жϺ������۵�ʹ��difflib�ľ�����о��࣬�����
������߳��ִ�������ƴ����͸��۵�����ƶȣ������Ƶ���Ϊ����Ĵ���
>python option_extraction/process_to_list.py

ÿһ��Ϊһ�����ۣ�����������д��sentence.txtͬʱ��������������д��sentence_neg.txt
>python option_extraction/main.py

Ĭ�������ļ�Ϊsentence_neg.txt�������޸�Ϊsentence.txt

config.json�ļ���һЩ���ò�����datalen�������۳���Ϊ1000��ȥ������exceptWordList�����ۣ�includeWordList��Ϊ�ؼ��ʣ�
minOptionLen��ӦΪ������С����Ϊ4��minClusterLen��ӦΪ��С������ĿΪ3��freqStrlen��Ӧ�Ҿ������ʱ��ߴ�Ƶ����Ҫ���ڵ���ֵ��
thresholdsΪ[0.2��0.7]������0.2����һ�࣬��Դ���Ľ�����Ը���0.7����һ�࣬�Խ�ʡʱ�䡣


����includeWordList���Ը�Ϊtfidf��textrank��ϵ��㷨��ȡ�Ĺؼ����б�



��֮ʹ��tfidf��textrank��ϵķ����ҳ��ؼ��ʺͶ�ӦȨ�أ����ƴ���ͼ�������ؼ������뵽
����䷨������ȡ�۵�Ĳ��������У�������ҵ�ÿһ��Ĵ����Ӵ�С�����Ч���Ϻá�
����Ҫ����������������Ҫ����opinion_extraction��config.json����ֵ�Ȳ�����

-----------------------------------------------------------

##Ч�����õľ���
���ھ��Ӿ��࣬ʹ��gensim��doc2vec��ֱ��תΪ��������������kmeans���о���ʱ��Ч�����ã�Silhouette Coefficient�ӽ���0��
��Ӧ��������doc2vec_gensim.py��ģ�ͱ��浽��d2v.model
˵���˱�����ǩ�����൱��Ҫ��


###ʹ��tfidf��AF�����㷨
AP�㷨����Ҫ��ȷ���������Ŀ�����ǰ����е����ݵ㶼����Ǳ��������
�ľ������ģ�exemplar��������ͨ���������ʹ�������Ӧ��tf-idf ֵ�����ı�������ʾ���ı�֮���������ͨ�������ı���
�������������Եõ������ͨ��AP�����㷨�õ��۵����������ӹ۵���ɸѡ��������
>python tfidf_ap.py

AP�㷨��Ȼ����Ҫָ�������������������㷨���Ӷȸߣ�����������ʱ����һ�����������ڴ����ݼ��ϱ��ֲ��ѡ�������ÿ�����ӵ���������ʾ��
