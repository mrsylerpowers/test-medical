import os


class Config:
    """Set Flask configuration vars from .env file."""

    SQLALCHEMY_BINDS = {
        'users': 'sqlite:///medical_test_uid_1.db',
        'patient': 'sqlite:///medical_test_pat_1.db'
    }
    SECRET_KEY = os.urandom(32)