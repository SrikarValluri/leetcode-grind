class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # first we generate graph
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)

        taken = set()

        def dfs(course):

            if not graph[course]:
                return True

            if course in taken:
                return False

            taken.add(course)

            for pre in graph[course]:
                if not dfs(pre):
                    return False

            graph[course] = []

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
