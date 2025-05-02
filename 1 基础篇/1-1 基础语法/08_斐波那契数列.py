'''
题目：生成斐波那契数列前n项

描述：编写一个Python程序，生成斐波那契数列的前n项。
斐波那契数列的定义：每一项等于前两项之和，前两项为0和1。
数列：0, 1, 1, 2, 3, 5, 8, 13, 21, ...
'''

# 解决方案
def fibonacci_sequence(n):
    """
    生成斐波那契数列的前n项
    
    参数:
        n (int): 需要生成的项数
    
    返回:
        list: 包含斐波那契数列前n项的列表
    """
    # 处理特殊情况
    if n <= 0:
        return []
    
    if n == 1:
        return [0]
    
    if n == 2:
        return [0, 1]
    
    # 初始化数列的前两项
    fib_sequence = [0, 1]
    
    # 生成剩余的项
    for i in range(2, n):
        # 每一项等于前两项之和
        next_num = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_num)
    
    return fib_sequence

# 递归方式计算斐波那契数列的第n项（注意：效率较低，仅用于演示）
def fibonacci_recursive(n):
    """
    使用递归方式计算斐波那契数列的第n项
    
    参数:
        n (int): 项的索引（从0开始）
    
    返回:
        int: 斐波那契数列的第n项
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# 示例输出
if __name__ == "__main__":
    try:
        # 从用户获取输入
        num = int(input("请输入要生成的斐波那契数列项数: "))
        
        # 检查输入是否为正整数
        if num <= 0:
            print("请输入正整数!")
        else:
            # 生成并显示斐波那契数列
            fib_seq = fibonacci_sequence(num)
            print(f"斐波那契数列的前{num}项:")
            print(fib_seq)
            
            # 演示递归方式计算第10项（如果用户输入足够大）
            if num > 10:
                print(f"\n使用递归方式计算的第10项: {fibonacci_recursive(10)}")
                print("注意：递归方式计算大项数时效率较低")
    except ValueError:
        print("请输入有效的整数!")