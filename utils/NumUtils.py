#! -*-coding:utf8-*-

def isRandomId(id):
    if (id % 10 == 2) or (id % 10 == 7):
        return True
    return False


if __name__ == '__main__':
    print isRandomId(27)