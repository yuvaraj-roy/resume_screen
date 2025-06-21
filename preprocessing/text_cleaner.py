from resume_input.resume_converter import convert_to_text
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

STOPWORDS =set(stopwords.words('english'))

def clean_text(raw_text: str)->str:
    """
    Cleans the raw resume text by
    - Lowercasing
    - Removing punctuation
    - Removing stopwords
    - Removing extra whitespace
    """
    text = raw_text.lower()

    text = re.sub(r'[^a-z\s]','',text)

    words = text.split()

    filtered_words = [word for word in words if word not in STOPWORDS]

    cleaned_text = ' '.join(filtered_words)

    return cleaned_text