"""
Parses the movie folders directory and creates collections of movies from every folder that contains "(Collection)" 
in its folder name with the movies inside that collection folder.

Collections can be made from Directors - "Alfred Hitchcock (Collection)" or even movie collections such as - "Harry Potter (Collection)".
The folder structure template is the one followed by Plex: Movie Name (Year).
"""

"""
The Lord of the Rings: &lotr
  - ^The Lord of The Rings.+?(The Fellowship of the Ring|The Two Towers|The Return of the King)$
The Hobbit: &hobbit
  - ^The Hobbit.+?(An Unexpected Journey|The Desolation Of Smaug|The Battle Of The Five Armies)$
Tolkien:
  - *lotr
  - *hobbit
 
- Wings {{ 1929 }}
"""

import glob
import os
import re

def is_video_file(filename):
    if filename.endswith('.mp4') or filename.endswith('.avi') or filename.endswith('.flv') or filename.endswith('.mkv') or filename.endswith('.mov') or filename.endswith('.webm') or filename.endswith('.wmv'):
        return True
    else:
        return False

def isAlphaNumericRegex(char):
    result = re.match("(^[a-zA-Z0-9])", char)
    return result

def get_movie_name_converted(movie_name):
    new_movie_name = ""
    get_real_number_of_dashes = movie_name.count(" - ")
    found_first_dash = False

    for char in movie_name:
        if get_real_number_of_dashes == 1: #transform "X-Men - First Class" -> "X-Men: First Class"
            previous_char = new_movie_name[:len(new_movie_name)][-1:]

            if isAlphaNumericRegex(char) or char.isspace():
                new_movie_name += char
            elif char == "-" and previous_char == " ":
                size = len(new_movie_name)
                new_movie_name = new_movie_name[:size-1]
                new_movie_name += '.'
            else:
                new_movie_name += '.'
    
        elif get_real_number_of_dashes == 2: #transform "The Twilight Saga - Breaking Dawn - Part 2 (2012)" -> "The Twilight Saga: Breaking Dawn - Part 2"
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

def get_movie_year(movie_name):
    return movie_name[-9:-5]

if __name__ == "__main__":
    cwd = os.getcwd()
    entries = os.listdir(cwd)

    movies_collection = [] # movie names with (Collection)
    movies = [] # movie names without (Collection)

    for entry in entries:
        if "(Collection)" in entry:
            movies_collection.append(entry)

    movies = movies_collection
    movies = list(map(lambda x: x.replace(' (Collection)','').replace('',''),movies))

    f = open("collections.yml", "w", encoding='utf-8')

    count = 0
    for j in movies_collection:
        f.write(movies[count] + ' Collection:\n')
        folderpath = cwd + '\\' + j
        for subdir, dirs, files in os.walk(folderpath):
            for file in files:
                if is_video_file(file):
                    f.write('  - ^' + get_movie_name_converted(file[:-11]) + ' {{ ' + get_movie_year(file) + ' }}$\n')
        count += 1

    f.close()






