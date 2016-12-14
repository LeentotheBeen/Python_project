from flask import Flask, render_template
from random import randint
import fft_program

app = Flask(__name__)

# def show_articles():
#     display_recent_articles_with_index(all_articles)
#     add_article_to_user_list()

@app.route('/')
def index():
    articles = fft_program.return_articles_for_display()
    return render_template('index.html', articles = articles)

@app.route('/articles')
def articles():
  return fft_program.return_article_titles()

@app.route('/lucky')
def lucky_number():
  lucky_num = randint(1, 10)
  lucky_message = "Your lucky number is %s" % lucky_num
  return "<html><body><h1>" + lucky_message + "</h1></body></html>"

if __name__ == "__main__":
  app.run(debug=True)
