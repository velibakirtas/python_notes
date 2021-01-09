import requests

class theMovieDB:

    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "20e1eeb6f4cc4ce8698ec36ea01c049d"
        
    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/top_rated?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getSearhResults(self,keyword):
        response1 = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response1.json()

movieApi = theMovieDB()    
    
while True:
    secim = input("1-Popular Movies\n2-Search Movies\n3-Exit\nSeçim: ")    
    if secim == "3":
        break
    else:
        if secim == "1":
            movies = movieApi.getPopulars()
            for movie in movies["results"]:
                print(movie["title"])
        
        if secim == "2":
            keyword = input("keyword: ")     
            movies = movieApi.getSearhResults(keyword)           
            for movie in movies["results"]:
                print(movie["name"])
            
                

        
   
         