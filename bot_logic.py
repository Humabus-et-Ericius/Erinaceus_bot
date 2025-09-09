import random 

def gen_pass(request):
    symb = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"   

    passwrd =  ""   
    for i in range(request):    
        passwrd += random.choice(symb) 

    return("Ваш пароль: " + passwrd)

def d4():
    symb_d4 = random.randint(1, 4)
    return symb_d4 

def d6():
    symb_d6 = random.randint(1, 6)
    return symb_d6 

def d8():
    symb_d8 = random.randint(1, 8)
    return symb_d8 

def d10():
    symb_d10 = random.randint(1, 10)
    return symb_d10 

def d12():
    symb_d12 = random.randint(1, 12)
    return symb_d12

def d20():
    symb_d20 = random.randint(1, 20)
    return symb_d20 

def d100():
    symb_d100 = random.randint(1, 100)
    return symb_d100 
