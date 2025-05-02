'''
题目：统计文本文件中特定单词的出现次数

要求：
1. 读取指定文本文件
2. 统计特定单词在文件中出现的次数
3. 打印统计结果
'''

def count_word_occurrences(file_path, target_word):
    """
    统计文本文件中特定单词的出现次数
    
    参数:
        file_path (str): 文件路径
        target_word (str): 要统计的目标单词
    
    返回:
        int: 目标单词在文件中出现的次数，如果文件不存在则返回-1
    """
    try:
        # 使用with语句自动处理文件关闭
        with open(file_path, 'r', encoding='utf-8') as file:
            # 读取文件全部内容
            content = file.read()
            
            # 将目标单词转换为小写以进行不区分大小写的匹配
            content_lower = content.lower()
            target_word_lower = target_word.lower()
            
            # 统计单词出现次数
            # 这里使用简单的方法，可能会统计到单词的一部分
            # 例如，搜索"is"会匹配到"this"中的一部分
            # 更精确的方法是使用正则表达式或分词
            word_count = content_lower.count(target_word_lower)
            
            return word_count
    except FileNotFoundError:
        print(f"错误: 文件 '{file_path}' 不存在")
        return -1
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return -1

# 更精确的统计方法（使用正则表达式）
def count_word_occurrences_regex(file_path, target_word):
    """
    使用正则表达式统计文本文件中特定单词的出现次数（更精确）
    
    参数:
        file_path (str): 文件路径
        target_word (str): 要统计的目标单词
    
    返回:
        int: 目标单词在文件中出现的次数，如果文件不存在则返回-1
    """
    import re
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # 使用正则表达式查找完整单词
            # \b表示单词边界
            pattern = r'\b' + re.escape(target_word) + r'\b'
            matches = re.findall(pattern, content, re.IGNORECASE)
            return len(matches)
    except FileNotFoundError:
        print(f"错误: 文件 '{file_path}' 不存在")
        return -1
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return -1

# 示例用法
if __name__ == "__main__":
    # 创建一个示例文件
    example_file = "example.txt"
    
    # 写入一些内容到示例文件
    with open(example_file, 'w', encoding='utf-8') as f:
        f.write("Python是一种流行的编程语言。\n")
        f.write("Python简单易学，功能强大。\n")
        f.write("使用Python可以开发各种应用程序。\n")
        f.write("我喜欢学习Python编程。\n")
        f.write("Python的语法非常优雅。")
    
    # 要统计的单词
    word = "Python"
    
    # 使用简单方法统计
    count = count_word_occurrences(example_file, word)
    if count >= 0:
        print(f"使用简单方法统计: 单词 '{word}' 在文件中出现了 {count} 次")
    
    # 使用正则表达式方法统计（更精确）
    count_regex = count_word_occurrences_regex(example_file, word)
    if count_regex >= 0:
        print(f"使用正则表达式统计: 单词 '{word}' 在文件中出现了 {count_regex} 次")