import pickle
import numpy as np
from gensim.models import KeyedVectors


# 将词向量文件保存成bin文件
def trans_bin(path1, path2):
    # 加载词向量文件（非二进制格式）
    wv_from_text = KeyedVectors.load_word2vec_format(path1, binary=False)
    # 进行必要的预处理和转换
    wv_from_text.init_sims(replace=True)
    # 保存转换后的词向量为二进制文件
    wv_from_text.save(path2)

# 构建新的词典和词向量矩阵
def get_new_dict(type_vec_path, type_word_path, final_vec_path, final_word_path):
    # 加载转换文件
    model = KeyedVectors.load(type_vec_path, mmap='r')
    # 读取包含特定语料词的文件并转换为列表形式
    with open(type_word_path, 'r') as f:
        total_word = eval(f.read())
        f.close()
    # 输出词向量
    word_dict = ['PAD', 'SOS', 'EOS', 'UNK']  # 其中0 PAD_ID, 1 SOS_ID, 2 EOS_ID, 3 UNK_ID

    fail_word = []
    rng = np.random.RandomState(None)
    pad_embedding = np.zeros(shape=(1, 300)).squeeze()
    unk_embedding = rng.uniform(-0.25, 0.25, size=(1, 300)).squeeze()
    sos_embedding = rng.uniform(-0.25, 0.25, size=(1, 300)).squeeze()
    eos_embedding = rng.uniform(-0.25, 0.25, size=(1, 300)).squeeze()
    word_vectors = [pad_embedding, sos_embedding, eos_embedding, unk_embedding]

    for word in total_word:
        try:
            word_vectors.append(model.wv[word])  # 加载词向量
            word_dict.append(word)
        except:
            fail_word.append(word)

    word_vectors = np.array(word_vectors)
    word_dict = dict(map(reversed, enumerate(word_dict)))

    with open(final_vec_path, 'wb') as file:
        pickle.dump(word_vectors, file)

    with open(final_word_path, 'wb') as file:
        pickle.dump(word_dict, file)

    print("完成")


# 得到词在词典中的位置
def get_index(type, text, word_dict):
    location = []
    if type == 'code':
        location.append(1)
        len_c = len(text)
        if len_c + 1 < 350:
            if len_c == 1 and text[0] == '-1000':
                location.append(2)
            else:
                for i in range(0, len_c):
                    index = word_dict.get(text[i], word_dict['UNK'])#获取词在词典中的位置，如果不存在则返回UNK的位置
                    location.append(index)
                location.append(2)
        else:
            for i in range(0, 348):
                index = word_dict.get(text[i], word_dict['UNK'])
                location.append(index)
            location.append(2)
    else:
        if len(text) == 0:
            location.append(0)
        elif text[0] == '-10000':
            location.append(0)
        else:
            for i in range(0, len(text)):
                index = word_dict.get(text[i], word_dict['UNK'])
                location.append(index)

    return location


# 将训练、测试、验证语料序列化
# 查询：25 上下文：100 代码：350
def serialization(word_dict_path, type_path, final_type_path):
    with open(word_dict_path, 'rb') as f:
        word_dict = pickle.load(f)

    with open(type_path, 'r') as f:
        corpus = eval(f.read())
        f.close()

    total_data = []

    for i in range(len(corpus)):
        qid = corpus[i][0]# 查询ID
        # 处理Si和Si+1的词列表
        Si_word_list = get_index('text', corpus[i][1][0], word_dict)
        Si1_word_list = get_index('text', corpus[i][1][1], word_dict)
        # 处理代码的词列表
        tokenized_code = get_index('code', corpus[i][2][0], word_dict)
        # 处理查询的词列表
        query_word_list = get_index('text', corpus[i][3], word_dict)

        block_length = 4
        label = 0

        if (len(Si_word_list) > 100):
            Si_word_list = Si_word_list[:100]
        else:
            for k in range(0, 100 - len(Si_word_list)):
                Si_word_list.append(0)

        if (len(Si1_word_list) > 100):
            Si1_word_list = Si1_word_list[:100]
        else:
            for k in range(0, 100 - len(Si1_word_list)):
                Si1_word_list.append(0)

        if (len(tokenized_code) < 350):
            for k in range(0, 350 - len(tokenized_code)):
                tokenized_code.append(0)
        else:
            tokenized_code = tokenized_code[:350]

        if (len(query_word_list) > 25):
            query_word_list = query_word_list[:25]
        else:
            for k in range(0, 25 - len(query_word_list)):
                query_word_list.append(0)

        one_data = [qid, [Si_word_list, Si1_word_list], [tokenized_code], query_word_list, block_length, label]
        total_data.append(one_data)

    with open(final_type_path, 'wb') as file:
        pickle.dump(total_data, file)


if __name__ == '__main__':
    # Python Struc2Vec 文件路径
    ps_path_bin = '../hnn_process/embeddings/10_10/python_struc2vec.bin'
    # SQL Struc2Vec 文件路径
    sql_path_bin = '../hnn_process/embeddings/10_8_embeddings/sql_struc2vec.bin'

    # 最初基于Staqc的词典和词向量
    python_word_path = '../hnn_process/data/word_dict/python_word_vocab_dict.txt'
    python_word_vec_path = '../hnn_process/embeddings/python/python_word_vocab_final.pkl'
    python_word_dict_path = '../hnn_process/embeddings/python/python_word_dict_final.pkl'

    sql_word_path = '../hnn_process/data/word_dict/sql_word_vocab_dict.txt'
    sql_word_vec_path = '../hnn_process/embeddings/sql/sql_word_vocab_final.pkl'
    sql_word_dict_path = '../hnn_process/embeddings/sql/sql_word_dict_final.pkl'

    # 最后打标签的语料
    new_sql_staqc = '../hnn_process/ulabel_data/staqc/sql_staqc_unlabled_data.txt'
    new_sql_large = '../hnn_process/ulabel_data/large_corpus/multiple/sql_large_multiple_unlable.txt'
    large_word_dict_sql = '../hnn_process/ulabel_data/sql_word_dict.txt'
    sql_final_word_vec_path = '../hnn_process/ulabel_data/large_corpus/sql_word_vocab_final.pkl'
    sqlfinal_word_dict_path = '../hnn_process/ulabel_data/large_corpus/sql_word_dict_final.pkl'

    staqc_sql_f = '../hnn_process/ulabel_data/staqc/seri_sql_staqc_unlabled_data.pkl'
    large_sql_f = '../hnn_process/ulabel_data/large_corpus/multiple/seri_ql_large_multiple_unlable.pkl'

    new_python_staqc = '../hnn_process/ulabel_data/staqc/python_staqc_unlabled_data.txt'
    new_python_large = '../hnn_process/ulabel_data/large_corpus/multiple/python_large_multiple_unlable.txt'
    final_word_dict_python = '../hnn_process/ulabel_data/python_word_dict.txt'
    large_word_dict_python = '../hnn_process/ulabel_data/python_word_dict.txt'
    python_final_word_vec_path = '../hnn_process/ulabel_data/large_corpus/python_word_vocab_final.pkl'
    python_final_word_dict_path = '../hnn_process/ulabel_data/large_corpus/python_word_dict_final.pkl'

    print('序列化完毕')
