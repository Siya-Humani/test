from app import db

class GameState(db.Model):
    __tablename__ = 'game_state'  # Ensure this matches the table name
    __table_args__ = {'extend_existing': True}  # Add this line to avoid the error
    
    id = db.Column(db.Integer, primary_key=True)
    user_ip = db.Column(db.String(120), unique=True)
    # Add other columns...
