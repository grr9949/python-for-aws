#Data types : The type of data which we use for our programme, mainly we use string (sequence of characters),
#   integer (whole number), Float (decimal values), Boolean(True/False)

def main():
    #String 
    instane_type='t2.miro'

    #integer
    num_of_instances=5
    up_time=10

    #float point number
    price=0.25

    #Boolean
    Instance_State=True

    print(f"I have {num_of_instances} instances of type {instane_type} running for {up_time} hours and per hour price is {price} USD.\nState is running = {Instance_State} ")

if __name__ == '__main__':
    main()