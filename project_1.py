"""INST326 Final Project

Project Team:
    Taner Bulbul
    Caleb Andree
    Ethan Klondar 


Movie recommendation system.
"""

#import pandas as pd  #data frames
import requests  # HTTP requests


def get_user_input():
    """Prompt user for movie preferences.
    
    Args:
        None
    Returns:
        Tuple: genre, artist_name, title.
    """ 
    # Prompt user for genre, artist_name, title
    # genre is mandotory, artist_name and title are optional and
    # should be set to None if not entered
    genre= input("Enter a genre:")
    artist_name = input("artist_name:")
    title= input("enter title of a movie:")
    
    return (genre,artist_name,title)
                 

def create_dataset():
    """load the dataset from Web or from a file
    
    Args:
        None
    Returns:
        None
    """ 
    
    # read a dataset file, e.g. CSV file
    # or Web API call to load a dataset with movie information
    #Using HTTP (not HTTPS) or not secure currently
    #below an example API call to The Movie Database API (TMDA)
    # themoviedb.org
    api_key = "69edbe08d42f4521bab37e2e5864045b"
    response = requests.get('http://api.themoviedb.org/3/discover/movie?api_key=' +  \
                            api_key + '&primary_release_year=2022')
    response_json = response.json() # store parsed json response
    print(response_json)

def get_streaming_svc_list(movie):
    """create a list of streaming service names
    
    Args:
        movie(Movie): Movie object
    Returns:
        list of strings containing streaming service names
    """
    #Search dataset to find streaming service that has this Movie
    #build a list and return that list
    stream_svcs =["Netflix", "Amazon"]
    return stream_svcs
    
def get_recommendation_movie(movie):
    """Find similiar movies for the movie.
    Args:
        movie(Movie): Movie object to find similar ones to
       
    """
    mvlist=[] #create an emply list
    #Apply some machine learning here ??????????
    #add the similar movies to this list
    rec_movie = Movie(2,"movie 2", "comedy",("a","b") )
    mvlist.append( rec_movie )
    return mvlist
    
    
class Movie():
    """Movie object to store movie information
    
    Attributes:
        movie_id(int): unique movie identifier.
        title (str): name of the movie.
        genre(str): genre of the movie.
        cast(list): list of names of artists
        
    """   
    def __init__(self,movie_id,title,genre,cast):
        """
        Args:
            movie_id(int): unique movie identifier.
            title (str): name of the movie.
            genre(str): genre of the movie.
            cast(list): list of names of artists
        """
        self.movie_id = movie_id
        self.title = title
        self.genre =genre
        self.cast = cast
    
    def __repr__(self):
        """ print a Movie object
        """
        return f"movie_id: {self.movie_id}\ntitle: {self.title}\n" + \
                f"genre: {self.genre}\ncast: {self.cast})\n"


class Recommendations():
    """List of recommended movies for the user.
    
    Attributes:
        rec_list(list): list of recommended movie data tuples
                            [(Movie obj1,stream1),(Movie obj2,stream2),...].
    """
        
    def __init__(self):
        """
        Args:
          None
        """
        self.rec_list =[] # start with empty list

    def add_recommendation(self,movie,stream_svc):
        """Add a recommended movie info to the recommendations list
        Args:
           movie(Movie): Movie object
           stream_svc(list): list of streaming services (Netflix, Amazon etc.)
        """
        new_movie =(movie,stream_svc) # create a tuple
        self.rec_list.append(new_movie) # add to the list


if __name__ == "__main__":

    mv_info= get_user_input() #prompt user for movie info
    print(mv_info)
    create_dataset() #from Web or file
    
    # create a test movie object for the user
    mv1 = Movie(1,"movie 1", "comedy",("a","b","c"))
    print("Find me movies similar to this:\n")
    print(mv1)
    
    #create a Recommendations object 
    rec= Recommendations()
    
    #find similiar movies to recommend to the user
    rec_movies = get_recommendation_movie(mv1)
    stream_svcs = get_streaming_svc_list(mv1)
    
    #add the recommended movie and streaming service to recommendation list
    rec.add_recommendation(rec_movies[0], stream_svcs)
    
    #print recommendations
    print("Recommended Movies\n")
    for i in range(len(rec.rec_list) ):
       print(rec.rec_list[i])
    
   


    