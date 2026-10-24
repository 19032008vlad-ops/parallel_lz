import importlib


def main():
    try:
       
        x = int(input('Enter task number (1, 2, or 3): '))
        
        if x not in (1, 2, 3):
            print(f'Error: Task number {x} does not exist. Please enter 1, 2, or 3.')
            return

        module_name = f'task{x}'
    
        module = importlib.import_module(module_name)
        
        module.main()
                
    except ModuleNotFoundError:
        print(f'Error: Module file "v1_t{x}.py" not found in the folder.')
    except ValueError:
        print('Error: You did not enter a number. Please enter the digit 1, 2, or 3.')
    except AttributeError:
        print(f'Error: The file "v1_t{x}.py" does not have a main() function.')
    

if __name__ == '__main__':
    main()