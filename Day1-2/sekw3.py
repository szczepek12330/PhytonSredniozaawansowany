# names = {
#     'kot' : 'mruczek',
#     'pies' : 'pimpek'
# }
#
# print(names)
# print(list(names.values()))
# print(list(names.keys()))
# print(names.items())
# print(names.popitem())
#
# def my_func(**kwargs):
#     for k,v in kwargs.items():
#         print(f'{k} = {v}')
from collections.abc import MutableMapping

votes = {
    'wydra': 1281,
    'miś polarny': 587,
    'lis': 863,
}

def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name]= 1


# def get_winner(ranks):
#     return next(iter(ranks))
#
# ranks = {}
# populate_ranks(votes, ranks)
# print(ranks)
# winner = get_winner(ranks)
# print(winner)

# def get_winner(ranks):
#     for name,rank in ranks.items():
#         if rank == 1:
#             return name

def get_winner(ranks):
    if not isinstance(ranks,dict):
        if ranks == 1:
            return name

class SortedDict(MutableMapping):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self):
        return len(self.data)

sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = get_winner(sorted_ranks)
print(winner)