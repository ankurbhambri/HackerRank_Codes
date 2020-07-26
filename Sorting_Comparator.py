from functools import cmp_to_key

# def Sort(sub_li):
#     return(sorted(sub_li, key = lambda x: x[1]))

# sub_li =[['amy', 100], ['david', 100], ['heraldo', 50], ['aakansha', 75], ['aleksa', 150]]

# print(Sort(sub_li))


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def comparator(a, b):
        if a.score == b.score:
            if a.name > b.name:
                return 1
            else:
                return -1
        else:
            return b.score - a.score

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)