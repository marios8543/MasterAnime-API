import masteranime
import asyncio
loop = asyncio.get_event_loop()

#Blocking implementations
def Anime(id):
    return loop.run_until_complete(masteranime.Anime(id))
def Search(query,detailed=False):
    return loop.run_until_complete(masteranime.Search(query,detailed))
def Trending(detailed=False):
    return loop.run_until_complete(masteranime.Trending(detailed))
def Releases(detailed=False):
    return loop.run_until_complete(masteranime.Releases(detailed))