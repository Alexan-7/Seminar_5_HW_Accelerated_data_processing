number_of_sweets = 120
player_turn = 1 # первый ход

def can_take(sweets):
    return sweets >= 1 and sweets <= 28

def switch_player_turn(turn): # переключение очереди
    return 1 if player_turn == 2 else 2

def end_of_game(sweets):
    return number_of_sweets <= 0

while (not end_of_game(number_of_sweets)): # пока не кончилась игра
    print(f'On the table {number_of_sweets} candies. How many sweets you will take?')
    taken = int(input()) # сколько палочек берет игрок

    if not can_take(taken):
        print(F'You can not eat {taken} sweets. Try again from 1 to 28 sweets')
        continue # чтобы вернуться в начало цикла

    number_of_sweets -= taken # если взял нормально
    print(f'Sweets taken: {taken}\n')

    if end_of_game(number_of_sweets):
        print(f'We do not have any more candy in the game! \nPlayer {player_turn} is the winning player!')
        break

    player_turn = switch_player_turn(player_turn) # поменяем очередь игрока