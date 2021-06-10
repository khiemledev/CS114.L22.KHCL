# CS114.L22.KHCL

## Thành viên

- Lê Trần Trọng Khiêm
- Trần Tiến Hưng
- Lê Đặng Đăng Huy

## Cách chạy tool crawl dữ liệu

Đầu tiên phải cài đặt scrapy trước. Sau khi cài thì chạy các câu lệnh sau:

```
cd headlinesbot
scrapy crawl thedailywtf -O output_file.json
scrapy crawl theonion -O output_file.json
scrapy crawl walkingeaglenews -O output_file.json
```