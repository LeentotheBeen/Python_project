from flask import Flask, render_template
from random import randint
import fft_frontend

app = Flask(__name__)

# def show_articles():
#     display_recent_articles_with_index(all_articles)
#     add_article_to_user_list()

@app.route('/')
def index():
    articles = ["article title", "another article title"]
    return render_template('index.html', articles = articles)

    # "<html><body><h1>" + fft_frontend.return_article_titles() + "</h1></body></html>"
    # return "<html><body><h1>I am changing the landing page</h1></body></html>"

@app.route('/articles')
def articles():
  return fft_frontend.return_article_titles()

@app.route('/lucky')
def lucky_number():
  lucky_num = randint(1, 10)
  lucky_message = "Your lucky number is %s" % lucky_num
  return "<html><body><h1>" + lucky_message + "</h1></body></html>"

if __name__ == "__main__":
  app.run(debug=True)
