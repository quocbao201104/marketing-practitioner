# Kết quả kiểm tra

Đã mở và quan sát cả 8 PNG cuối, đồng thời lập bảng thu nhỏ bằng System.Drawing trên Windows. Bảng kiểm tra chỉ bố trí và đổi kích thước hiển thị để đánh giá; không sửa hình học của các file logo.

| Hạng mục | Quan sát / quyết định |
| --- | --- |
| Biểu tượng 16 px | Khung và mảnh còn hiện nhưng khe hở chỉ còn rất nhỏ, chi tiết yếu. Không chọn làm kích thước sử dụng chính |
| Biểu tượng 24 px | Hai thành phần còn tách; mức tối thiểu đề xuất trong điều kiện đã xem |
| Biểu tượng 32–128 px | Khoảng âm và mảnh nghiêng rõ trên cả bốn biến thể |
| Bản đi cùng tên rộng 180 px | Đọc được trong bảng kiểm tra, nhưng khá chật |
| Bản đi cùng tên rộng 240–320 px | Tên rõ hơn; đề xuất từ 240 px, ưu tiên 320 px cho README |
| Đơn sắc và đảo trắng | Mảnh nghiêng vẫn tách khỏi khung, không phải dựa vào màu để thấy cấu trúc |
| Màu nền tối | Bản sinh đầu có viền lỗi, đã loại khỏi bộ giao; tạo lại từ biểu tượng đơn sắc sạch |
| Tên | Bốn bản cuối đều hiển thị đúng “Marketing Practitioner” trên hai dòng |
| Quan hệ biến thể | Giữ cùng họ hình, vị trí khung mở và mảnh rời; chưa chuẩn hóa hình học vector hoặc xác nhận đồng nhất từng pixel |
| Định dạng | 4 biểu tượng 1254 × 1254 px, 4 bản đi cùng tên 2172 × 724 px; tất cả 8 file là PNG RGB 24 bit, có nền, không có kênh alpha |
| Màu | Các mã màu trong brief là đích chỉ đạo. Ảnh sinh có biến thiên màu nhẹ; chưa có bảng màu in ấn hay chuẩn màu tuyệt đối |
| Giới hạn | Kiểm tra hiển thị bằng mắt của người thiết kế, không phải nghiên cứu khả năng ghi nhớ hoặc gán đúng thương hiệu |

File `files.json` ghi kích thước và định dạng đọc trực tiếp từ từng ảnh. `variants-preview.png` đặt 8 bản cạnh nhau; `small-size-check.png` là bảng kiểm tra kích thước thật. `preview.html` cho xem từng file và kiểm tra kích thước CSS ở mức thu phóng 100%.

Bản gốc vector, file nền trong suốt, kiểm tra in ấn và đo nhận diện với người dùng chưa được tạo/thực hiện.

