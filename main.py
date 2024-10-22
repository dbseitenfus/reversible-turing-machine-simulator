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
            self.tape = input
        else:
            self.tape = []
        self.position = 0
    
    def get_current_symbol(self):
        if self.position > len(self.tape)-1:
            return 'B'
        return self.tape[self.position]
    
    def write_symbol(self, symbol):
        if self.position > len(self.tape)-1:
            self.tape.append('B')
            return
        self.tape[self.position] = symbol

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
        self.final_state = self.states[len(self.states)-1]
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
                current_state = left_part[0],
                read_symbol = left_part[1],
                next_state = right_part[0],
                write_symbol = right_part[1],
                move_direction = right_part[2]
            )

            self.quintuples.append(quintuple)

    def read_tape_input(self, file):
        self.tape_input = file.readline().strip()

    def create_tapes(self):
        self.input_tape = Tape(list(self.tape_input))
        self.history_tape = Tape()
        self.output_tape = Tape()

    def print_tapes(self):
        print("tapes:")
        print(f"input: {self.input_tape.tape}")
        print(f"history: {self.history_tape.tape}")
        print(f"output: {self.output_tape.tape}")

    def get_quintuple(self, state, read_symbol):
        for quintuple in self.quintuples:
            if quintuple.current_state == state and quintuple.read_symbol == read_symbol: 
                return quintuple
            
    def get_quadruple(self, state, read_symbol):
        for quadruple in self.quadruples:
            if quadruple.current_state == state and (quadruple.read_symbol == read_symbol or quadruple.read_symbol == '/'): 
                return quadruple
    
    def run(self):
        print(self.tape_input)
        self.create_quadruples()
        print(self.states)
        for quadruple in self.quadruples:
            print(f'({quadruple.current_state}, {quadruple.read_symbol})=({quadruple.action}, {quadruple.next_state})')
        self.print_tapes()

        state = self.states[0]

        while state != self.final_state:
            print('')
            self.print_tapes()
            current_symbol = self.input_tape.get_current_symbol()
            quadruple = self.get_quadruple(state, current_symbol)
            print(f"ESTADO: ({state}, {current_symbol})")


            if quadruple is None:
                print("Movimento inválido!")
                return
            
            if quadruple.read_symbol != '/': #leitura/escrita
                # self.input_tape.tape[self.input_tape.position] = quadruple.action
                self.input_tape.write_symbol(quadruple.action)
            else: # movimento
                if quadruple.action == '-':
                    self.input_tape.position -= 1
                elif quadruple.action == '+':    
                    self.input_tape.position += 1

            state = quadruple.next_state

        


    def create_quadruples(self):
        self.quadruples = []
        for quintuple in self.quintuples:

            new_state_id = f"{quintuple.current_state}_{sum(1 for state in self.states if state.startswith(f'{quintuple.current_state}_')) + 1}"

            move_direction = ''
            if quintuple.move_direction == 'L':
                move_direction = '-'
            elif quintuple.move_direction == 'R':
                move_direction = '+'
            else:
                move_direction = '0'
            
            moviment_quadruple = Quadruple(
                new_state_id,
                '/',
                move_direction,
                quintuple.next_state
            )
       

            self.states.append(new_state_id)

            read_and_write_quadruple = Quadruple(
                quintuple.current_state,
                quintuple.read_symbol,
                quintuple.write_symbol,
                new_state_id
            )

            self.quadruples.append(read_and_write_quadruple)
            self.quadruples.append(moviment_quadruple)


if __name__ == "__main__":
    simulation = Simulation()
    simulation.run()