import data_classes
import aiohttp
import asyncio

BASE_URL = 'https://www.masterani.me/api'
client = aiohttp.ClientSession()

async def Anime(id):
    r = await client.get("{}/anime/{}/detailed".format(BASE_URL,id))
    if r.status==200:
        r = await r.json()
        ani = data_classes.Anime()
        ani.type = data_classes.Type((r['info']['type']))
        for k,v in r['info'].items():
            setattr(ani,k,v)
        for i in r['genres']:
            ani.genres.append(data_classes.Genre(i['id'],i['name']))
        for i in r['episodes']:
            ep = data_classes.Episode
            for k,v in i.items():
                setattr(ep,k,v)
            ani.episodes.append(ep)
        return ani

async def Search(query,detailed=False):
    r = await client.get("{}/anime/search".format(BASE_URL),params={'search':query})
    if r.status==200:
        r = await r.json()
        if len(r)>0:
            ret = []
            for i in r:
                if detailed:
                    await ret.append(Anime(i['id']))
                else:
                    ani = data_classes.Anime()
                    for k,v in i.items():
                        setattr(ani,k,v)
                    ret.append(ani)
            return ret

async def Trending(detailed=False):
    r = await client.get("{}/anime/trending".format(BASE_URL))
    if r.status==200:
        r = await r.json()
        ret = {"being_watched":[],"popular_today":[]}
        for i in r['being_watched']:
            ani = data_classes.Anime()
            ani.id = int(i['slug'].split("-")[0])
            for k,v in i.items():
                setattr(ani,k,v)
            if detailed:
                a = await ani.detailed()
                ret['being_watched'].append(a)
            else:
                ret['being_watched'].append(ani)
        for i in r['popular_today']:
            ani = data_classes.Anime()
            ani.id = int(i['slug'].split("-")[0])
            for k,v in i.items():
                setattr(ani,k,v)
            if detailed:
                a = await ani.detailed()
                await ret['popular_today'].append(a)
            else:
                ret['popular_today'].append(ani)
        return ret

async def Releases(detailed=False):
    r = await client.get("{}/releases".format(BASE_URL))
    if r.status==200:
        r = await r.json(content_type=None)
        ret=[]
        for i in r:
            ani = data_classes.Anime()
            for k,v in i['anime'].items():
                setattr(ani,k,v)
            if detailed:
                ani = await ani.detailed()
            ap = data_classes.Release(i['created_at'],int(i['episode']),ani)
            ret.append(ap)
        return ret

