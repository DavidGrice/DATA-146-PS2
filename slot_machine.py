import random

def slot_machine():
    symbols = ['lemon','grapes','sevens','oranges','gold bar','cherries', 'cash']*4+ ['WIN']*2
    result = [random.choice(symbols) for i in range(4)]
    if(result[0] == result[1] and result[1] == result[2] and result[2] == result[3]):
        if('WIN' in result):
          return 'Win 50X!'
        return 'Win 20X!'
    elif(result.count('WIN') > 2):
        return 'Win 10X!'
    elif(result[0] == result[3] and result[1] == result[2]):
        if('WIN' in result):
          return 'Win 5X!'
        return 'Win 2X!'
    return 'Lose!'
    

def slot_machine_2():
    symbols = ['lemon','grapes','sevens','oranges','gold bar','cherries', 'cash']*4+ ['WIN']*2
    result = [symbols[random.randint(0,29)]]*4
    if(result[0] == result[1] and result[1] == result[2] and result[2] == result[3]):
        if('WIN' in result):
          return 'Win 50X!'
        return 'Win 20X!'
    elif(result.count('WIN') > 2):
        return 'Win 10X!'
    elif(result[0] == result[3] and result[1] == result[2]):
        if('WIN' in result):
          return 'Win 5X!'
        return 'Win 2X!'
    return 'Lose!'


def marbles():
  marbs = ['R']*15 + ['B']*10
  result = [random.choice(marbs), random.choice(marbs), random.choice(marbs), random.choice(marbs)]
  if('R' not in result):
    return 'Win all blue!'
  elif result == ['B','B','R','R']:
    return 'Win second combo!'
  
  
def test_probs(repetitions, func):
    result = [func() for i in range(repetitions)]
    return {k:result.count(k) for k in result}
    

print(test_probs(10000, marbles))
print(test_probs(100000, slot_machine))