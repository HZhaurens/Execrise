# 29_检查字符串是否以特定子串开头.py

def starts_with(string, prefix):
    """检查字符串是否以特定子串开头
    
    Args:
        string: 输入的字符串
        prefix: 要检查的前缀
        
    Returns:
        如果字符串以指定前缀开头，返回True，否则返回False
    """
    return string.startswith(prefix)

# 测试
text = input("请输入一个字符串: ")
prefix = input("请输入要检查的前缀: ")
result = starts_with(text, prefix)
print(f"字符串是否以'{prefix}'开头: {result}")