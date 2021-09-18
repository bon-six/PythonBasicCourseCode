
import TicTacToe


test_gb = TicTacToe.GameBoard()
print(test_gb)

'''
test_gb.moves[1][0] = 'X'
test_gb.render_board()

test_gb.moves[2][0] = 'Y'
test_gb.render_board()

test_gb.moves[0][2] = 'Z'
test_gb.render_board()
'''
'''
print(test_gb.check_space_free((1,0)))
print(test_gb.check_space_free((3,0)))
print(test_gb.check_space_free((0,4)))


print(test_gb.add_move('X',(1,0)))
test_gb.render_board()
print(test_gb.add_move('O',(0,1)))
test_gb.render_board()
print(test_gb.add_move('Z',(1,0)))
test_gb.render_board()
print(test_gb.add_move('X',(4,1)))
test_gb.render_board()
print(test_gb.add_move('X',(2,3)))
test_gb.render_board()
'''
test_computer = TicTacToe.ComputerPlayer(test_gb,'X')
print(test_computer)
'''
test_gb.moves[0][0]='X'
test_gb.moves[1][2]='X'
print(test_computer.find_onemove_win(test_gb.moves))
'''
'''
test_gb.moves[0][0]='O'
test_gb.moves[0][1]='O'
print(test_computer.find_onemove_lose(test_gb.moves))
'''
'''
print(test_computer.find_corner_move(test_gb.moves))
print(test_computer.find_center_move(test_gb.moves))
print(test_computer.find_side_move(test_gb.moves))
print(test_computer.find_random_move(test_gb.moves))

print(test_computer.next_move())
'''
test_user = TicTacToe.UserPlayer(test_gb)
print(test_user)


