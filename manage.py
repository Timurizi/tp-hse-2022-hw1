class Contact():
    def __init__(self):
        self.database = []
        self.set2 = set()


    def read_txt(self, test):
        with open(test, encoding='utf-8') as f:
            for i in f:
                self.database.append(i.split(','))
            for i in self.database:
                a = i[2]
                i.remove(i[2])
                i.append(a[:-1])
        print(self.database)
        return self.database

    def number_finder(self, number):
        for j in self.database:
            if j[1] == number:
                print(' '.join((j)))


    def mail_finder(self, mail):
        for j in self.database:
            if j[-1] == mail:
                print(' '.join((j)))

    def names_resulter(self, info):
        for x in info.split():
            self.set2.add(x)
        for j in self.database:
            iterset = set()
            for i in j[0].split():
                iterset.add(i)
            if len(iterset.intersection(self.set2)) != 0:
                print(' '.join(j))
        self.set2.clear()


    def rat_finder(self):
        for i in self.database:
            if i[1] == '' or i[-1] == '':
                print(i)

    def edit(self):
        print('Введите номер клиента для изменения данных')
        for i in range(1, len(self.database) + 1):
            print(i, ' '.join(self.database[i-1]))
        id = int(input())
        print('Что вы хотите изменить(ФИО, Телефон, Почта)(Вводить в указанном порядке, регистр не важен)')
        instrument = input()
        print('Введите новое значение')
        if instrument.lower() == 'почта':
            new_mail = input()
            self.database[id-1][-1] = new_mail
        elif instrument.lower() == 'телефон':
            new_number = input()
            self.database[id-1][1] = new_number
        elif instrument.lower() == 'фио':
            new_name = input()
            self.database[id-1][0] = new_name
        print('Изменения приняты')
        print(self.database)









names = Contact()
names.read_txt('Tests.txt')
names.edit()