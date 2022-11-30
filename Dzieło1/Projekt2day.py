from datetime import datetime
from functools import singledispatch
import tkinter
import tkinter.messagebox


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Czy chcesz przejść dalej?')
        self.main_window.geometry('700x500')

        self.my_button = tkinter.Button(self.main_window, text="Chyba tak",
                                        command=lambda: self.do_something("Postaraj sie!"))
        self.my_button2 = tkinter.Button(self.main_window, text="TAK TAK ODWAL SIĘ !",
                                         command=lambda: self.do_something2("SZUKAJ SEKRETNEGO PRZYCISKU"))
        self.my_button3 = tkinter.Button(self.main_window, text="Owszem miłościwy Panie!",
                                         command=self.main_window.destroy)

        self.my_button.pack()
        self.my_button2.pack()
        self.my_button3.pack()

        tkinter.mainloop()

    def do_something(self, text1):
        tkinter.messagebox.showinfo(f'{text1}', 'Postaraj się!')

    def do_something2(self, text2):
        tkinter.messagebox.showinfo(f'{text2}', 'Nie tędy droga milordzie!')


my_gui = MyGui()


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Ogłoszenie')
        self.main_window.geometry('700x500')
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.my_button = tkinter.Button(self.main_window, text="Wchodzę na własną odpowiedzialność",
                                        command=self.main_window.destroy)
        self.label1 = tkinter.Label(self.top_frame, text="Witaj przywoływaczu!")
        self.label2 = tkinter.Label(self.top_frame,
                                    text="To jest program który gryzie i szarpie jak internet naszego wykładowcy.")
        self.label3 = tkinter.Label(self.top_frame,
                                    text="Jeśli widzisz ten tekst to znaczy że masz szanse oglądać wybitne dzieło programowania ")

        self.my_button.pack()
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')
        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    def do_something(self, param):
        pass


my_gui = MyGui()


@singledispatch
def report(value):
    return f'Dzień, godzina i sekunda objawienia mocy obliczeniowej: {value}'


print(report(datetime.now()))

print('Statystyka zdobytych goli na mundialu Katar 2022 wszystkich drużyn')


class Goal:
    """Statystyka zdobytych goli na mundialu Katar 2022 wszystkich drużyn"""

    def __init__(self, Country, Goals, Games):
        self.Country = Country
        self.Goals = Goals
        self.Games = Games

    def __repr__(self):
        return f'Goal({self.Country!r}, {self.Goals}, {self.Games})'


Goal = [Goal('Anglia', 9, 3),
        Goal('Katar', 1, 3),
        Goal('Hiszpania', 8, 2),
        Goal('Szwajcaria', 1, 2),
        Goal('Francja', 6, 3),
        Goal('Kanada', 1, 2),
        Goal('Holandia', 5, 3),
        Goal('Belgia', 1, 2),
        Goal('Senegal', 5, 3),
        Goal('Kostaryka', 1, 2),
        Goal('Argentyna', 5, 3),
        Goal('Portugalia', 5, 2),
        Goal('Dania', 1, 3),
        Goal('Walia', 1, 3),
        Goal('Iran', 4, 3),
        Goal('Korea_pld', 2, 2),
        Goal('Chorwacja', 4, 2),
        Goal('Japonia', 2, 2),
        Goal('Ekwador', 4, 3),
        Goal('Niemcy', 2, 2),
        Goal('Arabia_Saudyjska', 3, 3),
        Goal('Maroko', 2, 2),
        Goal('Australia', 3, 3),
        Goal('Polska', 2, 3),
        Goal('Kamerun', 3, 2),
        Goal('Meksyk', 2, 3),
        Goal('USA', 2, 3),
        Goal('Serbia', 3, 2),
        ]

print('Zbiór bałaganu', repr(Goal))
Goal.sort(key=lambda x: x.Country)
Goal.sort(key=lambda x: x.Goals)
Goal.sort(key=lambda x: x.Games)
Goal.sort(key=lambda x: (x.Goals, x.Games))
print('Rosnąco liczba strzelonych bramek->rozegrane_mecze', Goal)
Goal.sort(key=lambda x: (-x.Goals, x.Games))
print('Malejąco liczba strzelonych bramek->rozegrane mecze', Goal)


