# softwareEngineeringWork
软件工程实习——实现完美编程、规范代码
20211120124 吴昱卓

## 目录
- [一、项目描述](#一项目描述)
- [二、项目结构文件说明](#二项目结构文件说明)
  - [2.1 embeddings_process.py文件](#embeddings_process.py文件)
  - [2.2 getSru2Vec.py文件](#getSru2Vec.py文件)
  - [2.3 process_single_corpus.py文件](#process_single_corpus.py文件)
  - [2.4 python_structured.py文件](#spython_structured.py文件)
  - [2.5 sqlang_structured.py文件](#sqlang_structured.py文件)
  - [2.6 word_dict.py文件](#word_dictpy文件)
- [三、总结](#三总结)

## 一、项目描述
  此项目的python文件是对文本数据进行预测处理，对给出的python文件文件进行代码规范调试，使其更加美观易懂。
## 二、项目结构文件说明
### 结构说明：
```
├── data_preprocessing  
│   └── embaddings_process.py  
│   └── getStru2Vec.py
│   └── process_single_corpus.py
│   └── python_structured.py
│   └── sqlang_structured.py
│   └── word_dirt.py

```
### 文件说明

### embeddings_process.py文件

#### 1. 概述
将词向量文件转换为二进制格式，并从大词典中提取特定于语料的词典，将数据处理成待打标签的形式构建词向量矩阵。

#### 2.类和方法说明
- `trans_bin(word_path,bin_path)`:词向量文件保存成bin文件
- `get_new_dict(type_vec_path,type_word_path,final_vec_path,final_word_path)`:从大词典中获取特定于语料的词典，构建新的词向量矩阵
- `get_index(type,text,word_dict)`:根据词在词典中的位置，获取词的索引。
- `Serialization(word_dict_path,type_path,final_type_path)`:将训练、测试、验证语料进行序列化处理。

---
### getStru2Vec.py文件
#### 1. 概述
获取最终的python解析文本和SQL解析文本，并进行分词操作。

#### 2.类和方法说明


- `multipro_python_query(data_list)`:Python 查询解析方法。
- `multipro_python_code(data_list)`:Python 代码解析方法。
- `multipro_python_context(data_list)`:Python 上下文解析方法。
- `multipro_sqlang_query(data_list)`:SQL查询解析方法。
- `multipro_sqlang_code(data_list)`:SQL代码解析方法。
- `multipro_sqlang_context(data_list)`:SQL上下文解析方法。
- `parse_python(python_list,split_num)`:针对Python语料，调用上述解析函数进行分词处理，并返回分词结果。
- `parse_sqlang(sql_list,split_num)`:针对SQL语料，调用上述解析函数进行分词处理，并返回分词结果。
- `main(lang_type,split_num,source_path,save_path)`:主函数，将两个版本的解析集合到一个函数中，并将处理结果保存到文件中。
- `test(path1,path2)`:测试函数，用于验证读取和保存的数据是否一致。

---
### process_single_corpus.py文件
#### 1. 概述
把语料中的单候选和多候选分隔开。
#### 2. 类和方法说明
- `load_pickle(filename)`：读取pickle二进制文件。
- `split_data(total_data, qids)`：计算一个列表中指定元素出现的次数。
- `data_staqc_prpcessing(filepath,single_path,mutiple_path)`:把语料中的单候选和多候选分隔开，将数据分别保存到不同的文件中。
- ` single_unlabeled_to_labeled(input_path, output_path)`：将数据转换为带有标签的形式并保存

---
### python_structured.py文件
#### 1. 概述
完成解析 Python 代码的功能。
#### 2. 类和方法说明
- `repair_program_io(code):format_io(code)`:修复 Python 程序中的标准输入/输出（I/O）格式。
- `get_vars(ast_root)`：获取变量名。
- `get_vars_heuristics(code`:从 code 字符串中尽可能多地提取变量名。
- `PythonParser(code)`: 解析Python代码，提取代码中的变量名和标记化的代码列表。
- `revert_abbrev(line)`: 缩略词处理，将常见的英语缩写还原为它们的原始形式。
- `get_wordpos(tag)`:获取对应的WordNet词性。
- `process_nl_line(line)`:对句子进行预处理：空格，还原缩写，下划线命名，去括号，去除开头末尾空格等操作。
- `process_sent_word(line)`:对句子进行分词、标记化、词性标注、词形还原和词干提取等操作  
- `filter_all_invachar(line)`：根据正则表达式模式去除句子中的非法字符。
- `filter_part_invachar(line)`:过滤掉Python代码中部分不常用的字符，以减少解析时的错误。
- `python_code_parse(line)`:解析Python代码，提取代码中的标记列表。
- `python_query_parse_parse(line)`:将提供的文本进行标准化和归一化处理,除去所有特殊字符。
- `python_context_parse(line)`:将提供的文本进行标准化和归一化处理,除去部分特殊字符。

---
### sqlang_structured.py文件到这里
#### 1. 概述
完成解析SQL语言的功能。
#### 2. 类和方法说明
-`tokenizeRegex(s)`:使用正则表达式模式将字符串进行分词，返回分词后的结果。
- class` SqlangParser()`:   
   └──`sanitizeSql(sql)`:对输入的SQL语句进行清理和标准化
   └──`parseStrings(self, tok)`:返回SQL语句中所有token的字符串列表。
   └──`renameIdentifiers(self, tok)`:重命名 SQL 语句中的标识符。  
   └──` _hash_(self)`:将 SQL 解析器对象哈希化。  
   └──`_init__(self, sql, regex=False, rename=True)`:初始化。  
   └──`getTokens(parse)`:获取token序列。
   └──` removeWhitespaces(self, tok)`:删除多余空格。  
   └──`identifySubQueries(self, tokenList)`:识别 SQL 表达式中的子查询。  
   └──`identifyLiterals(self, tokenList)`:用于标识 SQL 解析器对象中的不同类型的文本字面量。  
   └──`identifyFunctions(self, tokenList)`:从给定的token列表中识别SQL语句中的函数并设置type类型。  
   └──`identifyTables(self, tokenList)`:标识SQL语句中的表（table）
   └──`__str__(self)`:将SQL语句的tokens列表中的所有token连接成一个字符串。 
   └──`parseSql(self)`:返回SQL语句中所有token的字符串列表。
- `revert_abbrev(line)`:缩略词处理，将常见的英语缩写还原为它们的原始形式。
- `get_wordpos(tag)`:获取词性。
- `process_nl_line(line)`:对句子进行处理预处理：空格，还原缩写，下划线命名，去括号，去除开头末尾空格。  
-` process_sent_word(line)`:对句子进行分词、词性标注、还原和词干提取。
- `filter_all_invachar(line)`：过滤掉SQL代码中不常用的字符，以减少解析时的错误。
- `filter_part_invachar(line)`:过滤掉SQL代码中部分不常用的字符，以减少解析时的错误。
- `sqlang_code_parse(line)`:解析SQL代码并返回代码中的标记列表。
- `sqlang_query_parse(line)`:解析 SQL 查询语句并返回句子中的标记列表。
- `sqlang_context_parse(line)`:解析SQL上下文句子并返回句子中的标记列表。
将提供的文本进行标准化和归一化处理,除去部分特殊字符。
---
### word_dict.py文件
#### 1. 概述
  通过遍历语料库中的数据，将所有单词添加到一个集合中，从而构建词汇表。
#### 2.类和方法说明
- `load_pickle(filename)`：读取pickle二进制文件。
- `get_vocab(filepath1, filepath2)`：根据给定的两个语料库，获取词汇表。
- `vocab_prpcessing(filepath1,filepath2,save_path)`：构建初步词典，从两个文本数据集中获取全部出现过的单词，并将单词保存到文件中。
- `final_vocab_processing`：首先从文件中加载已有的词汇表，然后调用get_vocab()函数获取新的词汇表。将新的词汇表与已有词汇表进行比较，找到新的单词，并将其保存到指定的文件路径中。
---

## 三、总结  
在本次实验中，学习并掌握了规范化代码。并且初步了解了npl项目如何进行文本数据的预处理与分析。

