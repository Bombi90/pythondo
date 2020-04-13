from app import application
from flask import request

description = "This page is used to check how long is one or more words"
label = "Letters Count"

@application.route("/letterscount", methods=["POST"])
def letterscount():
        content = request.json
        word:str = content['word']
        lenght = len(word)
        no_space_lenght = lenght - word.count(' ')
        
        result = '''
        The word {} has {} characters
        and {} characters without spaces
        '''.format(word, lenght, no_space_lenght)
        
        return {
        "result": result
            }