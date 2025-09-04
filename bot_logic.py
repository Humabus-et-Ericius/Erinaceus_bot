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

