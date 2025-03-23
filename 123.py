import requests
import shutil
from bs4 import BeautifulSoup # get clean data
from googlesearch import search #google search for the content

def google_search(query, num_results=1):
    results = []
    try:
        for result in search(query, num_results=num_results):#search by the keyword
            results.append(result)# record first 5 website's data
    except Exception as e:
        print(f"exception happen: {e}")# report exception
    
    return results

def get_page_title(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=5)#5秒的存取權限
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.title.string if soup.title else "no title"
    except Exception as e:
        return f"can't get title ({e})"

def get_website_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=5)#5秒的存取權限
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find("div")#撇除metadata 以及style的美編資料
        if content :
            # 找到title 跟 p 當中的值
            big_title = content.find_all("title")
            paragraphs = content.find_all("p")
            
            # 🔹 5. 篩選出包含關鍵字的段落
            matching_paragraphs = [p.get_text(strip=True) for p in paragraphs  or big_title if keyword in p.get_text()]
            
        
    except Exception as e:
        return f"can't get title ({e})"

if __name__ == "__main__":
    keyword = input("請輸入關鍵字: ")
    search_results = google_search(keyword)
    
    output_lines = []
    print("\n搜尋結果:")
    for idx, link in enumerate(search_results, 1):
        title = get_page_title(link)
        get_website_content(link)
        result_line = f"{idx}. {title} - {link}"
        print(result_line)
        output_lines.append(result_line)
    with open("搜尋結果.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(output_lines))
