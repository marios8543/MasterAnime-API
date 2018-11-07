from masteranime_blocking import Anime,Trending,Releases,Search,loop
from masteranime import client

def interface(i):
    if i==1:
        id = input("Enter anime id or enter to cancel\n")
        if not id or id=="":
            return
        ani = Anime(id)
        if ani:
            print(str(ani))
        else:
            return print("Anime not found")
    elif i==2:
        q = input("Enter your search query\n")
        res = Search(q)
        if res:
            for i,v in enumerate(res):
                print(i+1,". ",v.title)
            q = int(input("Enter a number from the list\n"))
            if q-1<len(res):
                print(str(res[q-1]))
            else:
                print("Invalid option")
        else:
            return print("No results for query")
    elif i==3:
        res = Trending()
        if res:
            q = int(input("""
            1. Being watched
            2. Popular today
            \n"""))
            if q==1:
                res = res['being_watched']
                for i,v in enumerate(res):
                    print(i+1,". ",v.title)
                q = int(input("Enter a number from the list\n"))
                if q-1<len(res):
                    print(str(res[q-1]))
                else:
                    print("Invalid option")
            elif q==2:
                res = res['popular_today']
                for i,v in enumerate(res):
                    print(i+1,". ",v.title)
                q = int(input("Enter a number from the list\n"))
                if q-1<len(res):
                    print(str(res[q-1]))
                else:
                    print("Invalid option")
            else:
                print("Invalid option")
    elif i==4:
        res = Releases()
        if res:
            for i,v in enumerate(res):
                print(i+1,". ",v.anime.title)
            q = int(input("Enter a number from the list\n"))
            if q-1<len(res):
                print(str(res[q-1]))
            else:
                print("Invalid option")
    elif i==5:
        return             
    else:
        return print("Invalid option")

            
i=0
while i!=5:
    i = int(input(
    """
    1. Fetch anime by id
    2. Search anime by name
    3. Fetch trending anime
    4. Fetch releasing anime
    5.Exit
    \n"""))
    interface(i)
loop.run_until_complete(client.close())
