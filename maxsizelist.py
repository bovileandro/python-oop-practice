class MaxSizeList(object):
    def __init__(self, value):
        self.list = []
        self.max_size = value

    def push(self, word):
        self.list.append(word)
        if len(self.list) > self.max_size:
            self.list.pop(0)

    def get_list(self):
        return self.list



m = MaxSizeList(3)

m.push("hey")
m.push("hi")
m.push("let\'s")
m.push("go")

print(m.get_list())
