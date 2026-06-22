from collections import defaultdict
from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):

        # No solution if target word does not exist
        if endWord not in wordList:
            return 0

        pattern_to_words = defaultdict(list)

        # Build pattern map
        for word in wordList:

            for i in range(len(word)):

                pattern = (
                    word[:i] +
                    "*" +
                    word[i + 1:]
                )

                pattern_to_words[pattern].append(word)

        queue = deque([beginWord])
        visited = set([beginWord])

        transformation_length = 1

        while queue:

            level_size = len(queue)

            # Process one BFS level
            for _ in range(level_size):

                current_word = queue.popleft()

                # Reached target
                if current_word == endWord:
                    return transformation_length

                # Generate all patterns
                for i in range(len(current_word)):

                    pattern = (
                        current_word[:i] +
                        "*" +
                        current_word[i + 1:]
                    )

                    # Visit all neighboring words
                    for next_word in pattern_to_words[pattern]:

                        if next_word not in visited:

                            visited.add(next_word)
                            queue.append(next_word)

            transformation_length += 1

        return 0

        f