# 32_将字符串中的空格替换为连字符.py

def replace_spaces_with_hyphens(string):
    """将字符串中的空格替换为连字符
    
    Args:
        string: 输入的字符串
        
    Returns:
        处理后的字符串
    """
    return string.replace(" ", "-")

# 测试
text = input("请输入一个包含空格的字符串: ")
result = replace_spaces_with_hyphens(text)
print(f"处理后的结果: {result}")