from enum import Enum
import masteranime
from pyquery import PyQuery as pq
import json

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

class Mirror():
    qualities = {}
    def __init__(self,name,q):
        self.name = name
        self.qualities = q

class Episode():
    def __init__(self,anime):
        self.anime = anime

    async def fetch_mirrors(self):
        async with masteranime.client.get("https://www.masterani.me/anime/watch/{}/{}".format(self.anime.slug,self.episode)) as r:
            if r.status==200:
                r = await r.text()
                r = pq(r)
                p = json.loads(r("video-mirrors").attr(":mirrors"))
                ret = []
                qualities = {}
                prefixes = {}
                suffixes = {}
                for i in p:
                    if i['host']['name'] not in qualities:
                        qualities[i['host']['name']] = {}
                    if i['host']['name'] not in prefixes:
                        prefixes[i['host']['name']] = {}
                    if i['host']['name'] not in suffixes:
                        suffixes[i['host']['name']] = {}
                    qualities[i['host']['name']][i['quality']] = i['embed_id']
                    prefixes[i['host']['name']] = i['host']['embed_prefix']
                    suffixes[i['host']['name']] = i['host']['embed_suffix']
                for k,v in qualities.items():
                    q={}
                    for m,n in v.items():
                        suffix = suffixes[k]
                        if not suffix:
                            suffix=""
                        q[m] = "{}{}{}".format(prefixes[k],n,suffix)
                    ret.append(Mirror(k,q))
                return ret

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

    def __str__(self):
        ret = ""
        for attr, value in self.__dict__.items():
            ret+="{} : {}\n".format(attr,value)
        return ret
