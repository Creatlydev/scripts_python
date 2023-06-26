from time import sleep


def read_file(input_file) :
    # Read the input HTML file
    with open(input_file, 'r', encoding='utf-8') as file:
        return file.read()


def write_file(input_file, output_file, time_sleep: float= .05) :
    ''' 
        Write content of input_file to output_file
            Examples
                ======================================
            >>> write_file('input.html', 'index.html')
            >>> # Alter to time_sleep
            >>> write_file('input.html', 'index.html', .1)
    '''
    content= read_file(input_file) 
    with open(output_file, 'w', encoding='utf-8') as file:
        for ch in content:
            # Write each character to the output file
            file.write(ch)
            file.flush() # Clear buffer to write immediately

            # Adjust the sleep time to control the typing speed
            sleep(time_sleep)




if __name__ == '__main__' :
    import argparse

    parser= argparse.ArgumentParser(
        description= 'Simple Pyhton script for write of a input_file to output_file'
    )
    parser.add_argument('input_file', help= 'input file to be writer')
    parser.add_argument('output_file', help= 'output file')
    parser.add_argument('-t', '--time-sleep', type= float, help= 'Time sleep between each letter of input file', default= .05) 
    # Get all args
    args= parser.parse_args() 
    write_file(
        input_file= args.input_file,
        output_file= args.output_file,
        time_sleep= args.time_sleep
    )
