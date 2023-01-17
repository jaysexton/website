import random
uw=0
cw=0
tie=0

op=['Rock', 'Paper', 'Scissors']

while True:
    ui=input('Choose "Rock", "Paper", "Scissors" or "Q" to quit: ')
    if ui == 'Q':
        break
    if ui not in op:
        continue
    rn=random.randint(0,2)
    cp=op[rn]
    print('Computer chose', cp + '.')

    if ui == 'Rock' and cp == 'Scissors':
        print('You win!!')
        uw+=1
    elif ui == 'Paper' and cp == 'Rock':
        print('You win!!')
        uw+=1
    elif ui == 'Scissors' and cp == 'Paper':
        print('You win!!')
        uw+=1
    elif ui==cp:
        print('Tie!!')
        tie+=1

    else:
        print('You lose!!')
        cw+=1

print('You won',uw,'times.', 'The computer won',cw,'times.','You tied', tie,'times.','Goodbye!!')


