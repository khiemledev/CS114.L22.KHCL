# CS114.L22.KHCL

## Thành viên

- Lê Trần Trọng Khiêm
- Trần Tiến Hưng
- Lê Đặng Đăng Huy

## Cách chạy tool crawl dữ liệu

Đầu tiên phải cài đặt scrapy trước. Sau khi cài thì chạy các câu lệnh sau:

```
cd headlinesbot
scrapy crawl thedailywtf -O crawled_data/sarcasm/thedailywtf.json
scrapy crawl theonion -O crawled_data/sarcasm/theonion.json
scrapy crawl walkingeaglenews -O crawled_data/sarcasm/walkingeaglenews.json
scrapy crawl theguardian -O crawled_data/official/theguardian.json
scrapy crawl huffpost -O crawled_data/official/huffpost.json
```
