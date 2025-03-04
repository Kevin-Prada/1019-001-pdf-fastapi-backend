import os
import cloudinary
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_HOST: str
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: int
    app_name: str = "Full Stack PDF CRUD App"
    CLOUDINARY_URL: str

    @staticmethod
    def setup_cloudinary():
        cloudinary.config(
            cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME', 'dyje6aftb'),
            api_key=os.environ.get('CLOUDINARY_API_KEY', '175786421248115'),
            api_secret=os.environ.get('CLOUDINARY_API_SECRET', 'LvO2ZGWpKMNzuVXrmcMgyC_HlPk')
        )

    class Config:
        env_file = ".env"
        extra = "ignore"
