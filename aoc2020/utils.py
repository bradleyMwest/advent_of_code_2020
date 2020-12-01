def read_file(fname):
    with open(fname, 'r') as f:
        file = f.read().splitlines() # this reads each line in as a string
        input_list = [int(i) for i in file] # convert string to int
    return input_list