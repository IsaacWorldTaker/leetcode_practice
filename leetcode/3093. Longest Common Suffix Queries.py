from typing import List


class TrieNode:
    def __init__(self, index=float('inf'), word_len=float('inf')):
        self.children = [None] * 26
        self.is_end = False
        self.index = index
        self.word_len = word_len


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()

        answer = [0]*len(wordsQuery)
        for i, word in enumerate(wordsContainer):
            current_node = root
            for ch in word[::-1]:
                if len(word) < root.word_len:
                    root.word_len = len(word)
                    root.index = i
                index = ord(ch)-ord('a')
                if current_node.children[index] is None:
                    new_node = TrieNode()
                    current_node.children[index] = new_node
                current_node = current_node.children[index]
                if len(word) < current_node.word_len:
                    current_node.word_len = len(word)
                    current_node.index = i
                elif len(word) == current_node.word_len:
                    current_node.index = min(current_node.index, i)
            current_node.is_end = True

        for j, query in enumerate(wordsQuery):
            current_node = root
            min_index = current_node.index
            for i, ch in enumerate(query[::-1]):
                index = ord(ch)-ord('a')
                if current_node.children[index] is None:
                    break
                current_node = current_node.children[index]
                min_index = current_node.index

            answer[j] = min_index
        return answer
        # class Solution:
        #     def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        #         indices = {}
        #         suffix_len = {}
        #         answer = [0]*len(wordsQuery)
        #         for j, suffix in enumerate(wordsQuery):
        #             longest = 0
        #             for i, word in enumerate(wordsContainer):
        #                 common = 0
        #                 for ch in range(-1, -1*(len(suffix)+1), -1):
        #                     if -1*ch > len(word) or suffix[ch] != word[ch]:
        #                         break
        #                     else:
        #                         common += 1
        #                 if common > longest:
        #                     longest = common
        #                     suffix_len[suffix] = len(word)
        #                     indices[suffix] = i
        #                     answer[j] = i
        #                 elif common == longest:
        #                     if len(word) < suffix_len.get(suffix, float('inf')):
        #                         suffix_len[suffix] = len(word)
        #                         indices[suffix] = i
        #                         answer[j] = i
        #         return answer


solution = Solution()
print(solution.stringIndices(["a", "b"], ["a", "b"]))
print(solution.stringIndices(["jfmjjma", "daamjj", "jgamdjj", "gamjaj", "afgjjg", "ddfma", "adggf", "gfaafdmfdj", "ammfdj", "fgdfdjja", "mfgmagfm", "fffdjfggfg", "mdjmf", "mmaja", "ajjmgmfg"], ["djmmjgmfmm", "fmaafmafj", "agdgajmgd", "dgmafmafj",
      "dgjfmf", "djdmjffmj", "faafmg", "dmmmammfdj", "jmajafdafd", "djmjffgdd", "fggfgfaj", "dajgjfdm", "mfdmafdm", "mgffgjgdm", "jjadjdmjja", "adfgd", "gjajj", "ggdmdjdm", "gjgmgfffa", "gjaajjm", "dgjfmdjmmj", "dddmj", "mfmgfdgaf", "ffafjj", "jdmgf"]))
print(solution.stringIndices(["abcd", "bcd", "xbcd"], ["cd", "bcd", "xyz"]))
print(solution.stringIndices(
    ["abcdefgh", "poiuygh", "ghghgh"], ["gh", "acbfgh", "acbfegh"]))
