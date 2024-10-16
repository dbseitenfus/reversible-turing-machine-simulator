file = open('entrada-quintupla.txt', 'r')

first_line = file.readline()
first_line_data = first_line.split(' ')

number_of_states = first_line_data[0]
number_of_symbols_input_alphabet = first_line_data[1]
number_of_symbols_tape_alphabet = first_line_data[2]
number_of_transitions = first_line_data[3]
