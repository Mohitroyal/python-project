import random
import string
a= random.choice(string.ascii_letters)
b=random.choice(string.digits)
c = random.choice(string.punctuation)
others = random.choices(string.ascii_letters + string.digits + string.punctuation, k=2)
result = [a, b, c] + others
random.shuffle(result)
print("".join(result))

