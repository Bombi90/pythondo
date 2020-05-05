from app import application
from flask import request

description = "This page is to simulate a Blackjack's hand"
label = "Blackjack"

@application.route("/blackjack", methods=["POST"])

def blackjack():
    if request.method == 'POST':
        
        content = request.json
        data = content['data']
        a = data['a']
        b = data ['b']
        c = data ['c']
        score = a+b+c
    
        if score <= 21:
            return {
            "result": score
            }
        elif score <=31 and 11 in (a,b,c):
            return {
            "result": score - 10
            }
        else:
            return {
            "result" : "BUST"
            }
    
    
    