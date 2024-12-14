from app import app, db
from models import GameState

with app.app_context():
    db.create_all()  # Creates the `gamestate` table if it doesn't exist

    # Initialize GameState if not already present
    if not GameState.query.first():
        game_state = GameState(has_played=False, prize_won=False, user_ip=None)
        db.session.add(game_state)
        db.session.commit()
        print("GameState initialized!")
from app import app, db
from models import GameState

with app.app_context():
    # Clear previous metadata if needed
    db.metadata.clear()

    # Create all tables (if they don't exist)
    db.create_all()

    # Initialize GameState if not already present
    if not GameState.query.first():
        game_state = GameState(prize_won=False, has_played=False, user_ip=None)
        db.session.add(game_state)
        db.session.commit()

    print("GameState initialized!")
