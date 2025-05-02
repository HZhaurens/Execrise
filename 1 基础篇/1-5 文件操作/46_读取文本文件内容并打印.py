'''
题目：读取文本文件内容并打印

要求：
1. 读取指定文本文件的内容
2. 将文件内容打印到控制台
'''

def read_and_print_file(file_path):
    """
    读取文本文件内容并打印到控制台
    
    参数:
        file_path (str): 文件路径
    
    返回:
        None
    """
    try:
        # 使用with语句自动处理文件关闭
        with open(file_path, 'r', encoding='utf-8') as file:
            # 读取文件全部内容
            content = file.read()
            # 打印文件内容
            print("文件内容:")
            print(content)
    except FileNotFoundError:
        print(f"错误: 文件 '{file_path}' 不存在")
    except Exception as e:
        print(f"读取文件时发生错误: {e}")

# 示例用法
if __name__ == "__main__":
    # 创建一个示例文件
    example_file = "example.txt"
    
    # 写入一些内容到示例文件
    with open(example_file, 'w', encoding='utf-8') as f:
        f.write("这是一个示例文件。\n")
        f.write("用于测试文件读取功能。\n")
        f.write("Python文件操作很有用！")
    
    # 读取并打印文件内容
    read_and_print_file(example_file)