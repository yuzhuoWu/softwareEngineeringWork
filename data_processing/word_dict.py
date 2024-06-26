import pickle

# 读取pickle二进制文件
def load_pickle(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data

# 构建新的词典和词向量矩阵
def get_vocab(filepath1, filepath2):
    word_vocab = set()
    corpora = [filepath1, filepath2]
    for corpus in corpora:
        for data in corpus:
            for i in range(1, 4):
                for j in range(len(data[i][0])):
                    word_vocab.add(data[i][0][j])
                for j in range(len(data[i][1])):
                    word_vocab.add(data[i][1][j])
    print(len(word_vocab))
    return word_vocab

# 构建初步词典
def vocab_processing(filepath1, filepath2, save_path):
    with open(filepath1, 'r') as f:
        total_data1 = set(eval(f.read()))
        f.close()
    with open(filepath2, 'r') as f:
        total_data2 = eval(f.read())
        f.close()

    word_set = get_vocab(total_data2, total_data2)
    with open(save_path, 'w') as f:
        f.write(str(word_set))
        f.close()

# 获取两个文本数据集中出现的单词的集合，
# 仅返回在第二个数据集中出现过而未在第一个数据集中出现过的单词的集合
def final_vocab_prpcessing(filepath1,filepath2,save_path):
    word_set = set()
    with open(filepath1, 'r') as f:
        total_data1 = set(eval(f.read()))
        f.close()
    with open(filepath2, 'r') as f:
        total_data2 = eval(f.read())
        f.close()
    total_data1 = list(total_data1)
    x1 = get_vocab(total_data2, total_data2)
    # total_data_sort = sorted(x1, key=lambda x: (x[0], x[1]))
    for i in x1:
        if i in total_data1:
            continue
        else:
            word_set.add(i)
    print(len(total_data1))
    print(len(word_set))
    f = open(save_path, "w")
    f.write(str(word_set))
    f.close()

if __name__ == "__main__":
    # 获取staqc的词语集合
    python_hnn = './data/python_hnn_data_teacher.txt'
    python_staqc = './data/staqc/python_staqc_data.txt'
    python_word_dict = './data/word_dict/python_word_vocab_dict.txt'

    sql_hnn = './data/sql_hnn_data_teacher.txt'
    sql_staqc = './data/staqc/sql_staqc_data.txt'
    sql_word_dict = './data/word_dict/sql_word_vocab_dict.txt'

    # 获取最后大语料的词语集合的词语集合
    new_python_staqc = '../hnn_process/ulabel_data/staqc/python_staqc_unlabled_data.txt'
    new_python_large ='../hnn_process/ulabel_data/large_corpus/multiple/python_large_multiple_unlable.txt'
    large_word_dict_python = '../hnn_process/ulabel_data/python_word_dict.txt'

    new_sql_staqc = './ulabel_data/staqc/sql_staqc_unlabled_data.txt'
    new_sql_large = './ulabel_data/large_corpus/multiple/sql_large_multiple_unlable.txt'
    large_word_dict_sql = './ulabel_data/sql_word_dict.txt'

    final_vocab_processing(sql_word_dict, new_sql_large, large_word_dict_sql)
