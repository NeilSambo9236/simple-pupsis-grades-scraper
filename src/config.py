import os
from dotenv import load_dotenv

load_dotenv()

STUDENT_NUMBER = os.getenv("STUDENT_NUMBER")
PASSWORD = os.getenv("PASSWORD")

BIRTH_MONTH = os.getenv("BIRTH_MONTH")
BIRTH_DAY = os.getenv("BIRTH_DAY")
BIRTH_YEAR = os.getenv("BIRTH_YEAR")
