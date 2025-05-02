# 28_将字符串中首字母大写.py

def capitalize_first_letter(string):
    """将字符串中每个单词的首字母大写
    
    Args:
        string: 输入的字符串
        
    Returns:
        处理后的字符串
    """
    # 使用title()方法将每个单词的首字母大写
    return string.title()

# 测试
text = input("请输入一个句子: ")
result = capitalize_first_letter(text)
print(f"处理后的结果: {result}")