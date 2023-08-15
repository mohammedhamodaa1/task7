x = int(input('Input the number: '))
def print_number_of_rows():
    for y in range(x + 1):
        for z in range(1, y + 1):
            print(z, end=' ')
        print()
print_number_of_rows()
# #####################################
num = int(input("Enter number :"))
def sum_num():
    sum1 = 0
    for i in range(1, num + 1):
        sum1 += i
    return sum1
result = sum_num()
print("Sum is :", result)
#########################################
name = input("Enter your name")
def a():
    for i in range(len(name)):
        print(name[:i], end=" ")
        print()
    for v in range(len(name), 0, -1):
        print(name[:v], end=" ")
        print()
a()

####################################
n = input("input a word to revers")
def c():
    print(n[::-1])
c()
############################
def i():
    o = int(input('Enter range'))

    while o>=1:
        print(o, end=" ")
        o +=-1
    print()
i()
#####################################
def k():
    t = int(input('multiples of 5'))
    while t<=50:
        print(t, end=" ")
        t +=5
k()
######################
def main():
    Limit_number = int(input("Enter the limit number: "))
    Max_display_on_screen = int(input("Enter the maximum outputs to display (Max-display-on-screen): "))
    Target_number = int(input("Enter the target number: "))
    count = 0
    current_number = Target_number

    while current_number <= Limit_number and count < Max_display_on_screen:
        print(current_number, end=" ")
        count += 1
        current_number += Target_number

if __name__ == "__main__":
    main()