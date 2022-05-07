# Movie-Recomender
A program that recommends certain movies to users based on a movie title. It asks the user for a movie title anthen searches a movie databaseand reccomends similair movies using a machine learning algorithm. 

Design:
------
See the flowchart and UML diagram 

Program Files: 
-------------
You need to have the following files in the same diretory to run the program:
movie_rec_mod.py   # runs a text version of the application
movie_rec_gui.py   # runs a simple Graphical User Iterface (GUI) Uses movie_rec_mod.py
tmdb_5000_movies.csv  #movie dataset
tmdb_5000_credits.csv  #Movie dataset
movie_help.txt  # Help file for GUI app

Unit tests:
-----------
test_movie_rec_mod.py

Unit tests the movie_rec_mod.py

RUN with pytest:
pytest test_movie_rec_mod.py

Requires installation of packages: 
---------------------------------
pip install pandas
pip install scikit-learn
pip install regex
pip install numpy
pip install ast
pip ionstall tkinter



Example of Run: 
---------------
With GUI:
C:\INST326\Final_Project_git\Movie-Recomender>python movie_rec_gui.py
or
Without GUI:
\INST326\Final_Project_git\Movie-Recomender>python movie_rec_mod.py

Example text version run:
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


Example Unit test: 
------------------

C:\INST326\Final_Project_git\Movie-Recomender>pytest test_movie_rec_mod.py
=========================================================================================================== test session starts ============================================================================================================
platform win32 -- Python 3.10.2, pytest-7.1.2, pluggy-1.0.0
rootdir: C:\INST326\Final_Project_git\Movie-Recomender
plugins: anyio-3.5.0
collected 8 items

test_movie_rec_mod.py ........                                                                                                                                                                                                            [100%]

============================================================================================================ 8 passed in 15.06s ============================================================================================================

