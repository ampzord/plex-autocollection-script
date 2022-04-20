"""
Simple script to transfrom all Oscar Winners Movies from Best Picture till Best Animation 
To a readable .yml file to be further processed into Plex Collections automatically. 
"""

"""
Columns Order:    
        Best Picture, Best Actor, Best Actress, Best Supporting Actor, Best Supporting Actress, 
        Best Original Screenplay, Best Adapted Screenplay, Best Cinematography, Best Director
        Best Animation, IMDB Top 250 Movies

Example of data in .csv

Template1 : 1927 - "Wings"
Template2 : 1927 - Emil Jannings, "The Way of All Flesh"

.yml File Format Example
Best Picture:
 - Wings {{ 1927 }}
"""

import csv
import re

csv_filename = 'MyOscarsWinnersList.csv'

def read_csv(filename):

    best_picture_list = []
    best_actor_list = []
    best_actress_list = []
    best_supp_actor_list = []
    best_supp_actress_list = []
    best_orig_screenplay_list = []
    best_adap_screenplay_list = []
    best_cinematography_list = []
    best_director_list = []
    best_animation_list = []
    imdb_top250_movies_list = []

    header = True
    second_header = True

    with open(filename, encoding="utf-8") as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        header_count = 0
        for row in csvReader:
            if not header and not second_header:
                best_picture_list.append(row[0])
                best_actor_list.append(row[1])
                best_actress_list.append(row[2])
                best_supp_actor_list.append(row[3])
                best_supp_actress_list.append(row[4])
                best_orig_screenplay_list.append(row[5])
                best_adap_screenplay_list.append(row[6])
                best_cinematography_list.append(row[7])
                best_director_list.append(row[8])
                best_animation_list.append(row[9])
                imdb_top250_movies_list.append(row[10])

            if header_count >= 1:
                header = False
                second_header = False

            header_count += 1

    return best_picture_list, best_actor_list, best_actress_list, best_supp_actor_list, best_supp_actress_list, best_orig_screenplay_list, best_adap_screenplay_list, best_cinematography_list, best_director_list, best_animation_list, imdb_top250_movies_list

def parse_movie(movie_string):
    movies_year = movie_string[0:4]
    movies_title = movie_string.split('"')[1::2]
    return movies_title, movies_year

def write_to_file(collection_title, movie_list):
    header = True
    for movie in movie_list:
        if header:
            f.write(collection_title+':\n')
        if movie:
            movie_title, movie_year = parse_movie(movie)
            movie_string = " - ^" + get_movie_name_converted(movie_title[0]) + " {{ " + movie_year + " }}$"  
            f.write(movie_string+'\n') 
        header = False

def isAlphaNumericRegex(char):
    result = re.match("(^[a-zA-Z0-9])", char)
    return result

def get_movie_name_converted(movie_name):
    new_movie_name = ""
    get_real_number_of_dashes = movie_name.count(" - ")
    found_first_dash = False

    for char in movie_name:
        if get_real_number_of_dashes == 1: #trasform "X-Men - First Class" -> "X-Men: First Class"
            previous_char = new_movie_name[:len(new_movie_name)][-1:]

            if isAlphaNumericRegex(char) or char.isspace():
                new_movie_name += char
            elif char == "-" and previous_char == " ":
                size = len(new_movie_name)
                new_movie_name = new_movie_name[:size-1]
                new_movie_name += '.'
            else:
                new_movie_name += '.'
    
        elif get_real_number_of_dashes == 2: #trasform "The Twilight Saga - Breaking Dawn - Part 2 (2012)" -> "The Twilight Saga: Breaking Dawn - Part 2"
            previous_char = new_movie_name[:len(new_movie_name)][-1:]

            if isAlphaNumericRegex(char) or char.isspace():
                new_movie_name += char
            elif char == "-" and previous_char == " ":
                if found_first_dash == False:
                    size = len(new_movie_name)
                    new_movie_name = new_movie_name[:size-1]
                    new_movie_name += '.'
                else:
                    new_movie_name += '.'
                found_first_dash = True
            else:
                new_movie_name += '.'
        else:
            if isAlphaNumericRegex(char) or char.isspace():
                new_movie_name += char
            else:
                new_movie_name += '.'

    return new_movie_name

if __name__ == "__main__":

    best_picture_list, best_actor_list, best_actress_list, best_supp_actor_list, best_supp_actress_list, best_orig_screenplay_list, best_adap_screenplay_list, best_cinematography_list, best_director_list, best_animation_list, imdb_top250_movies_list = read_csv(csv_filename)

    f = open("movie_oscars.yml", "w", encoding='utf-8')

    write_to_file("Best Picture Collection", best_picture_list)
    write_to_file("Best Actor Collection", best_actor_list)
    write_to_file("Best Actress Collection", best_actress_list)
    write_to_file("Best Supporting Actor Collection", best_supp_actor_list)
    write_to_file("Best Supporting Actress Collection", best_supp_actress_list)
    write_to_file("Best Original Screenplay Collection", best_orig_screenplay_list)
    write_to_file("Best Adapted Screenplay Collection", best_adap_screenplay_list)
    write_to_file("Best Cinematography Collection", best_cinematography_list)
    write_to_file("Best Director Collection", best_director_list)
    write_to_file("Best Animation Collection", best_animation_list)
    write_to_file("IMDB Top250 Collection", imdb_top250_movies_list)




