# Marketing Practitioner — bộ vector Dấu chuyển

Bản dựng lại ngày 08-09-2026. Thư mục PNG tham chiếu `../logo-20260908/` được giữ nguyên; đối chiếu SHA-256 trước/sau không thay đổi.

## File sử dụng

- `svg/symbol-{color,black,white}.svg`: 3 biểu tượng vector thật, nền trong suốt.
- `svg/lockup-{color,black,white}.svg`: 3 bản biểu tượng đi cùng tên, toàn bộ chữ đã thành path, nền trong suốt.
- `png/symbol-{color,black,white}-{32,64,128,256,512,1024}.png`: 18 PNG RGBA trong suốt, xuất trực tiếp từ SVG.
- `favicon/favicon.ico`: chứa đủ 16, 32, 48 px, trong suốt. Dùng hình học favicon điều chỉnh riêng.
- `favicon/favicon-optical-{color,black,white}.svg`: bản vector nguồn của favicon, trong suốt.
- `pdf/marketing-practitioner-vector.pdf`: PDF vector 6 trang; lần lượt biểu tượng/bản có tên màu, đen, trắng. Hai trang trắng có nền xanh mực vector để xem được hình. Nền này thuộc bản trình bày PDF; SVG và PNG không có nền.
- `source/master.json`: nguồn hình học, bố cục, màu và các mục tiêu hiệu chỉnh chữ.
- `source/lockup-editable.svg`: giữ chữ có thể sửa; cần font Montserrat. Bản phân phối trong `svg/` không cần font.
- `source/rebuild.py`: dựng lại tất cả bản phân phối từ master.json và font kèm theo.

SVG dùng path/g thuần, không có image, bitmap nhúng, data URI, bộ lọc hay tài nguyên ngoài. Chữ trong SVG phân phối và PDF đã là đường nét vector.

## Bản gốc chuẩn và đối chiếu

Chọn `symbol-color-light.png` làm tham chiếu hình học biểu tượng. Bản gốc có viewBox 0 0 1254 1254, gồm đúng hai path: khung và mảnh bằng chứng. Đường thẳng thay cho viền raster không đều; mảnh nghiêng được chuẩn hóa thành hình bình hành có cạnh trên/dưới song song.

Giữ độ dày quan sát được thay vì đồng nhất máy móc: cạnh trái 153,5 đơn vị, tay ngang trên 141,5, đáy 132,5 và cạnh phải 154. Khoảng ngang giữa đầu tay trên và mảnh rời là 62 đơn vị. Sự chênh độ dày này đã có trong PNG và giúp giữ tỷ lệ đã chọn.

So sánh mặt nạ biểu tượng vector với PNG đạt IoU **0,993237**. Mặt nạ PNG dùng R < 100, G < 190, G − R > 5; mặt nạ vector dùng alpha > 127. Đây chỉ là độ chồng khít vùng hình ở kích thước 1254 px, không phải điểm chất lượng hoặc bằng chứng nhận diện thương hiệu. Xem `qa/symbol-overlay.png`: phần chung màu xanh mực, riêng PNG màu hồng, riêng vector màu xanh lam.

PNG biểu tượng riêng và PNG có tên không hoàn toàn đồng nhất hình học. Bản có tên mới sử dụng chính hai path của bản gốc, với phép biến đổi `translate(156 -25) scale(0.59)`, không dựng lại biểu tượng lần thứ hai. Vị trí khung trên có dịch nhẹ so với ảnh có tên để giữ tỷ lệ của bản gốc; đáy và vị trí tổng thể được cân theo bố cục tham chiếu.

Xem `qa/reference-comparison.png` để đối chiếu cạnh nhau; không nhúng ảnh tham chiếu vào SVG hay PDF.

## Font và hiệu chỉnh quang học

Không thể xác định chắc chắn font gốc từ PNG sinh bằng AI. **Montserrat ExtraBold, trục wght = 800**, được chọn làm font thay thế có nguồn xác minh, không tuyên bố đây là font gốc chính xác.

- Nguồn: https://github.com/google/fonts/tree/main/ofl/montserrat
- Font kèm theo: `source/Montserrat-wght.ttf`, bản variable nguyên bản, Version 9.000.
- Bản quyền: Copyright 2024 The Montserrat.Git Project Authors.
- Giấy phép: **SIL Open Font License 1.1**, bản đầy đủ tại `source/OFL.txt`.
- SHA-256 của font: `0f7b311b2f3279e4eef9b2f968bcdbab6e28f4daeb1f049f4f278a902bcd82f7`.
- File font được giữ nguyên; chỉ đường nét chữ trong logo được biến đổi. Không phát hành một font Montserrat đã sửa.

Chữ ban đầu dùng cỡ 198 trên viewBox 2172 × 724, kerning HarfBuzz, tracking −5 đơn vị. Vì Montserrat rộng hơn chữ trong PNG, hai dòng được chỉnh theo khung mực mục tiêu để giữ bố cục:

| Dòng | Khung mực mục tiêu x/y | Co giãn ngang | Co giãn dọc |
| --- | --- | --- | --- |
| Marketing | (857,217) đến (1799,425) | 92,3396% | 104,3844% |
| Practitioner | (857,402) đến (1902,559) | 88,0573% | 97,6056% |

Đây là **chữ tùy biến dựa trên Montserrat**, không phải Montserrat nguyên tỷ lệ. Tỷ lệ riêng từng dòng là điều chỉnh có chủ đích để gần khung chữ PNG; hình dạng từng chữ, nhất là “g”, “r”, không được nhận là khớp tuyệt đối. Hai dòng căn cùng mép mực trái x = 857. Bản chỉnh sửa giữ ma trận tương ứng; `master.json` và `rebuild.py` là nguồn để xuất lại chính xác.

Màu bản gốc: khung/chữ #092D35, mảnh rời #008477. Bản đen #000000, bản trắng #FFFFFF. Màu được chuẩn hóa thành mảng phẳng; không giữ nhiễu/biến thiên màu trong PNG sinh.

## Favicon điều chỉnh riêng

Ở 16 px, khoảng ngang 62 đơn vị của bản gốc còn khoảng **0,79 px**. Favicon dùng lưới riêng 16 × 16:

- Khung trái x = 3, tay trên đến x = 8; mảnh rời bắt đầu x = 10, tạo khe ngang **2 px**.
- Khung kéo đến x = 12, y = 14; khoảng rỗng trong từ x = 5 đến 10, đáy trong y = 12.
- Mảnh rời có các đỉnh (10,4), (14,2), (14,5), (10,7); vẫn là hình bình hành đầu bằng.
- Các cạnh ngang/dọc được bám lưới nguyên. Tỷ lệ chiếm chỗ và độ dày được điều chỉnh cho hình nhỏ; không thay bản gốc trong SVG/PNG thông thường.
- Ba frame ICO được render trực tiếp từ SVG favicon ở 16, 32 và 48 px. Đã giải mã từng frame và so sánh pixel với kết quả render tương ứng.

## Kiểm tra đã thực hiện

- Render toàn bộ 6 SVG phân phối bằng resvg, không tải font hệ thống.
- Xác nhận không có image/text trong SVG phân phối; tên đã thành path.
- So sánh path, transform và alpha giữa ba biến thể: giống nhau hoàn toàn trong từng loại.
- Kiểm tra đủ 18 PNG, đúng kích thước, chế độ RGBA, alpha có cả 0 và 255; góc ảnh có alpha = 0. Kênh alpha bằng nhau giữa ba màu tại từng kích thước.
- Kiểm tra ICO có chính xác 16/32/48 px, mỗi frame trong suốt và đúng kết quả render.
- Kiểm tra PDF 6 trang, không có ảnh raster; render lại cả 6 trang bằng Poppler và quan sát không mất hình, chữ, hoặc cắt mép.
- Quan sát biểu tượng ở 16/32/64/128 px: bản chính rõ từ 32 px; 16 px dùng favicon riêng. Bản trắng được kiểm tra trên nền xanh mực.
- Kiểm tra đối chiếu PNG/vector và giữ nguyên SHA-256 của toàn bộ file tham chiếu.

Kết quả máy đọc: `qa/verification.json`. Các hình kiểm tra nằm trong `qa/`; chúng là ảnh minh họa kiểm tra, không thay cho các file SVG phân phối.

## Chỉnh sửa và dựng lại

Giữ `source/master.json` làm nguồn duy nhất. Sửa các điểm hình học, màu hoặc khung chữ tại đây; chạy `source/rebuild.py` để xuất lại. Font nguồn và OFL đã kèm theo. Các gói Python cần dùng được ghi đầu script; có tùy chọn `--deps` cho thư mục gói độc lập. Không cần cài font vào Windows để chạy script.

Nếu sửa trực tiếp chữ trong `lockup-editable.svg`, cần nạp font Montserrat kèm theo vào trình sửa và chuyển lại thành path trước khi phân phối. Trình sửa khác nhau có thể xử lý variable font/kerning khác nhau; script với font kèm theo là đường xuất chuẩn.

