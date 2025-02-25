from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./salon.db"
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    STRIPE_SECRET_KEY: str = "your-stripe-secret-key"
    
    class Config:
        env_file = ".env"

settings = Settings() 