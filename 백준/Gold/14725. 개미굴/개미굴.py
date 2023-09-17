import sys
input = sys.stdin.readline


class Trie:
    def __init__(self):
        self.root = {}

    def add(self, foods):
        cur = self.root

        for food in foods:
            if food not in cur:
                cur[food] = {}
            cur = cur[food]
        cur[0] = True

    def travel(self, level, cur):
        if 0 in cur:
            return
        cur_child = sorted(cur)

        for ch in cur_child:
            print("--" * level + ch)
            self.travel(level + 1, cur[ch])


n = int(input())
trie = Trie()
for i in range(n):
    k, *t = list(input().split())
    trie.add(t)

trie.travel(0, trie.root)
