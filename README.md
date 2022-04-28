# Movie-Recomender
A program that recommends certain movies to users based on a movie title. It asks the user for a movie title anthen searches a movie databaseand reccomends similair movies using a machine learning algorithm. 

Design:
------
See the flowchart and UML diagram 

Program Files: 
-------------
You need to have the following files in the same diretory to run the program:
project_1.py
tmdb_5000_movies.csv
tmdb_5000_credits.csv

Unit tests:
-----------
test_project_1.py

Requires installation of packages: 
---------------------------------
pip install pandas
pip install scikit-learn
pip install regex
pip install numpy
pip install ast



Example of Run: 
---------------

C:\INST326\Exercise_4\Movie-Recomender>python project_1.py
Enter a Title or part of a Title: Iron

Here are some matching Titles you can search
Iron Man 3
Iron Man
Iron Man 2
The Iron Giant
The Man in the Iron Mask
Gridiron Gang
Ironclad
The Man with the Iron Fists
The Iron Lady

Enter one of them to narrow your search
Enter a Title or part of a Title: Iron Man 3

Searching Recommended Movies like: Iron Man 3 ....
Here are the recommended Movies:
--------------------------------

Title: Avengers: Age of Ultron
Genre: Action, Adventure, Science Fiction
Cast: Robert Downey Jr., Chris Hemsworth, Mark Ruffalo
Homepage: http://marvel.com/movies/movie/193/avengers_age_of_ultron

Title: The Avengers
Genre: Science Fiction, Action, Adventure
Cast: Robert Downey Jr., Chris Evans, Mark Ruffalo
Homepage: http://marvel.com/avengers_movie/

Title: Captain America: Civil War
Genre: Adventure, Action, Science Fiction
Cast: Chris Evans, Robert Downey Jr., Scarlett Johansson
Homepage: http://marvel.com/captainamericapremiere

Title: Iron Man
Genre: Action, Science Fiction, Adventure
Cast: Robert Downey Jr., Terrence Howard, Jeff Bridges
Homepage: http://www.ironmanmovie.com/

Title: Iron Man 2
Genre: Adventure, Action, Science Fiction
Cast: Robert Downey Jr., Gwyneth Paltrow, Don Cheadle
Homepage: http://www.ironmanmovie.com/

C:\INST326\Exercise_4\Movie-Recomender>


Example Unit test: 
------------------

C:\INST326\Exercise_4\Movie-Recomender>pytest test_project_1.py
=========================================================================================================== test session starts ============================================================================================================
platform win32 -- Python 3.10.2, pytest-7.1.2, pluggy-1.0.0
rootdir: C:\INST326\Exercise_4\Movie-Recomender
plugins: anyio-3.5.0
collected 8 items

test_project_1.py ........                                                                                                                                                                                                            [100%]

============================================================================================================ 8 passed in 15.06s ============================================================================================================

C:\INST326\Exercise_4\Movie-Recomender>
