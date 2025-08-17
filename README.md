# QQ阅读爬取

## 依赖

```shell
pip install requests playwright selectolax && python -m playwright install
```

## 使用方法

需要下载编译器编译

<https://gitee.com/LZY4/xiaoyi>

然后构建

```shell
git clone https://gitee.com/LZY4/qq-reading-crawling.git
cd qq-reading-crawling
make
```

构建后的产物在 `build` 目录

完成之后请先运行 `登录.py` 初始化

## 提示

- 书籍ID 可在 URL 中找到 `bid`

- 创世中文网的账号跟QQ阅读是互通的
