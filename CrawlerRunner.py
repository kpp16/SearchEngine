from crawler import Crawler
from dotenv import dotenv_values
from pymongo import MongoClient
from SimilarityFinder import DocStats

config = dotenv_values(".env")

def init_mongoDB():
    client = MongoClient("localhost", 27017, maxPoolSize=50)
    db = client.LinkDocsDB
    return db


def crawl_pages(crawler, cname) -> None:
    crawler.write_data(crawler.seed, cname)
    # print(crawler.link_queue.is_empty())

    while not crawler.link_queue.is_empty() and \
            crawler.stop_crawling is False:

        top_link: str = crawler.link_queue.pop()

        # print("top link: ", top_link)

        crawler.write_data(top_link, cname)
    
    print("Crawling pages done... exiting process")


def main():
    crawler = Crawler()
    db = init_mongoDB()

    # test_data = {
    #     "Name": "kai"
    # }

    cname = db["Docs"]
    # # # cname.insert_one(test_data)

    # crawl_pages(crawler, cname)

    ds = DocStats("World War 2", cname)
    links = ds.cosine_similarity()

    for link in links:
        print(link)
    

if __name__ == "__main__":
    main()
