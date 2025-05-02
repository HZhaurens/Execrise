# 34_检查字符串是否只包含字母.py

def is_alpha(string):
    """检查字符串是否只包含字母
    
    Args:
        string: 输入的字符串
        
    Returns:
        如果字符串只包含字母，返回True，否则返回False
    """
    return string.isalpha()

# 测试
text = input("请输入一个字符串: ")
result = is_alpha(text)
print(f"字符串是否只包含字母: {result}")