'''
题目：将用户输入的内容写入文件

要求：
1. 接收用户输入的内容
2. 将用户输入的内容写入到文本文件中
3. 提示写入成功
'''

def write_user_input_to_file(file_path):
    """
    将用户输入的内容写入到文件
    
    参数:
        file_path (str): 要写入的文件路径
    
    返回:
        bool: 写入成功返回True，否则返回False
    """
    try:
        # 提示用户输入内容
        print("请输入要保存到文件的内容（输入'END'单独一行表示结束输入）:")
        
        # 收集用户输入的所有行
        lines = []
        while True:
            line = input()
            if line == 'END':
                break
            lines.append(line)
        
        # 将内容写入文件
        with open(file_path, 'w', encoding='utf-8') as file:
            for line in lines:
                file.write(line + '\n')
        
        print(f"内容已成功写入到文件 '{file_path}'")
        return True
    except Exception as e:
        print(f"写入文件时发生错误: {e}")
        return False

# 带有追加模式的版本
def append_user_input_to_file(file_path):
    """
    将用户输入的内容追加到文件末尾
    
    参数:
        file_path (str): 要追加内容的文件路径
    
    返回:
        bool: 追加成功返回True，否则返回False
    """
    try:
        # 提示用户输入内容
        print("请输入要追加到文件的内容（输入'END'单独一行表示结束输入）:")
        
        # 收集用户输入的所有行
        lines = []
        while True:
            line = input()
            if line == 'END':
                break
            lines.append(line)
        
        # 将内容追加到文件（使用'a'模式）
        with open(file_path, 'a', encoding='utf-8') as file:
            for line in lines:
                file.write(line + '\n')
        
        print(f"内容已成功追加到文件 '{file_path}'")
        return True
    except Exception as e:
        print(f"追加到文件时发生错误: {e}")
        return False

# 示例用法
if __name__ == "__main__":
    # 定义文件路径
    file_path = "user_input.txt"
    
    # 写入模式示例
    print("=== 写入模式示例 ===")
    write_user_input_to_file(file_path)
    
    # 读取并显示文件内容
    print("\n文件当前内容:")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            print(f.read())
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
    
    # 追加模式示例
    print("\n=== 追加模式示例 ===")
    append_user_input_to_file(file_path)
    
    # 再次读取并显示文件内容
    print("\n更新后的文件内容:")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            print(f.read())
    except Exception as e:
        print(f"读取文件时发生错误: {e}")