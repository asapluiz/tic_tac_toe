import re
import sys

GAME_ON = True
WINNER = ''
board =[' 1 | 2 | 3 ',
       '-----------',
       ' 4 | 5 | 6 ',
       '-----------',
       ' 7 | 8 | 9 ']

for board_parts in board:
    print(board_parts)

new_board = board
container_board = []

while GAME_ON:

    def effect_win_cond(player):
        global GAME_ON
        global WINNER

        GAME_ON = False
        WINNER = player
        print(f'{WINNER} win')


    # check player win conditions
    def player_win(val):

        #check horizontal win conditions
        for x in range(0, 5):
            if new_board[x][1] == val and new_board[x][5] == val and new_board[x][9] == val:
                if val == 'X':
                    effect_win_cond('player 1 ')
                else:
                    effect_win_cond('player 2 ')
                sys.exit()

        #check vertical win conditions
        for x in range(0, 11):
            if new_board[0][x] == val and new_board[2][x] == val and new_board[4][x] == val:
                if val == 'X':
                    effect_win_cond('player 1 ')
                else:
                    effect_win_cond('player 2 ')
                sys.exit()

        #check diagonal win
        if new_board[0][1] == val and new_board[2][5] == val and new_board[4][9] == val:
            if val == 'X':
                effect_win_cond('player 1 ')
            else:
                effect_win_cond('player 2 ')
            sys.exit()
        elif new_board[0][9] == val and new_board[2][5] == val and new_board[4][1] == val:
            if val == 'X':
                effect_win_cond('player 1 ')
            else:
                effect_win_cond('player 2 ')
            sys.exit()


    player1_input = input('Player 1 select your position :')
    for replace_board in new_board:
        replace_value = re.sub(player1_input, 'X', replace_board)
        container_board.append(replace_value)

    new_board = container_board
    container_board = []
    player_win('X')

    for board_parts in new_board:
        print(board_parts)



    player2_input = input('Player 2 select your position :')
    for replace_board in new_board:
        replace_value2 = re.sub(player2_input, "Ø", replace_board)
        container_board.append(replace_value2)

    new_board = container_board
    container_board = []
    player_win('Ø')

    for board_parts in new_board:
        print(board_parts)






