import sys
import urllib2
import json
import re

# removes unwanted bloat from JSON returned from Graph API
def addJSONtoCollection(collection, objects):
    for obj in objects :
        if 'comments' in obj :
            obj['comments'].pop('paging', None)
            obj['comments'].pop('data', None)
            obj['comments'].pop('summary.order', None)
        if 'likes' in obj :
            obj['likes'].pop('paging', None)
            obj['likes'].pop('data', None)
        obj.pop('updated_time', None)
        collection.append(obj)

def main():
    access_token = sys.argv[1]
    group_id = sys.argv[2]
    url = "https://graph.facebook.com/%s?fields=feed{from,created_time,message,likes.summary(true).limit(1),comments.summary(true).limit(1),link,name}&method=GET&format=json&suppress_http_code=1&access_token=%s"
    url = url % (group_id, access_token)
    
    print("Querying Graph API with following request:\n%s" % url)
    response = urllib2.urlopen(url)
    html = response.read()
    load = json.loads(html)
    if u'error' not in load.keys():
        parsed = load["feed"]
        allposts = []
        addJSONtoCollection(allposts, parsed["data"])
        print("# of posts retrieved: %s" % len(allposts))
    
        #assumes there will be a next because i'm being lazy
        parsed['paging']['next'] = re.sub('limit=[0-9]*', 'limit=500', parsed['paging']['next'])
        while 'paging' in parsed:
            if 'next' in parsed['paging']:
                response = urllib2.urlopen(parsed["paging"]["next"])
                html = response.read()
                parsed = json.loads(html)
                addJSONtoCollection(allposts, parsed["data"])
                print("# of posts retrieved: %s" % len(allposts))
            else:
                break
        print("Saving posts to posts.json...")
        output = open('posts.json', 'w')
        output.write("posts =")
        output.write(json.dumps(allposts))
        output.close()
        print("Done!")
    else:
	print load[u'error'][u'type']+": "+load[u'error'][u'message']
if __name__ == "__main__":
    main()
