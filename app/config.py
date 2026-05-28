import os

class Config:
    # Security
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-funny-key'
    
    # Base directory
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    
    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'instance', 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Storage
    VIDEOS_FOLDER = os.path.join(BASE_DIR, 'videos')
    QUEUE_FOLDER = os.path.join(BASE_DIR, 'queue')
    
    # Upload settings
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024 # 50 MB max-limit
    ALLOWED_EXTENSIONS = {'mp4', 'webm', 'ogg'}
    
    # Admin credentials
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME') or 'admin'
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD') or 'password'

    # Rate limiting (shared across uWSGI workers via Redis)
    RATELIMIT_STORAGE_URI = os.environ.get('REDIS_URL') or 'memory://'
    RATELIMIT_STRATEGY = 'fixed-window'
    RATELIMIT_HEADERS_ENABLED = True
