class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Course -> list of prerequisites
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visiting = set()   # Nodes in current DFS path

        def dfs(course: int) -> bool:

            # Cycle detected
            if course in visiting:
                return False

            # Already processed safely (memoized)
            if graph[course] == []:
                return True

            visiting.add(course)

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            visiting.remove(course)

            # Mark as fully processed (memoization)
            graph[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
