import 章节获取
import threading

def crawl_with_step(start_chapter, book_id, step, offset=0):
    """使用步长爬取章节
    
    Args:
        start_chapter: 起始章节
        book_id: 书籍ID
        step: 步长
        offset: 偏移量
    """
    chapter_id = start_chapter + offset
    while True:
        is_finished = 章节获取.crawl_chapter(chapter_id, book_id)
        if is_finished == False:
            print(f"线程{offset}爬取完成")
            break
        print(f"线程{offset}: 第{chapter_id}章完成", end='\r')
        chapter_id += step


def start_crawling_threads(start_chapter, book_id, concurrent_count):
    """
    创建指定数量的线程，分别以指定并发次数作为步长爬取章节
    
    Args:
        start_chapter: 起始章节
        book_id: 书籍ID
        concurrent_count: 同时并发次数，默认为2
    """
    threads = []
    # 创建指定数量的线程，以并发次数作为步长爬取
    for i in range(concurrent_count):
        thread = threading.Thread(target=crawl_with_step, args=(start_chapter, book_id, concurrent_count, i))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_crawling_threads(60, 34895175, 2)
    print("所有线程爬取完成")
