import multiprocessing
import random
import time


def generation(p_conn, count):           
    numbers = [random.randint(-1_000_000, 1_000_000) for _ in range(count)]
    p_conn.send(numbers)
    p_conn.close()

def square(p_conn):         
    numbers = p_conn.recv()
    square = [i**2 for i in numbers]   
    print(f'Number of numbers : {len(numbers)} . Squares of numbers: {square}')
    p_conn.close()  

def main():                     
    numbers_count = 1_000
    receiver_pipe, sender_pipe = multiprocessing.Pipe()
    generator_process = multiprocessing.Process(target = generation, args=(sender_pipe, numbers_count, ) )
    calculator_process  = multiprocessing.Process(target=square ,args = (receiver_pipe, ))
    print('Start process')
    start_time = time.perf_counter()
    generator_process.start()
    calculator_process .start()
    generator_process.join()
    calculator_process .join()
    print(f'The process is completed in {time.perf_counter() - start_time} seconds')

if __name__ == "__main__":
    main()