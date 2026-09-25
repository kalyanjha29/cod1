import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'instance', 'attendance.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
    EMBEDDINGS_FOLDER = os.path.join(BASE_DIR, 'static', 'models')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  
    
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}