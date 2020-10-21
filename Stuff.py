import tensorFlow as ts

def cur():
    return object


class Link(object):

    def __init__(self, item, nxt):
        self.item = item
        self.next = nxt

        pass

    def set_next(self, nxt):
        self.next = Link(nxt)

        pass

    def get_item(self):
        return self.item


pass


class LinkedList(object):

    def __init__(self, head):
        self.head = Link()
        self.curr = self.head
        self.size = 0

        pass

    def add(self, obj):
        self.curr = Link(obj)
        self.size += 1

        pass

    def remove(self, loc):
        cur: Link = self.head
        for i in range(loc-1):
            cur = cur.next
        cur.set_next(cur.next.next)

        pass

    pass
