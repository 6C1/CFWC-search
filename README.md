CFWC
====

Tools for the Cool Freaks' Wikipedia Club.

Forked from DanielPorter's FBNR tool; he's the real hero, and wrote 79.99% of the code. Also big shoutout to SlickGrid

## Workflow
How to use this:

1. put the table on the internet somewhere
2. run fbscrape.py with arguments <access_token> <groupid> to generate posts.json
3. repeat step two as often as you want

### Scripts
The scripts are for pulling down and manipulating group data. 

The script fbscrape.py is for pulling down the data. To grab group data you need: 1. an access token, which you can get from https://developers.facebook.com/tools/explorer/ with permissions to access groups, and 2. the group ID, which you can find by clicking around in the graph explorer. The output is a list of json objects, each object is a post to the group.

The list of users is generated from the list of posts. Thus contains only users who have posted to the group's wall (and the post has not been deleted + has been successfully grabbed using fbscrape.py).

### Table
The table takes posts.json as input and allows users to view the posts from the repository.

###Known Issues
Some json objects returned by the call to Facebook Graph API do not appear to include any details about the link, even though viewing the post on Facebook clearly shows the link preview box. This has been worked-around for some cases, by parsing the article from the actual URL in the comment, but in cases where the URL is not present either, the article name remains blank.

