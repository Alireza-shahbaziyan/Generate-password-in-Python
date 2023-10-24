import string
import secrets

# make a alphabet
alphabet = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
#-------------------------MAKE A PASSWORD-------------------------------------------------  
pasword = ''.join(secrets.choice(alphabet) for i in range(16))
""" 
or you can write pasword = ''.join(random.choice(alphabet) for i in range(16))
* of course remember to << import random >>
"""

print(pasword)