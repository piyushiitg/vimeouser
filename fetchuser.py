import urllib2
import MySQLdb.cursors
import settings
from django.core.management import setup_environ
from BeautifulSoup import BeautifulSoup
setup_environ(settings)
from vimeocrawl.models import *
def create_entry(): 
    msg = ''
    pay='NO'
    Staffpick='NO'
    Video='NO'
    try:
        crawling = fetchurl.pop()
    except:
        print "fetchurl is empty:"
        raise
    try:
        usock = urllib2.urlopen(crawling)
        msg = usock.read()
        if msg.find('data-ga-event="button|plus_badge_click|plus"')!=-1:
            pay='YES'
        if msg.find('featured_videos')!=-1:
            Staffpick='YES'
        if msg.find('recent_videos')!=-1:
            Video='YES'
        start=msg.find('title=')
        end=msg.find('Videos',start+7)
        name=msg[start+7:end-9]
        print name
        v = Vimeouserinfo.objects.create(Name=name,URL=crawling,Paying=pay,StaffPick=Staffpick,Video=Video)
    except Exception as ex:
        print ex
    return msg

def find_next_users(msg):
    urls = []
    startPos = msg.find('<ul class="profile_following">')
    if startPos != -1:
        endPos = msg.find('</ul>',startPos+3)
        if endPos != -1:
            title = msg[startPos+3:endPos]
            soup = BeautifulSoup(title)
            for a in soup.findAll('a',href=True):
                #print "Found the URL:", a['href'],a['title']
                #urls[a['href']] = a['title']
                urls.append(a['href'])
            for url in urls:
                if(vimeo_url+url not in fetchedurl):
                    fetchurl.add(vimeo_url+url)
                    fetchedurl.add(vimeo_url+url)
                    print '_________',len(fetchedurl)

fetchurl = set(["http://vimeo.com/eterea"])
fetchedurl = set([])
vimeo_url="http://vimeo.com"

if __name__ == '__main__':
    count=0
    while count <= 5000:
        print "****************",count ,fetchurl
        msg = create_entry()
        if msg != '':
            find_next_users(msg)
            count = count+1
