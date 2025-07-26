import 章节获取

chapter_id = 60
book_id = 34895175

while True:
    is_finished = 章节获取.crawl_chapter(chapter_id, book_id)
    
    if is_finished == False:
        print(f"爬取完成")
        break
    
    print(f"第{chapter_id}章完成", end='\r')
    chapter_id += 1
