from collections import deque

class Quintuple: 
    def __init__(self, current_state, read_symbol, next_state, write_symbol, move_direction):
        self.current_state = current_state
        self.read_symbol = read_symbol
        self.next_state = next_state
        self.write_symbol = write_symbol
        self.move_direction = move_direction

class Quadruple:
    def __init__(self, current_state, read_symbol, next_state, move_direction):
        self.current_state = current_state
        self.read_symbol = read_symbol
        self.next_state = next_state
        self.move_direction = move_direction

class Fita:
    def __init__(self, entrada=None):
        if entrada:
            self.fita = deque(entrada)
        else:
            self.fita = deque(['B'])
        self.posicao = 0

file = open('entrada-quintupla.txt', 'r')

first_line = file.readline()
second_line = file.readline()
third_line = file.readline()
fourth_line = file.readline()

first_line_data = first_line.split(' ')

number_of_states = first_line_data[0]
number_of_symbols_input_alphabet = first_line_data[1]
number_of_symbols_tape_alphabet = first_line_data[2]
number_of_transitions = int(first_line_data[3])

states = second_line.replace('\n', '').split(' ')
input_alphabet = third_line.replace('\n', '').split(' ')
tape_alphabet = fourth_line.replace('\n', '').split(' ')

quintuples = []

for _ in range(number_of_transitions):
    line = file.readline().strip()

    parts = line.replace('(','').replace(')','').split('=')
    left_part = parts[0].split(',')
    right_part = parts[1].split(',')

    quintuple = Quintuple(
        current_state = int(left_part[0]),
        read_symbol = left_part[1],
        next_state = int(right_part[0]),
        write_symbol = right_part[1],
        move_direction = right_part[2]
    )

    quintuples.append(quintuple)

accepting_state = file.readline().strip()

file.close()

# for quintuple in quintuples:
#     print(f'({quintuple.current_state}, {quintuple.read_symbol}) = ({quintuple.next_state}, {quintuple.write_symbol}, {quintuple.move_direction})')