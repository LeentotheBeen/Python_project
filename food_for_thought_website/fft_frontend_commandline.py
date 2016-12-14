# display articles and allow the user to add/remove from to-read and have-read Lists

#To Do list:
# -ability to remove article from list
# -front end interface
# -ability to open the link from the article
# -refactor (do I need another backend file?)
# -if I have time:
#     -ability to find articles from different sources
#     -ability to sort (top, latest, popular)
#     -manual inputs for articles

from urllib2 import urlopen
from json import load
from json import dump

from article_class import Article

with open("news_api_keys.txt") as apiKey:
    apiKey = apiKey.readline()

all_articles = []
user_list = []

def call_api():
    # sort_by = choose_sort()
    # source = choose_source()
    source = "google-news"
    sort_by = "top"

    apiUrl = "https://newsapi.org/v1/articles?source=" + source + "&sortBy=" + sort_by + "&apiKey=" + apiKey
        #open the apiUrl and assign data to variable
    response = urlopen(apiUrl)
    json_obj = load(response)
    list_of_articles = json_obj['articles']
    return list_of_articles

# def choose_sort():
#     # sortBy = [top, latest, popular] top is default
#     if int(sort_user_choice) == 1:
#         sort_by = "top"
#     elif int(sort_user_choice) == 2:
#         sort_by = "latest"
#     elif int(sort_user_choice) == 3:
#         sort_by = "popular"
#     else:
#         print "Your selection is not valid. Choose 1 - 3."
#     return sort_by
    #pass

# def choose_source(source_option):
#     # category = "business, entertainment, gaming, general, music, science-and-nature, sport, technology"
#         #can add source and sortBy layer
#         # source = google, etc.
#     pass

def get_list_of_articles():
    #setup function that populates to all_articles list
    list_of_articles = call_api()
    for article_dict in list_of_articles:
        article_obj = Article(article_dict['title'], article_dict['author'],
        article_dict['description'], article_dict['url'], article_dict['publishedAt'])
        all_articles.append(article_obj)

def article_format_full(article_obj):
    #formats how the user will view each article info in full
    print 'Title: "' + article_obj.title + '"'
    print 'By ' + article_obj.author
    print 'Description: ' + article_obj.description
    print 'URL: ' + article_obj.url
    print ''

def article_format_short(article_obj):
    #formats how the user will view each article info in short
    print 'Title: "' + article_obj.title + '"'
    print 'URL: ' + article_obj.url
    print ''

def display_recent_articles_with_index(top_articles):
    #shows top articles from the API with an index number attached
    index_num = 1
    for article in top_articles:
        print index_num
        index_num += 1
        article_format_full(article)

def return_article_titles():
    get_list_of_articles()
    display_recent_articles_with_index

# def view_more_article_details():
#     pass

def display_to_read_list():
    print "To Read List:\n"
    for article in user_list:
        if article.status == "To Read":
            article_format_short(article)

def display_have_read_list():
    print "Have Read List:\n"
    for article in user_list:
        if article.status == "Have Read":
            article_format_short(article)

def add_article_to_user_list():
    ask_to_add = raw_input("Do you want to add one of these articles to your list? ")
    while(True):
        if ask_to_add == "yes":
            user_choice = int(raw_input("Give the index number for article you want to add.\n"))
            article_index = user_choice - 1
            if user_choice <= len(all_articles):
                user_list.append(all_articles[article_index])
                save_data(user_list)
            else:
                print "Error: Please select a valid article index."
            return article_format_short(all_articles[article_index])
        else:
            break

def change_status():
    ask_to_change_status = raw_input("Do you want to mark an article as read? ")
    while(True):
        if ask_to_change_status == "yes":
            user_choice = int(raw_input("Give the index number for article you want to change.\n"))
            article_index = user_choice - 1
            if user_choice <= len(user_list):
                user_list[article_index].change_status_to_have_read()
                save_data(user_list)
            else:
                print "Error: Please select a valid article index."
            return article_format_short(user_list[article_index])
        else:
            break

def remove_article_from_user_list():
    ask_to_remove = raw_input("Are you sure you want to remove article from you list?")
    while(True):
        if ask_to_remove == "yes":
            user_choice = int(raw_input("Give the index number for article you want to add.\n"))
            if user_list(user_choice): #reqs a counter to automatically create an index number for the entry
                user_list.remove(user_choice)
                save_data(user_list)
            else:
                print "Error: Please select a valid article index."
            return article_format_short(all_articles[article_index])
        else:
            break

def display_main_menu():
    print """
    1 - View articles to add
    2 - View To Read list
    3 - View Have Read list
    4 - Exit
    """

def save_data(user_list):
    with open("user_saved_articles.json", mode = "w") as exported_data:
        for article_obj in user_list:
            temp_dict = article_obj.turn_to_dict()
            dump(temp_dict, exported_data)

#for viewing saved data later on
# def open_data():
#     with open("user_saved_articles.json", 'r') as f:
#         user_list = json.load(f)
#         return user_list

def main():
    #test functions
    # print call_api()
    # get_list_of_articles()
    # display_recent_articles(all_articles)
    # print all_articles
    # print display_recent_articles(top_articles)
    # print choose_sort()
    # open_data()

    print """\nWelcome to Food for Thought!\n
    An app to save all those online news articles you want to read for later."""

    while(True):
        "Select from the following menu of options. "
        get_list_of_articles()
        display_main_menu()
        user_choice = int(raw_input("Select one of the options: "))
        #1 - View articles to add, option to add
        if user_choice == 1:
            display_recent_articles_with_index(all_articles)
            add_article_to_user_list()
        #2 - View To Read list
        elif user_choice == 2:
            display_to_read_list()
            change_status()
            add_article_to_user_list()
            remove_article_from_user_list()
            #give them choice to add more, remove, or change to have read
        #3 - View Have Read list
        elif user_choice == 3:
            display_have_read_list()
        #4 - Exit
        elif user_choice == 4:
            break
        else:
            print "Sorry, that's not an option. Select again."

if __name__ == '__main__':
    main()
