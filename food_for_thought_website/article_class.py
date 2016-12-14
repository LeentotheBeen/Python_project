class Article(object):
    def __init__(self, title, author, description, url, published_date, status="To Read"):
    #Add this attributes later: added_date, status, category
        # self.index = index (make sure that each obj has index value)
        self.title = title
        if author == None:
            self.author = ""
        else:
            self.author = author
        self.description = description
        self.url = url
        self.published_date = published_date
        # self.added_date = ""
        self.status = status
        # self.category = ""
    def change_status_to_have_read(self):
        self.status = "Have Read"
    def turn_to_dict(self):
        temp_dict = {}
        temp_dict['title'] = self.title
        temp_dict['author'] = self.author
        temp_dict['description'] = self.description
        temp_dict['url'] = self.url
        temp_dict['published_date'] = self.published_date
        temp_dict['status'] = self.status
        return temp_dict

# def main():

#test
    # article_001 = Article(
    #     'Israel Defense Forces Kill 4 ISIS-Linked Attackers in Golan Heights',
    #     'Isabel Kershner',
    #     'The firefight, near Syria, appeared to be the first deadly exchange between Israeli forces and fighters associated with the Islamic State.',
    #     'http://www.nytimes.com/2016/11/27/world/middleeast/israeli-military-kills-4-isis-linked-militants-in-golan-heights.html',
    #     '2016-11-28T05:52:19Z',
    #     "Have read")
    # article_002 = Article(
    #     'Cats are awesome',
    #     'Crazy cat lady',
    #     'The love of felines in a post-modern era.',
    #     'http://cathazcheezborger.com',
    #     '2016-11-27T06:40:19Z')
    #
    # to_read_list = []
    # to_read_list.append(article_001)
    # to_read_list.append(article_002)
    #
    # for article in to_read_list:
    #     print article.title + ", by " + article.author + article.status
    #
    # print to_read_list
