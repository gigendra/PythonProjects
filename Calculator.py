class calcs:

    def menus(self):
        print('______BASIC CALCULATOR________')
        print("""1. ADDITION\n2. SUBTRACTION\n3. MULTIPLICATION\n4. DIVISION\n0. EXIT""")
        a=int(input("enter option: "))
        if a==1:
            o1.adds()
        elif a==2:
            o1.subs()
        elif a==3:
            o1.muls()
        elif a==4:
            o1.divs()
        elif a==0:
            o1.contd()
        else:
            print("invalid option selected,select correct option: \n")
            o1.menus()

    def adds(self):
        print("enter the two real numbers to be added\n")
        a = float(input())
        b = float(input())
        print("a+b=", a + b)
        o1.contd()
    def subs(self):
        print("enter minuend \n")
        a = float(input())
        print("enter subtrahend \n")
        b = float(input())
        print("a-b=", a - b)
        o1.contd()
    def muls(self):
        print("enter two real numbers to be multiplied\n")
        a = float(input())
        b = float(input())
        print("a*b=", a * b)
        o1.contd()
    def divs(self):
        print("enter dividend\n")
        a = float(input())
        try:
            print("enter divisor\n")
            b = float(input())
            if b==0:
                raise Exception
        except Exception:
            print("math error, divisor must be non zero \n")
            print("enter divisor\n")
            b = float(input())
        finally:
            print("a/b=", a / b)
        o1.contd()
    def contd(self):
        a=int(input("""to confirm exit enter 1\nto continue enter 2\n"""))
        if a==1:
            print("exit")
        elif a==2:
            o1.menus()
        else:
            print("invalid option, enter correct option: \n")
            o1.contd()

o1=calcs()
o1.menus()
        