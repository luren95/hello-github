# demo.py —— 一个最小的 Python 例子
# 说明：GitHub 只负责存放这个文件，真正运行它的是你电脑上的 Python

def greet(name):
    return f"你好，{name}！欢迎来到 GitHub。"

if __name__ == "__main__":
    print(greet("世界"))
    for i in range(1, 4):
        print(f"这是第 {i} 行输出")
