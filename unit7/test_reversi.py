import reversi

'''
gb = reversi.GameBoard()

gb.render_board()

user = reversi.UserPlayer(gb)

print(user.player)

neighbours = gb.get_allneighbours()
print(neighbours)

hints = gb.get_hints('X')
print (hints)

coord = user.next_move()
print(coord)
'''
gc = reversi.GameController()
gc.game_loop()
