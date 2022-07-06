# movie_app
Created a Python application that consumes a dataset from the user and exposes the Flask API as a service for users to interact with the application

LIST OF API’s
------------------------------------------------------------------------------------------------------------------------------------------
API which takes a json file as an input and inserts the data into ElasticSearch.

POST METHOD :

API URL - http://127.0.0.1:5005/insert_all

Input :

Json file - (Movies_DB.json)

Sample input :

{
    "file_path" : "/home/harinibandaru/Downloads/Movies_DB.json"
}

Output:

Documents inserted successfully
-----------------------------------------------------------------------------------------------------------------------------------------
API to insert a new record into the ElasticSearch index which we already created in Step-1

POST METHOD:

API URL - http://127.0.0.1:5005/insert

Input :

Insert document with required fields

Sample input :

     {
            "id": 137,
            "title": "The Shining",
            "year": "1980",
            "runtime": "146",
            "genres":
            [
                "Drama",
                "Horror"
            ],
            "director": "Stanley Kubrick",
            "actors": "Jack Nicholson, Shelley Duvall, Danny Lloyd, Scatman Crothers",
            "plot": "A family heads to an isolated hotel for the winter where an evil and spiritual presence influences the father into violence, while his psychic son sees horrific forebodings from the past and of the future.",
            "posterUrl": "http://ia.media-imdb.com/images/M/MV5BODMxMjE3NTA4Ml5BMl5BanBnXkFtZTgwNDc0NTIxMDE@._V1_SX300.jpg"
        }

Output:

Created
 
 ----------------------------------------------------------------------------------------------------------------------------------------
API to delete a record from the ElasticSearch index based on the ID

GET METHOD :

API URL - http://127.0.0.1:5005/delete_doc/{integer_value}
 
Sample url - http://127.0.0.1:5005/delete_doc/5

Output :

Document Deleted Successfully
------------------------------------------------------------------------------------------------------------------------------------------
API to give a brief stats like how many unique genres, actors and directors are there in the entire dataset

GET METHOD :

API URL - http://127.0.0.1:5005/stats

Output :

{
   "actors": 97,
   "directors": 81,
   "genres": 21
}

------------------------------------------------------------------------------------------------------------------------------------------
API to get a specific movie related details based on the movie name

GET METHOD :

API URL - http://127.0.0.1:5005/movie_search/{movie_name}

Sample input - http://127.0.0.1:5005/movie_search/Shutter Island

Output :

{
   "plot": "In 1954, a U.S. marshal investigates the disappearance of a murderess who escaped from a hospital for the criminally insane.",
   "title": "Shutter Island"
}
------------------------------------------------------------------------------------------------------------------------------------------
API to get a specific movie related details based on the director name

GET METHOD :

API URL - http://127.0.0.1:5005/director_search/{director_name}

Sample input - http://127.0.0.1:5005/director_search/Christopher Nolan

Output :

{
   "plot": "A man juggles searching for his wife's murderer and keeping his short-term memory loss from being an obstacle.",
   "title": "Memento",
   "year": "2000"
}

------------------------------------------------------------------------------------------------------------------------------------------
API to get a specific movie related details based on the actor name

GET METHOD :
API URL - http://127.0.0.1:5005/actor_search/{actor_name}

Sample input -  http://127.0.0.1:5005/actor_search/Leonardo%20DiCaprio

Output :

{
   "1": {
       "actors": "Leonardo DiCaprio, Daniel York, Patcharawan Patarakijjanon, Virginie Ledoyen",
       "plot": "Twenty-something Richard travels to Thailand and finds himself in possession of a strange map. Rumours state that it leads to a solitary beach paradise, a tropical bliss - excited and intrigued, he sets out to find it.",
       "title": "The Beach"
   },
   "2": {
       "actors": "Jamie Foxx, Christoph Waltz, Leonardo DiCaprio, Kerry Washington",
       "plot": "With the help of a German bounty hunter, a freed slave sets out to rescue his wife from a brutal Mississippi plantation owner.",
       "title": "Django Unchained"
   },
   "3": {
       "actors": "Leonardo DiCaprio, Tom Hanks, Christopher Walken, Martin Sheen",
       "plot": "The true story of Frank Abagnale Jr. who, before his 19th birthday, successfully conned millions of dollars' worth of checks as a Pan Am pilot, doctor, and legal prosecutor.",
       "title": "Catch Me If You Can"
   },
   "4": {
       "actors": "Leonardo DiCaprio, Jonah Hill, Margot Robbie, Matthew McConaughey",
       "plot": "Based on the true story of Jordan Belfort, from his rise to a wealthy stock-broker living the high life to his fall involving crime, corruption and the federal government.",
       "title": "The Wolf of Wall Street"
   },
   "5": {
       "actors": "Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page, Tom Hardy",
       "plot": "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
       "title": "Inception"
   },
   "6": {
       "actors": "Leonardo DiCaprio, Mark Ruffalo, Ben Kingsley, Max von Sydow",
       "plot": "In 1954, a U.S. marshal investigates the disappearance of a murderess who escaped from a hospital for the criminally insane.",
       "title": "Shutter Island"
   }
}




 
 

 


















