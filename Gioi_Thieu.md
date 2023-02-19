- Mạng máy tính sử dụng phổ biến, các máy tính trong mạng cùng kết nối Internet
- Lỗ hổng mạng có dây / không dây -> truy cập khôngg chứng thực đến mạng
- Tấn công từ thiết bị của kẻ tấn công qua `hubb/switch` không an toàn.
- Mạng không dây `ít` an toàn mạng có dây
# 1. Tấn công mạng
- Thu thập gói tin ăn cắp thông tin
- Từ chối dịch vụ người dùng = các gói giả mạo
- Giả mạo địa chỉ vật lí (MAC) máy chủ hợp pháp -> đánh cắp dữ liệu -> tấn công
# 2. Nghi thức mạng
- Tập hợp quy tắc điều khiển truyền thông giữa các thiết bị kết nối trên mạng
- Cơ chế tạo kết nối, định dạng đóng gói dữ liệu gói tin gửi & nhận
- `Nghi thức TCP/IP` phổ iến, sử dụng rộng
![image](https://user-images.githubusercontent.com/88178841/219944335-d3b1ac3f-b70e-41d0-babe-48d695c74440.png)

# 3. Nghi thức TCP/IP
- Ra đời 1908
## Ví dụ lỗ hổng TCP/IP
- `HTTP`: nghi thức `tầng ứng dụng`. dùng truyền các trang web từ máy chủ web, dữ liệu truyền dạng `văn bản thuần túy` -> dễ dàng đọc
- `Sự xác thực yếu giữa máy khách & máy chủ web` trong quá trình khởi tạo 1 phiên session -> tấn công chiếm quyền truy cập -> đánh cắp 1 phiên HTTP hợp 
## Nghi thức bắt tay TCP/IP
sender ___________ receiver

SYN seq=X ----------> SYN received (step 1)

SYN received <--------send ACK X+1 and SYN Y (step 2)

Send ACK Y+1 --------> (step 3)
![image](https://user-images.githubusercontent.com/88178841/219946261-d925b295-eae5-41d4-8e8a-5b21d86b91e8.png)
- Kẻ tấn công mở tấn công từ chối dịch vụ `SYN-flooding` -> thiết lập nhiều phiên mở  dang dở (không bắt tay) -> quá tải máy chủ, máy chủ gục ngã
- Sửa đổi header của nghi thức IP -> khởi chạy cuộc tấn công giả mạo
## SYN 
