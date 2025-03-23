import random
num=[0,1,2,3,4,5,6,7,8,9]
alph=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
sym=["!","@","#","$","%","&","*"]
ask_len=int(input("Enter the length of password you want to generate "))
ask_num=int(input("Enter the number of digits you want in your password "))
ask_alpha=int(input("Enter the number of alphabets you want in your password "))
ask_sym=int(input("Enter the number of symbols you want in your password "))
k=""
if ask_len==ask_num+ask_alpha+ask_sym:
    for i in range(ask_num):
        k=k+str(random.choice(num))
    for i in range(ask_alpha):
        k=k+random.choice(alph)
    for i in range(ask_sym):
        k=k+random.choice(sym)
else:
    print("Invalid input")
g="".join(random.sample(k,ask_len))
print(F"The strongest password you can have is {g}")
