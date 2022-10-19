# writing a binary file on students
from ast import Break
import pickle
from re import L
from numpy import True_

from traitlets import Int


def write():
    f = open('student.dat', 'wb')
    record = []
    while True:
        rno = int(input('Roll No:'))
        name = input('Name:')
        marks = int(input('Marks:'))
        L = [rno, name, marks]
        record.append(L)
        print(L)

        ch = input("Want to enter more(Y/N):")
        if ch in ['N', 'n']:
            break
        pickle.dump(record, f)
        print("Record added successfully!!!")
        f.close()


def read():
    with open('student.dat', 'rb') as f:
        while True:
            try:
                L=pickle.load(f)
                for i in L:
                    print(i)
            except EOFError:
                break


def read1():
    try:
        with open('student.dat', 'rb') as f:
            L.pickle.load(f)
            for i in L:
                print(i)
    except FileNotFoundError:
        print("Sorry!!File not found")


def append():
    # or we can open in rb+ that is we will read the data and then append
    with open('student.dat', 'rb+') as f:
        record = pickle.load(f)
        print('Append data in a file...')
        while True:
            rno = int(input('Roll No:'))
            name = input('Name:')
            marks = int(input('Marks:'))
            L = [rno, name, marks]
            record.append(L)
            ch = input('Want to enter more(Y/N):')
            if ch in ['N', 'n']:
                break
            f.seek(0)
            pickle.dump(record, f)
            print('Record Appended Successfully!!!')


def search1():
    with open('student.dat', 'rb')as f:
        rno = int(input('Enter roll no which you want to search'))
        while True:
            try:
                L = pickle.load(f)
                for i in L:
                    if rno == i[0]:
                        print(i)
                        break
                else:
                    print('Sorry rollno not exist!!')
            except EOFError:
                break


def search():
    try:
        with open('student.dat', 'rb') as f:
            L = pickle.load(f)
            rno = int(input('Enter roll no which you want to search:'))
            for i in L:
                if rno == i[0]:
                    print(i)
                    break
            else:
                print('Sorry Rollno do not exist!!')
    except FileNotFoundError:
        print('Sorry!!File Not Found...')


def update():
    # or we can open in rb+ that is we will read the data and then append
    with open('student.dat', 'rb+')as f:
        rno = int(input('enter roll no you want to modify:'))
        f.seek(0)
        try:
            while True:
                pos = f.tell()
                s = pickle.load(f)
                for i in s:
                    if i[0] == rno:
                        i[1] = input('Enter New Name')
                        i[2] = int(input('Enter Marks'))
                f.seek(0)
                pickle.dump(s, f)
                break
        except Exception:
            f.close()


def update1():
    try:
        # or we can open in rb+ that is we will read the data and then append
        with open('student.dat', 'rb+')as f:
            L = pickle.load(f)
            for i in L:
                print(i)
                ch = input('Modify (Y/N)')
                if ch in ['y'/'Y']:
                    i[1] = input('Enter New Name:')
                    i[2] = int(input('Enter Marks:'))
            f.seek(0)
            pickle.dump(L, f)
            print('Record Updated Successfully!!!')
    except Exception:
        f.close()


def delete():
    try:
        with open('student.dat', 'rb') as f:
            L = pickle.load(f)
            rno = int(input('Enter Roll no which you want to delete:'))
            with open('student.dat', 'wb') as fl:
                record = []
                for i in L:
                    if rno == i[0]:
                        continue
                    record.append(i)
                pickle.dump(record, fl)
    except FileNotFoundError:
        print('Sorry!!File not found...')


def MainMenu():
    print("1.Write Data")
    print("2.Read Data")
    print("3.Append Data")
    print("4.Search Data")
    print("5.Update Data")
    print("6.Delete Data")
    print("7.Exit...")


while True:
    MainMenu()
    ch = int(input('Enter your choice:'))
    if ch == 1:
        write()
    elif ch == 2:
        read()
    elif ch == 3:
        append()
    elif ch == 4:
        search1()
    elif ch == 5:
        update()
    elif ch == 6:
        delete()
    elif ch == 7:
        print("Exiting the program")
        break
