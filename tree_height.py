# python3
"""
# python3
Lasma Ketija Bogdane 221RDB404
"""
import sys
import threading
from typing import List
def compute_height(_n, parents: List[int]) -> int:
    """
    return
    """
    max_height = 0
    if _n == 0:
        return max_height
    heights = [0] * _n
    for i in range(_n):
        parent = parents[i]
        if parent == -1:
            heights[i] = 1
        else:
            if heights[parent] == 0:
                heights[parent] = compute_height(parent, parents)
            heights[i] = heights[parent] + 1
        max_height = max(max_height, heights[i])
    return max_height
def main():
    """
    return
    """
    file = input("Enter the input filename: ")
    if file.startswith("i"):
        path = "./test/" + file
    elif file.startswith("f"):
        path = "./test/Folder/" + file
    else:
        print("Invalid file type")
        return
    with open(path, "r", encoding="utf-8") as _f:
        _n = int(_f.readline())
        parents = list(map(int, _f.readline().split()))

    sys.setrecursionlimit(10**7)
    threading.stack_size(2**27)
    _t=threading.Thread(target=compute_height, args=(_n, parents))
    _t.start()
    _t.join()

    with open(path, "r", encoding="utf-8") as _f:
        _n = int(_f.readline())
        parents = list(map(int, _f.readline().split()))

    height = compute_height(_n, parents)
    print(height)
    if __name__ == '__main__':
        main()
        print()
# print(numpy.array([1,2,3]))
