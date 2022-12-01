numbers = [93, 86, 11, 68, 70]
numbers.sort()
print(numbers)

class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'


tools = [Tool('młotek', 3.5),
         Tool('piła tarczowa', 40),
         Tool('poziomica', 3),
         Tool('dłuto', 0.25),
         Tool('szlifierka', 3),
         ]
saw = (5, 'piła tarczowa')
hammer = (40, 'młot')
drill = (5, 'wiertarka')

# assert not (hammer < saw)
# assert drill[0] == saw[0]
# assert drill[1] < saw[1]
# assert drill < saw



print('nieposortowane', repr(tools))
tools.sort(key=lambda x:x.name)
tools.sort(key=lambda x:x.weight, reverse=True)
# tools.sort(key=lambda x: (x.weight, x.name), reverse=True)
print('posortowane', tools)



# print('nieposortowane', repr(tools))
# # tools.sort(key=lambda x:x.name)
# # tools.sort(key=lambda x:x.weight)
# # tools.sort(key=lambda x: (-x.weight, x.name))
# print('posortowane', tools)


# places = ['dom', 'praca', 'Nowy Jork', 'Paryż']
# places.sort()
# print('Uwzględniona wielkość liter:', places)
# places.sort(key=lambda x:x.lower())
# print('Nieuwzględniona wielkość liter:', places)
