from app import application
from flask import request
import random

description = "This page is to simulate a Tictactoe game"
label = "TicTacToe"
is_blank_page = True

def get_script(board_state):
        return f"""
                <script type="application/json">
                (function(){{
                const player_one_input = document.getElementById("player-one-input");
                const player_two_input =document.getElementById("player-two-input");
                const player_one_button = document.getElementById("player-one-button");
                const player_two_button =document.getElementById("player-two-button");
                const restart_button = document.getElementById("restart-button");
                const begin_button = document.getElementById("pick-random-player");

                const board_state = {board_state};

                const post = async (turn, board, position) => {{ 
                   const response = await fetch("/tictactoe", {{
                        headers: {{ "Content-Type": "application/json" }},
                        method: "POST",
                        body: JSON.stringify({{turn, board, position}})
                    }})
                   const data = await response.json()
                   document.getElementById("pythondo-app-container").innerHTML = data.html
                 }}
                const get = async (turn, board, position) => {{ 
                   const response = await fetch("/tictactoe", {{
                        headers: {{ "Content-Type": "application/json" }},
                    }})
                   const data = await response.json()
                   document.getElementById("pythondo-app-container").innerHTML = data.html
                 }}

                 if(player_one_button) {{
                    player_one_button.addEventListener("click", async event => {{
                        const value = player_one_input.value;
                        await post("Player 1", board_state, Number(value))
                    }})
                 }}
                 if(player_two_button) {{
                    player_two_button.addEventListener("click", async event => {{
                        const value = player_two_input.value;
                        await post("Player 2", board_state, Number(value))
                    }})
                 }}

                 begin_button.addEventListener("click", async event => {{
                    await post(false, board_state, 0)
                 }})
                restart_button.addEventListener("click", async event => {{
                    await get()
                 }})
                }})()
                </script>
                """



def get_style():
        return """<style>*{ margin:0;padding:0;box-sizing:border-box;font-family:Arial,Helvetica,sans-serif }.container{min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;background:#eee}h1{font-size:5rem;margin-bottom:.5em}h2{margin-top:1em;font-size:2rem;margin-bottom:.5em}.play-area{display:grid;width:300px;height:300px;grid-template-columns:auto auto auto}.block{display:flex;width:100px;height:100px;align-items:center;justify-content:center;font-size:3rem;font-weight:700;border:3px solid #000;transition:background .2s ease-in-out}.block:hover{cursor:pointer;background:#0ff30f}.occupied:hover{background:#ff3a3a}.win{background:#0ff30f}.win:hover{background:#0ff30f}#block_0,#block_1,#block_2{border-top:none}#block_0,#block_3,#block_6{border-left:none}#block_6,#block_7,#block_8{border-bottom:none}#block_2,#block_5,#block_8{border-right:none}button{outline:0;border:4px solid green;padding:10px 20px;font-size:1rem;font-weight:700;background:0 0;transition:all .2s ease-in-out}button:hover{cursor:pointer;background:green;color:#fff}.playerWin{color:green}.computerWin{color:red}.draw{color:#ff4500}@media only screen and (max-width:600px){h1{font-size:3rem;margin-bottom:.5em}h2{margin-top:1em;font-size:1.3rem}}</style>"""
def display_board(board, message, turn):
    return f"""
            {get_style()}
            <div id="tictactoe" class="container">
                <h1>Tic-Tac-Toe</h1>
                <h3>{message}</h3>
                <div>
                    { '<button id="pick-random-player">Begin</button></p>' if turn == "Start" else ''}
                    {'<p>Player 1 is <strong>X</strong> <input id="player-one-input" /> <button id="player-one-button">Submit</button></p>' if turn == 'Player 1' else ''}
                    {'<p>Player 2 is <strong>O</strong> <input id="player-two-input" /> <button id="player-two-button">Submit</button></p>' if turn == 'Player 2' else ''} 
                    <p><button id="restart-button" >Restart</button></p>
                </div>
                <div class="play-area">
                    <div id="block_0" class="block">{board[1]}</div>
                    <div id="block_1" class="block">{board[2]}</div>
                    <div id="block_2" class="block">{board[3]}</div>
                    <div id="block_3" class="block">{board[4]}</div>
                    <div id="block_4" class="block">{board[5]}</div>
                    <div id="block_5" class="block">{board[6]}</div>
                    <div id="block_6" class="block">{board[7]}</div>
                    <div id="block_7" class="block">{board[8]}</div>
                    <div id="block_8" class="block">{board[9]}</div>
                </div>
            </div>
            {get_script(board)}
            """
def win_check(board,mark):
    
    return(
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[3] == mark and board[5] == mark and board[7] == mark)
    )
def place_marker(board,marker,position):
    
    board[position] = marker
def space_check(board,position):
    
    return board[position] == ' '
def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    # the board is full
    return True
def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
@application.route("/tictactoe", methods=["POST", "GET"])

def tictactoe():
    if request.method == 'GET':
        board = display_board([' ']*10, " ", "Start")
        return {
            "html": board
        }

    elif request.method == 'POST':
        content = request.json
        the_board = content['board']

        player1_marker, player2_marker = ("X", "O")
        who_won = ""
        turn = content['turn'] if content['turn'] else choose_first()
             
        if turn == 'Player 1':
            
            position = content['position']
            
            #place a marker in the position
            place_marker(the_board,player1_marker, position)
            
            #check if they whon
            if win_check(the_board,player1_marker):
                who_won = 'Player 1 Won'
            else:
                if full_board_check(the_board):
                    who_won = 'There is a Tie'
                else:
                    turn = 'Player 2'
        
        else:
            
            position = content['position']
            
            #place a marker in the position
            place_marker(the_board,player2_marker, position)
            
            #check if they whon
            if win_check(the_board,player2_marker):
                who_won = 'Player 2 Won'
            else:
                if full_board_check(the_board):
                    who_won = 'There is a Tie'
                else:
                    turn = 'Player 1'
    
    board = display_board(the_board, who_won, turn)
    return {
            "html": board
    }