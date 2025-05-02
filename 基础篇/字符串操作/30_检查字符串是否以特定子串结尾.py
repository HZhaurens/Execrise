# 30_检查字符串是否以特定子串结尾.py

def ends_with(string, suffix):
    """检查字符串是否以特定子串结尾
    
    Args:
        string: 输入的字符串
        suffix: 要检查的后缀
        
    Returns:
        如果字符串以指定后缀结尾，返回True，否则返回False
    """
    return string.endswith(suffix)

# 测试
text = input("请输入一个字符串: ")
suffix = input("请输入要检查的后缀: ")
result = ends_with(text, suffix)
print(f"字符串是否以'{suffix}'结尾: {result}")