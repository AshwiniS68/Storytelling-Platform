from flask import Flask, request, render_template
import story_generator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = {
            'genre': request.form['genre'],
            'theme': request.form['theme'],
            'characters': request.form['characters']
        }
        story = story_generator.generate_story(user_input)
        choice = story_generator.generate_choice(story)
        return render_template('index.html', story=story, choice=choice)
    return render_template('index.html')

@app.route('/update-story', methods=['POST'])
def update_story():
    story = request.form['story']
    choice = request.form['choice']
    updated_story = story_generator.update_story(story, choice)
    return render_template('index.html', story=updated_story)

if __name__ == '__main__':
    app.run(debug=True)