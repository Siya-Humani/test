from flask import Flask, render_template, redirect, url_for, request, session, jsonify
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Path to the file that will track the number of winners
WINNER_FILE = 'winners_count.txt'
MAX_WINNERS = 200

# Initialize the file if it doesn't exist
if not os.path.exists(WINNER_FILE):
    with open(WINNER_FILE, 'w') as f:
        f.write('0')

def get_winner_count():
    """Get the current number of winners from the file."""
    with open(WINNER_FILE, 'r') as f:
        return int(f.read().strip())

def increment_winner_count():
    """Increment the winner count in the file."""
    current_count = get_winner_count()
    if current_count < MAX_WINNERS:
        current_count += 1
        with open(WINNER_FILE, 'w') as f:
            f.write(str(current_count))
    return current_count

@app.route('/')
def index():
    """Render the main game page."""
    winner_count = get_winner_count()

    # If user has already played, redirect to tryagain
    if session.get('has_played', False):
        return redirect(url_for('try_again'))

    return render_template('index.html', winner_count=winner_count, max_winners=MAX_WINNERS)

@app.route('/spin', methods=['POST'])
def spin():
    """Handle spin and determine if the user wins."""
    winner_count = get_winner_count()

    # If the number of winners is less than the max allowed and user hasn't played yet
    if winner_count < MAX_WINNERS:
        if session.get('has_played', False):
            return redirect(url_for('try_again'))  # Prevent user from playing again
        
        # Simulate the landing on the prize slice (for demonstration purposes)
        prize_landed = request.form.get('landed_on_prize') == 'true'  # Simulate if user landed on prize

        # Mark that the user has played
        session['has_played'] = True

        if prize_landed:
            new_winner_count = increment_winner_count()
            if new_winner_count <= MAX_WINNERS:
                return redirect(url_for('prize'))
            else:
                return redirect(url_for('all_winners'))
        else:
            return redirect(url_for('try_again'))

    return redirect(url_for('all_winners'))

@app.route('/prize')
def prize():
    """Page shown when the user wins."""
    return render_template('prize.html')

@app.route('/tryagain')
def try_again():
    """Page shown when the user doesn't win or tries to play more than once."""
    return render_template('tryagain.html')

@app.route('/allwinners')
def all_winners():
    """Page shown when the maximum number of winners is reached."""
    return render_template('allwinners.html')

if __name__ == '__main__':
    app.run(debug=True)

