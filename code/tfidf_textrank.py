# -*- coding: utf-8 -*-
import jieba
# from es.es_io import  *
from jieba import analyse
import  pickle

jieba.load_userdict("./dict/SogouLabDic.txt")
jieba.load_userdict("./dict/dict_baidu_utf8.txt")
jieba.load_userdict("./dict/dict_pangu.txt")
jieba.load_userdict("./dict/dict_sougou_utf8.txt")
jieba.load_userdict("./dict/dict_tencent_utf8.txt")

def get_data(content,max_words):
    stopwords = {}.fromkeys([ line.rstrip() for line in open('./Stopword.txt','r',encoding='utf8') ])

    result =[]
    seg = jieba.cut(content)
    for i in seg:
        if i not in stopwords:
            result.append(i)

    content_full = " ".join(result)
    tfidf = analyse.extract_tags
    keywords = tfidf(content_full, allowPOS=('ns', 'nr', 'nt', 'nz', 'nl', 'n', 'vn', 'vd', 'vg', 'v', 'vf', 'a', 'an', 'i'))
    # print(keywords)
    result_keyword = []
    for keyword in keywords:
        result_keyword.append(keyword)


    keywords_full = " ".join(result_keyword)
    # 考虑了相邻词的语义关系、基于图排序的关键词提取算法TextRank
    keywords_full_result = jieba.analyse.textrank(keywords_full, topK=max_words, withWeight=True)

    keywords={}
    for i in keywords_full_result:
        keywords[i[0]] = i[1]
    # pickle.dump(keywords,open("data/keywords.pkl"))
    return keywords


# 测试生成的关键词
# if __name__=='__main__':
#     content ='单车 共享 过退 刘小明 吹风会 押金 例行 提问 倒闭 运营 国务院 部长 停止 透露 投入 回答 记者 企业 \
# 单车 停放 治理 成都 \
# 单车 政协委员 提案 人大代表 共享 建议 关注 \
# 建议 提案 提出 \
# 车辆 刘小明 建议 单车 业态 提出 管理 停放 提案 共享 说好 投放 优化 用户 委员 监管 加强 希望 指出 代表 \
# 单车 共享 刘小明 运送 累计 透露 投入 企业 '
#     wc = get_data(content)
#     print(wc)


    #     # 更新数据
    #     actions = []
    #     update = {
    #         'is_word_cloud_handle': 1,
    #         'word_cloud': wc
    #     }
    #     event_id = news['_id']
    #     action = update_action("news_event" , "news_event" , event_id, update)
    #     actions.append(action)
    #     helpers.bulk(es, actions)







