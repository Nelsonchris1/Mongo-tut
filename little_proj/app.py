from util import create_connection
from read import read_data
from read import write_data
import datetime 

def main():
    start_time = datetime.now()
    inventory = read_data()
    write_data(inventory)
    end_time = datetime.now()
    total_runtime = end_time - start_time
    
    

if __name__ == "__main__":
    main()