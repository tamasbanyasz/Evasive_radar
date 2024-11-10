import numpy as np
import time


class EvasiveRadar:
    def __init__(self, size):
        self.matrix_col = size
        self.matrix_row = size

        self.return_pos = size // 2  # position of the staying number
        self.own_row = self.return_pos

        self.row_step = 0  # position of the moving number
        self.obj_col = 0

    def display_radar(self):

        while self.obj_col != self.matrix_col:
            radar_map = np.zeros((self.matrix_row, self.matrix_col), dtype=int)  # create map

            self.get_incoming_number_position(radar_map)

            self.dodge_when_number_incoming(radar_map)

            self.get_dodging_number_position(radar_map)

            time.sleep(1)

            self.row_step += 1 # row steps of the moving number
            print(f"\n{radar_map}\n")

            self.change_column_of_moving_number()

            self.return_back_when_moving_number_gone_to_next_column(radar_map)

    def dodge_when_number_incoming(self, radar_map):  # step one index to left when the moving number coming
        if radar_map[self.matrix_col // 2 - 1, self.own_row] != 0:
            self.own_row -= 1

    def return_back_when_moving_number_gone_to_next_column(self, radar_map):  # staying number return back to the original position
        if all(radar_map[-self.matrix_col:, self.return_pos] == 0):
            self.own_row += 1

    def change_column_of_moving_number(self):  # if the moving number reached the bottom of the matrix it steps one column to right
        if self.row_step == self.matrix_col:
            self.obj_col += 1
            self.row_step = 0

    def get_incoming_number_position(self, radar_map):  # moving number on the matrix
        radar_map[self.row_step, self.obj_col] = 4

    def get_dodging_number_position(self, radar_map):  # staying number on the matrix
        radar_map[self.matrix_col // 2, self.own_row] = 1


if __name__ == "__main__":
    obj = EvasiveRadar(4)
    obj.display_radar()
    something = 10 + 10
