import requests
import shutil
import nltk
""" !pip install spacy
!python -m spacy download en_core_web_sm
!pip install -U NLTK
nltk.download('punkt_tab')
!pip install scipy
!pip install sumy """
import sumy
from bs4 import BeautifulSoup # get clean data
from googlesearch import search #google search for the content
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.edmundson import EdmundsonSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
#nltk.download('punkt_tab')

url = 'https://pipingtech.com/resources/faqs/what-is-u-stamp-certification/'
keyword = "U-stamp"
web = requests.get(url)
web.encoding = "utf-8"
soup = BeautifulSoup(web.text, "html.parser")
dived = soup.find_all('div')
paragraph = [ct.get_text(strip=True) for ct in dived if keyword in ct.get_text()]

text = " ".join(paragraph)

# 設計語言以及懲罰詞(有缺點)
LANGUAGE = "english"
bonus_words = ["important", "significant", keyword]  # 重要詞
stigma_words = ["example", "however", "thus","SupportsExpansion","Gallery","TX",".com"]  # 懲罰詞
null_words = get_stop_words(LANGUAGE)  # 停用詞


parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))

# https://www.geeksforgeeks.org/mastering-text-summarization-with-sumy-a-python-library-overview/
summarizer = EdmundsonSummarizer(Stemmer(LANGUAGE))
summarizer.bonus_words = bonus_words
summarizer.stigma_words = stigma_words
summarizer.null_words = null_words


summary_sentences = summarizer(parser.document, 1)

summary = " ".join(str(sentence) for sentence in summary_sentences)

print(summary)
