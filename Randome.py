L = [12345,2,.2,52,222222]
K = 2
def function(L,K):
    counter = 0
    for i in range(len(L)): 
        numbers = L[i]
        divide = True
        while divide:
            if numbers < 1:
                divide = False
            digit = int(numbers % 10)
            if digit == K:
                counter += 1
            numbers /= 10
    return counter
            
                
            
#print(function(L,K))
import random
class Cards(object):
    def __init__(self,number):
        self.number = number
        
    def scramble(self):
        print('hi')
        self.number = random.randint(1,14)

        
class PlayCards(Cards):
    def __init__(self,number,color,symbol):
        Cards.__init__(self,number)
        Cards.scramble(self)
        self.color = color
        self.symbol = symbol
        print(self.number)

card = PlayCards(2,'red','club') 
print(card.color)
