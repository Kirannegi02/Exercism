# TODO: define the 'EXPECTED_BAKE_TIME' constant
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer


# TODO: define the 'bake_time_remaining()' function
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
def bake_time_remaining(time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    pass
    return EXPECTED_BAKE_TIME - time

# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(layers):
    """
    :param layers: int total number of layers of lagasna
    :return: int total time of preparation of layers derived from 
             preparation_time_in_minutes
    Function that takes the number of layers that will be prepared to lasagna and 
    returns how many minutes it will take to get done.
    """
    return layers * PREPARATION_TIME



# TODO: define the 'elapsed_time_in_minutes()' function

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time 
    already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
