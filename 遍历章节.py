import 章节获取


def crawl_chapters(book_id):
    """遍历章节"""
    chapter_id = 1
    while True:
        is_finished = 章节获取.crawl_chapter(chapter_id, book_id)

        if is_finished == False:
            break

        print(f"第{chapter_id}章完成", end='\r')
        chapter_id += 1


if __name__ == "__main__":
    crawl_chapters(34895175)
    print("遍历完成")
