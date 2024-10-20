class Graph:
    def __init__(self, adjacency_list):
        """

        :rtype: object
        """
        self.adjacency_list = adjacency_list

    def depth_first_search(self, root):
        stack = [root]
        while stack:
            curr = stack.pop()
            print(curr, end=" ")
            for ele in self.adjacency_list[curr]:
                stack.append(ele)

    def depth_first_search_recursively(self, root):
        print(root, end=" ")
        for ele in self.adjacency_list[root]:
            self.depth_first_search_recursively(ele)

    def breadth_first_search(self, root):
        queue = [root]
        while queue:
            curr = queue.pop(0)
            print(curr, end=" ")
            for ele in self.adjacency_list[curr]:
                queue.append(ele)


adjacency_list = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}
graph = Graph(adjacency_list)
# graph.depth_first_search('a')
# print('\r')
# print('-----------------------------------------')
# graph.depth_first_search_recursively('a')
#
# print('\r')
# print('-----------------------------------------')
graph.breadth_first_search('a')
