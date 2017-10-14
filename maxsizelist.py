class MaxSizeList(object):
    def __init__(self, value):
        self.list_ = []
        self.max_size = value

    def push(self, word):
        self.list_.append(word)
        if len(self.list_) > self.max_size:
            self.list_.pop(0)

    def get_list(self):
        return self.list_



m = MaxSizeList(3)
m.push("hey")
m.push("hi")
m.push("let\'s")
m.push("go")
print(m.get_list())

n = MaxSizeList(1)
n.push("hey")
n.push("hi")
n.push("let\'s")
n.push("go")
print(n.get_list())
