'''
题目：统计文本文件的行数

要求：
1. 读取指定文本文件
2. 统计文件的总行数
3. 打印统计结果
'''

def count_lines(file_path):
    """
    统计文本文件的行数
    
    参数:
        file_path (str): 文件路径
    
    返回:
        int: 文件的行数，如果文件不存在则返回-1
    """
    try:
        # 使用with语句自动处理文件关闭
        with open(file_path, 'r', encoding='utf-8') as file:
            # 使用readlines()方法读取所有行，然后计算长度
            # 也可以使用len(file.readlines())，但下面的方法更节省内存
            line_count = 0
            for _ in file:
                line_count += 1
            return line_count
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
        f.write("这是第一行\n")
        f.write("这是第二行\n")
        f.write("这是第三行\n")
        f.write("这是第四行\n")
        f.write("这是第五行")
    
    # 统计并打印行数
    lines = count_lines(example_file)
    if lines >= 0:
        print(f"文件 '{example_file}' 共有 {lines} 行")