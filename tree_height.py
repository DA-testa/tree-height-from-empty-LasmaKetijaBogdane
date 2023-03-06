# python3
"""
# python3
Lasma Ketija Bogdane 221RDB404
"""
import sys
import threading
from typing import List

def compute_height(n: int, parents: List[int]) -> int:
    """
    """
    max_height = 0
    if n == 0:
        return max_height
    heights = [0] * n
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            heights[i] = 1
        else:
            if heights[parent] == 0:
                heights[parent] = compute_height(parent, parents)
            heights[i] = heights[parent] + 1
        max_height = max(max_height, heights[i])
    return max_height


def main() -> None:
    """
    """
    file = input("Enter the input filename: ")
    if file.startswith("i"):
        path = "./test/" + file
    elif file.startswith("f"):
        path = "./test/Folder/" + file
    else:
        print("Invalid file type")
        return
    with open(path, "r", encoding="utf-8") as f:
        n = int(f.readline())
        parents = list(map(int, f.readline().split()))

    height = compute_height(n, parents)
    print(height)


if __name__ == '__main__':
    sys.setrecursionlimit(10**7)
    threading.stack_size(2**27)
    thread = threading.Thread(target=main)
    thread.start()
    thread.join()
    main()
