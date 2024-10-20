from collections import deque

class Quintuple: 
    def __init__(self, current_state, read_symbol, next_state, write_symbol, move_direction):
        self.current_state = current_state
        self.read_symbol = read_symbol
        self.next_state = next_state
        self.write_symbol = write_symbol
        self.move_direction = move_direction

class Quadruple:
    def __init__(self, current_state, read_symbol, action, next_state):
        self.current_state = current_state
        self.read_symbol = read_symbol # pode ser / (sem leitura), ou o símbolo a ser lido
        self.action = action # pode ser o símbolo a ser escrito ou o movimento (+, -, 0)
        self.next_state = next_state

class Tape:
    def __init__(self, input=None):
        if input:
            self.tape = deque(input)
        else:
            self.tape = deque(['B'])
        self.position = 0

class Simulation:
    def __init__(self):
        file = open('entrada-quintupla.txt', 'r')
        self.read_header(file)
        self.read_quintuples(file)
        self.read_tape_input(file)
        file.close()

    def read_header(self, file):
        first_line = file.readline()
        second_line = file.readline()
        third_line = file.readline()
        fourth_line = file.readline()
        first_line_data = first_line.split(' ')
        self.number_of_statesnumber_of_states = first_line_data[0]
        self.number_of_symbols_input_alphabet = first_line_data[1]
        self.number_of_symbols_tape_alphabet = first_line_data[2]
        self.number_of_transitions = int(first_line_data[3])
        self.states = second_line.replace('\n', '').split(' ')
        self.input_alphabet = third_line.replace('\n', '').split(' ')
        self.tape_alphabet = fourth_line.replace('\n', '').split(' ')

    def read_quintuples(self, file):
        quintuples = []

        for _ in range(self.number_of_transitions):
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

    def read_tape_input(self, file):
        self.tape_input = file.readline().strip()

    
    def run(self):
        print(self.tape_input)

if __name__ == "__main__":
    simulation = Simulation()
    simulation.run()