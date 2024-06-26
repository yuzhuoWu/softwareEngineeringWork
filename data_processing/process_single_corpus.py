import pickle
from collections import Counter


#读取pickle二进制文件
def load_pickle(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f, encoding='iso-8859-1')
    return data

#计算一个列表中指定元素的出现次数
def split_data(total_data, qids):
    return total_data.coutnt(qids)

#把语料中的单候选和多候选分隔开
def data_staqc_prpcessing(filepath,single_path,mutiple_path):
    with open(filepath,'r')as f:
        total_data = eval(f.read())
        f.close()
    qids = []
    for i in range(0, len(total_data)):
        qids.append(total_data[i][0][0])
    result = Counter(qids)

    total_data_single = []
    total_data_multiple = []
    for i in range(0, len(total_data)):
        if(result[total_data[i][0][0]]==1):
            total_data_single.append(total_data[i])
        else:
            total_data_multiple.append(total_data[i])
    f = open(single_path, "w")
    f.write(str(total_data_single))
    f.close()
    f = open(mutiple_path, "w")
    f.write(str(total_data_multiple))
    f.close()

#将数据转换为带有标签的形式并保存
def single_unlabeled_to_labeled(input_path, output_path):
    total_data = load_pickle(input_path)
    labels = [[data[0], 1] for data in total_data]
    # 按照问题ID和标签进行排序
    total_data_sort = sorted(labels, key=lambda x: (x[0], x[1]))
    # 将有标签的数据保存到文件
    with open(output_path, "w") as f:
        f.write(str(total_data_sort))


if __name__ == "__main__":
    staqc_python_path = './ulabel_data/python_staqc_qid2index_blocks_unlabeled.txt'
    staqc_python_single_save = './ulabel_data/staqc/single/python_staqc_single.txt'
    staqc_python_multiple_save = './ulabel_data/staqc/multiple/python_staqc_multiple.txt'
    data_staqc_processing(staqc_python_path, staqc_python_single_save, staqc_python_multiple_save)

    staqc_sql_path = './ulabel_data/sql_staqc_qid2index_blocks_unlabeled.txt'
    staqc_sql_single_save = './ulabel_data/staqc/single/sql_staqc_single.txt'
    staqc_sql_multiple_save = './ulabel_data/staqc/multiple/sql_staqc_multiple.txt'
    data_staqc_processing(staqc_sql_path, staqc_sql_single_save, staqc_sql_multiple_save)

    large_python_path = './ulabel_data/python_codedb_qid2index_blocks_unlabeled.pickle'
    large_python_single_save = './ulabel_data/large_corpus/single/python_large_single.pickle'
    large_python_multiple_save = './ulabel_data/large_corpus/multiple/python_large_multiple.pickle'
    data_large_processing(large_python_path, large_python_single_save, large_python_multiple_save)

    large_sql_path = './ulabel_data/sql_codedb_qid2index_blocks_unlabeled.pickle'
    large_sql_single_save = './ulabel_data/large_corpus/single/sql_large_single.pickle'
    large_sql_multiple_save = './ulabel_data/large_corpus/multiple/sql_large_multiple.pickle'
    data_large_processing(large_sql_path, large_sql_single_save, large_sql_multiple_save)

    large_sql_single_label_save = './ulabel_data/large_corpus/single/sql_large_single_label.txt'
    large_python_single_label_save = './ulabel_data/large_corpus/single/python_large_single_label.txt'
    single_unlabeled_to_labeled(large_sql_single_save, large_sql_single_label_save)
    single_unlabeled_to_labeled(large_python_single_save, large_python_single_label_save)
