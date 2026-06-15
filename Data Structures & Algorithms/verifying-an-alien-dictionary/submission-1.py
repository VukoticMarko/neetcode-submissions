class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        order_index = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            word_1, word_2 = words[i], words[i + 1]

            for j in range(len(word_1)):
                if j == len(word_2):
                    return False

                if word_1[j] != word_2[j]:
                    if order_index[word_1[j]] > order_index[word_2[j]]:
                        return False
                    break
        return True