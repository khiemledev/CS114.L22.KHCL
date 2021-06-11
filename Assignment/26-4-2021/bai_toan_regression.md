# CS114.L22.KHCL

## Thành viên nhóm

- Lê Trần Trọng Khiêm - 19521689
- Trần Tiến Hưng - 19521587
- Lê Đặng Đăng Huy - 19521612

## Một số bài toán regression trong thực tế

### 1. Dự đoán giá xe

Dự đoán giá của một chiếc xe dựa vào các thông tin cơ bản như hãng xe, đời xe, loại xe, mã lực, số cầu...

Input:

- Hãng xe: string
- Đời xe: int
- Loại xe: string
- Mã lực: float
- Số cầu: int

Output: giá xe (float)

Cách thu thập data: tìm thông tin về xe trên website chính thức của các hãng xe và đại lý xe. Chỉ thu thập thông tin cần thiết, có ảnh hưởng đến giá của chiếc xe.

Cách xử lý data:

- Loại bỏ các giá trị NULL (có thể fill với giá trị trung bình của cột hoặc giá trị xuất hiện nhiều nhất đối với cột có kiểu string)

### 2. Dự đoán số người mắc covid19

Dự đoán số ca mắc covid19 trong ngày kế tiếp dựa trên số ca mắc bệnh ngoài cộng đồng trong 20 ngày gần nhất.

Input: 20 feature, mỗi feature là một con số thể hiện số người nhiễm covid19, theo thứ tự trước đó từ 1 đến 20 ngày.

Output: Số người mắc covid19 trong ngày tiếp theo

Thu thập dữ liệu: Thu thập từ các trang covid tracker, đặc biệt là thông tin được tổng hợp từ [JHU CSSE Covid19 Data](https://github.com/CSSEGISandData/COVID-19). Nếu như số người nhiễm covid ở ngày hiện tại là label thì số người nhiễm ở mỗi 20 ngày trước đó là feature.

Xử lý dữ liệu: Loại bỏ các thông tin bị NULL
