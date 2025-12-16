# Random Password
oooooo
import random
import string

pass_len = 12

charValues = string.ascii_letters + string.digits + string.punctuation

password = " "
for i in range(pass_len):
    password += random.choice(charValues)


print("Your random password is:", password)


# Output:

'''
Your random password is:  ^Tg?!U#pk9x5
Your random password is:  GJosVo88Nsx9
Your random password is:  {T+w_[C"t!TR
Your random password is:  &{#FG_p+4vQ%                        
Your random password is:  s0\`@Q>RE`!6
Your random password is:  }C|&Y{,GAH(D
                                                 

'''
