# 33_检查字符串是否只包含数字.py

def is_digit(string):
    """检查字符串是否只包含数字
    
    Args:
        string: 输入的字符串
        
    Returns:
        如果字符串只包含数字，返回True，否则返回False
    """
    return string.isdigit()

# 测试
text = input("请输入一个字符串: ")
result = is_digit(text)
print(f"字符串是否只包含数字: {result}")