# -*- coding: utf-8 -*-
# LeetCode 热题 100 · 中等题
# 208. 实现 Trie (前缀树) (Implement Trie (Prefix Tree)) | 难度: 中等 | 官方分组: 图论
# 题目链接: https://leetcode.cn/problems/implement-trie-prefix-tree/
# 题意: 实现前缀树（插入/查找/前缀查询）
# 考点: Trie 前缀树：节点含 26 叉 children 数组 + isEnd 标志，逐字符走边
# 标签: 设计,字典树,哈希表,字符串
# hello-algo: 第7章 树 · 二叉树
#   https://www.hello-algo.com/chapter_tree/binary_tree/
# 题解来源: @LeetCode-Solution《实现 Trie (前缀树)》(LeetCode 题解)
#   https://leetcode.cn/problems/implement-trie-prefix-tree/solutions/shi-xian-trie-qian-zhui-shu-by-leetcode-ti500/

class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
    
    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None