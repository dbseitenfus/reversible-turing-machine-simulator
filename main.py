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

        self.create_tapes()

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
        self.quintuples = []

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

            self.quintuples.append(quintuple)

    def read_tape_input(self, file):
        self.tape_input = file.readline().strip()

    def create_tapes(self):
        self.input_tape = Tape(self.tape_input)
        self.history_tape = Tape()
        self.output_tape = Tape()
    
    def run(self):
        print(self.tape_input)
        self.create_quadruples()
        print(self.states)
        for quadruple in self.quadruples:
            print(f'({quadruple.current_state}, {quadruple.read_symbol})=({quadruple.action}, {quadruple.next_state})')

    def create_quadruples(self):
        self.quadruples = []
        for quintuple in self.quintuples:

            new_state_id = f"{quintuple.current_state}_{sum(1 for state in self.states if state.startswith(f'{quintuple.current_state}_')) + 1}"

            moviment_quadruple = Quadruple(
                new_state_id,
                '/',
                quintuple.next_state,
                quintuple.move_direction
            )

            self.states.append(new_state_id)

            read_and_write_quadruple = Quadruple(
                quintuple.current_state,
                quintuple.read_symbol,
                new_state_id,
                quintuple.write_symbol
            )

            self.quadruples.append(read_and_write_quadruple)
            self.quadruples.append(moviment_quadruple)


if __name__ == "__main__":
    simulation = Simulation()
    simulation.run()