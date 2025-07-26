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
        print(f"线程{offset}: 第{chapter_id}章完成")
        chapter_id += step

if __name__ == "__main__":
    # 创建两个线程，分别以步长2爬取
    t1 = threading.Thread(target=crawl_with_step, args=(60, 34895175, 2, 0))  # 爬取 60, 62, 64...
    t2 = threading.Thread(target=crawl_with_step, args=(60, 34895175, 2, 1))  # 爬取 61, 63, 65...
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
