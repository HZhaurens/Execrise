# 27_统计字符串中单词的数量.py

def count_words(string):
    """统计字符串中单词的数量
    
    Args:
        string: 输入的字符串
        
    Returns:
        单词的数量
    """
    # 去除首尾空格并按空格分割
    words = string.strip().split()
    return len(words)

# 测试
text = input("请输入一个句子: ")
result = count_words(text)
print(f"单词的数量: {result}")