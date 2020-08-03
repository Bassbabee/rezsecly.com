import random
import string

def choice_code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for i in range(size))

def create_shortcode(instance, size=6):
    new_code = choice_code_generator(size=size)
    URLclass = instance.__class__
    querry_set = URLclass.objects.filter(shortcode=new_code).exists()
    if querry_set:
        return create_shortcode(size=size)
    return new_code
