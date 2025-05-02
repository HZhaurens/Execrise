'''
题目：复制文件内容到另一个文件

要求：
1. 读取源文件的内容
2. 将内容写入到目标文件
3. 处理可能出现的异常
'''

def copy_file_content(source_file, target_file):
    """
    复制源文件的内容到目标文件
    
    参数:
        source_file (str): 源文件路径
        target_file (str): 目标文件路径
    
    返回:
        bool: 复制成功返回True，否则返回False
    """
    try:
        # 打开源文件读取内容
        with open(source_file, 'r', encoding='utf-8') as source:
            content = source.read()
        
        # 将内容写入目标文件
        with open(target_file, 'w', encoding='utf-8') as target:
            target.write(content)
        
        print(f"文件内容已成功从 '{source_file}' 复制到 '{target_file}'")
        return True
    except FileNotFoundError:
        print(f"错误: 文件 '{source_file}' 不存在")
        return False
    except PermissionError:
        print(f"错误: 没有权限访问文件 '{source_file}' 或 '{target_file}'")
        return False
    except Exception as e:
        print(f"复制文件时发生错误: {e}")
        return False

# 使用缓冲区复制大文件的版本
def copy_large_file(source_file, target_file, buffer_size=4096):
    """
    使用缓冲区复制大文件的内容到目标文件
    
    参数:
        source_file (str): 源文件路径
        target_file (str): 目标文件路径
        buffer_size (int): 缓冲区大小，默认为4KB
    
    返回:
        bool: 复制成功返回True，否则返回False
    """
    try:
        # 打开源文件和目标文件
        with open(source_file, 'r', encoding='utf-8') as source, \
             open(target_file, 'w', encoding='utf-8') as target:
            # 分块读取和写入
            while True:
                buffer = source.read(buffer_size)
                if not buffer:  # 如果读取为空，表示已到文件末尾
                    break
                target.write(buffer)
        
        print(f"大文件内容已成功从 '{source_file}' 复制到 '{target_file}'")
        return True
    except FileNotFoundError:
        print(f"错误: 文件 '{source_file}' 不存在")
        return False
    except PermissionError:
        print(f"错误: 没有权限访问文件 '{source_file}' 或 '{target_file}'")
        return False
    except Exception as e:
        print(f"复制文件时发生错误: {e}")
        return False

# 二进制文件复制版本
def copy_binary_file(source_file, target_file, buffer_size=4096):
    """
    复制二进制文件的内容到目标文件
    
    参数:
        source_file (str): 源文件路径
        target_file (str): 目标文件路径
        buffer_size (int): 缓冲区大小，默认为4KB
    
    返回:
        bool: 复制成功返回True，否则返回False
    """
    try:
        # 使用二进制模式打开文件
        with open(source_file, 'rb') as source, open(target_file, 'wb') as target:
            # 分块读取和写入
            while True:
                buffer = source.read(buffer_size)
                if not buffer:  # 如果读取为空，表示已到文件末尾
                    break
                target.write(buffer)
        
        print(f"二进制文件内容已成功从 '{source_file}' 复制到 '{target_file}'")
        return True
    except FileNotFoundError:
        print(f"错误: 文件 '{source_file}' 不存在")
        return False
    except PermissionError:
        print(f"错误: 没有权限访问文件 '{source_file}' 或 '{target_file}'")
        return False
    except Exception as e:
        print(f"复制文件时发生错误: {e}")
        return False

# 示例用法
if __name__ == "__main__":
    # 创建一个源文件
    source_file = "source.txt"
    with open(source_file, 'w', encoding='utf-8') as f:
        f.write("这是源文件的第一行\n")
        f.write("这是源文件的第二行\n")
        f.write("这是源文件的第三行\n")
        f.write("这是源文件的内容，将被复制到目标文件。")
    
    # 定义目标文件
    target_file = "target.txt"
    
    # 复制文件内容
    success = copy_file_content(source_file, target_file)
    
    # 如果复制成功，显示目标文件内容
    if success:
        print("\n目标文件内容:")
        try:
            with open(target_file, 'r', encoding='utf-8') as f:
                print(f.read())
        except Exception as e:
            print(f"读取目标文件时发生错误: {e}")