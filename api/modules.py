import random
from random import random, randint

def fraud(service):
    fraud_score = random()
    return fraud_score


def classifier(service):
    some_dict = {1: 'консультация', 2: 'лечение', 3: 'стационар', 4: 'диагностика', 5: 'лаборатория'}
    ran = randint(1, 5)
    out_dict = {'service_class': ran, 'service_name': some_dict[ran]}    
    return out_dict
