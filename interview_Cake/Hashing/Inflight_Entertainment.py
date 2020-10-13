import time

def Flight(flight_length:int, movie_lengths:list):

    for first_movie in movie_lengths:
        for second_movie in movie_lengths:
            sec_check = flight_length - first_movie
            second_movie == sec_check
            if first_movie + second_movie == flight_length:
                return True
            else:
                return False

flight_len = int(input())
movie_len = list(int(input()) for i in range(3))

print(Flight(flight_len, movie_len))