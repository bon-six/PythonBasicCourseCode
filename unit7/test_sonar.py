import Sonar

gb = Sonar.GameBoard()
gb.reset_board()

gb.show_board()

gb.add_detector((2,3))
gb.add_detector((20,20))
gb.show_board()

gb.remove_detector((2,3))
gb.remove_detector((20,20))
gb.show_board()

gb.add_detector((10,7))
gb.show_detected_cell((10,7),9)
gb.show_detected_cell((10,7),8)
gb.show_detected_cell((10,7),7)
gb.show_detected_cell((10,7),6)
gb.show_detected_cell((10,7),5)
gb.show_detected_cell((10,7),4)
gb.show_detected_cell((10,7),3)
gb.show_board()

gb.remove_all_detected()
gb.show_board()
