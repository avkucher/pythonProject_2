from flask import Flask

import utils

app = Flask(__name__)

@app.route('/',)
def page_index():

    candidates = utils.get_candidates_all()
    page_content = ''

    for candidate in candidates:
        page_content += candidate['name'] + '\n'
        page_content += candidate['position'] + '\n'
        page_content += candidate['skills'] + '\n'
        page_content += '\n'

    return '<pre>' + page_content + '</pre>'


@app.route('/skill/<skill_name>')
def page_skill(skill_name):

    candidates = utils.get_candidates_by_skill(skill_name)
    page_content = ''

    for candidate in candidates:
        page_content += candidate['name'] + '\n'
        page_content += candidate['position'] + '\n'
        page_content += candidate['skills'] + '\n'
        page_content += '\n'

    return '<pre>'+page_content+'</pre>'

@app.route('/candidats/<int:uid>')
def page_candidate(uid):

    candidate = utils.get_candidate_by_id(uid)
    page_content = ''

    page_content = f'<pre>'
    page_content += candidate['name'] + '\n'
    page_content += candidate['position'] + '\n'
    page_content += candidate['skills'] + '\n'

    return '<pre>'+page_content+'</pre>'

app.run()