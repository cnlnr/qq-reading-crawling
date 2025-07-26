# 检查是否全书完
div_book_end = parser.css_first('div.book-end.ypc-column-name')
if div_book_end:
    print("全书完")
