from enum import Enum
import masteranime

class Type(Enum):
    TV = 0
    Movie = 1
    OVA = 2
    Special = 3
    ONA = 4

class Genre():
    def __init__(self,id,name):
        self.id = id
        self.title = name

class Episode():
    pass

class Release():
    def __init__(self,created,episode,anime):
        self.created_at = created
        self.episode = episode
        self.anime = anime
    
    def __str__(self):
        return"Created at: {}\nEpisode: {}\nAnime: {}".format(self.created_at,self.episode,str(self.anime))

class Anime():
    id=0
    genres=[]
    episodes=[]

    async def detailed(self):
        return await masteranime.Anime(self.id)

    async def stream(self):
        return
        #TODO: implement

    def __str__(self):
        ret = ""
        for attr, value in self.__dict__.items():
            ret+="{} : {}\n".format(attr,value)
        return ret
