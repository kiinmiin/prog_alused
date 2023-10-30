"""Function examples."""


def func():
    print("I´m inside the function")

func()
    


def my_name_is(name):
    print("My name is " + name)



def sum_six(num):
    return(num + 6)
    

def sum_numbers(a, b):
    return a + b


def usd_to_eur(dollar):
    eur_amount = dollar * 0.8
    return(eur_amount)
    
    
my_name_is("Mari")
print(usd_to_eur(100))