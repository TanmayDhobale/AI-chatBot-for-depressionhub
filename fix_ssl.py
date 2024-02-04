import ssl
import nltk

# Create an SSL context
ssl._create_default_https_context = ssl._create_unverified_context

# Download NLTK data
nltk.download('punkt')
