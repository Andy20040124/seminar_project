import requests
import shutil
import nltk
from bs4 import BeautifulSoup # get clean data
from googlesearch import search #google search for the content
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.edmundson import EdmundsonSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
nltk.data.path.append("C:/Users/andy/AppData/Roaming/nltk_data")

url = 'https://pipingtech.com/resources/faqs/what-is-u-stamp-certification/'
keyword = "U-stamp"
web = requests.get(url)
web.encoding = "utf-8"
soup = BeautifulSoup(web.text, "html.parser")
dived = soup.find_all('div')
paragraph = [ct.get_text(strip=True) for ct in dived if keyword in ct.get_text()]

text = " ".join(paragraph)

# 設定語言
LANGUAGE = "english"
bonus_words = ["important", "significant", "key", keyword]  # 重要詞
stigma_words = ["example", "however", "thus"]  # 懲罰詞
null_words = get_stop_words(LANGUAGE)  # 停用詞

# 創建解析器
parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))

# Edmundson 摘要器
summarizer = EdmundsonSummarizer(Stemmer(LANGUAGE))
summarizer.bonus_words = bonus_words
summarizer.stigma_words = stigma_words
summarizer.null_words = null_words

# 設定摘要句數
summary_sentences = summarizer(parser.document, 3)
summary = " ".join(str(sentence) for sentence in summary_sentences)

print("\n摘要結果：\n", summary)
