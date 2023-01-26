
import model_sum as summ
import model_div
import model_mult
import model_sub

def main():
    do = True
while do:
    value_model = int(input('выберите значение: '))

    if value_model == 3:
        do_it = summ

    elif value_model == 1:
        do_it = model_div

    elif value_model == 2:
        do_it = model_mult

    elif value_model == 4:
        do_it = model_sub

    elif value_model == 5:
        do = False
        print("Bye")

    else:
        print("Error")

main()