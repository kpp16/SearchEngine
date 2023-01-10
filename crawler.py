from urllib.request import urlopen
from bs4 import BeautifulSoup
from linkQueue import Queue
from stopWordsremoval import WordProcessor
import uuid

class Crawler:
    def __init__(self) -> None:
        self.link_queue = Queue()
        self.num_pages = 250
        self.cur_pages = 0
        self.seed = "https://en.wikipedia.org/wiki/Main_Page?action=render"
        self.stop_crawling = False


    def write_data(self, url: str, collections) -> None:
        if self.cur_pages >= self.num_pages:
            self.stop_crawling = True
            return

        self.cur_pages += 1
        # url = "https://en.wikipedia.org/wiki/Third_Punic_War"
        try:
            page = urlopen(url)
        except Exception as e:
            print("Error opening url: ", e)
            return

        page_bytes = page.read()
        html = page_bytes.decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")

        data: str = soup.get_text()

        docID = uuid.uuid4()

        print("Writing data...")

        back_links = self.get_links(url)

        wp = WordProcessor()

        words = wp.process_doc(data)

        json_data = {
            "doc_ID": str(docID),
            "data": words,
            "url": url,
            "back_links": back_links
        }

        try:
            collections.insert_one(json_data)
            print("Data inserted successfully...")
        except Exception as e:
            print("Error inserting data: ", e)



    def get_links(self, url: str) -> list:
        page = urlopen(url)

        page_bytes = page.read()
        html = page_bytes.decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")

        links: list = soup.find_all("a")
        filtered_links: list = []

        for link in links:
            try:
                # print(link["href"])
                if (link["href"][:8] == "https://"):
                    self.link_queue.push(link["href"])
                    filtered_links.append(link["href"])
                elif link["href"][:2] == "//":
                    new_link = "https:" + link["href"]
                    self.link_queue.push(new_link)
                    filtered_links.append(new_link)
            except:
                continue
        
        return filtered_links
