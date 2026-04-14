# 📁 Tấm Cám Tool 

Là một ứng dụng Python đơn giản, giúp tự động phân loại và tách tệp tin PDF ra khỏi các định dạng tệp khác trong một thư mục bất kỳ, trong khi vẫn giữ nguyên cấu trúc thư mục con ban đầu.

# Tính năng chính

Tách riêng tệp .pdf và các tệp định dạng khác (.docx, .jpg, .txt,...) vào hai thư mục riêng biệt.

Giữ nguyên cấu trúc: Giữ hoàn toàn cấu trúc thư mục con bên trong thư mục nguồn.

An toàn dữ liệu: Sử dụng copy, không làm thay đổi hay xóa tệp gốc ở thư mục nguồn.

# Cách hoạt động
Khi bạn chọn một thư mục có tên là TaiLieu, ứng dụng sẽ tạo ra hai thư mục mới nằm cùng cấp:

TaiLieu pdf: Chứa tất cả các tệp PDF.

TaiLieu Others: Chứa tất cả các tệp còn lại.

# Hướng dẫn chạy thử 
Để kiểm tra ứng dụng với file mẫu bạn đã upload:

Giải nén file mẫu "Samples Test Tấm Cám.zip"

Chạy ứng dụng "python tam_cam_tool.py"

# Thực hiện lọc

Khi cửa sổ hiện lên, nhấn CHỌN THƯ MỤC.

Trỏ đến thư mục mẫu vừa giải nén.

Kiểm tra kết quả tại các thư mục mới

# Yêu cầu
Python 3.x trở lên.

# Tùy chỉnh nâng cao
Bạn có thể dễ dàng thay đổi loại file muốn tách (ví dụ: thay vì tách PDF, bạn muốn tách file ảnh .jpg hoặc file Word .docx) bằng cách chỉnh sửa trực tiếp mã nguồn bằng Notepad.

Các bước thực hiện:
Mở file: Click chuột phải vào file Tấm Cám Tool.py, 

chọn Open with -> Notepad.

Thay đổi định dạng: Nhấn Ctrl + F tìm từ khóa .pdf và thay bằng định dạng bạn muốn.

Dòng 20: target_base = pdf_root if file_ext == '.jpg' else others_root

Dòng 23: if file_ext == '.jpg':

Tách nhiều định dạng cùng lúc:

Nếu bạn muốn gom nhiều loại file vào một chỗ (ví dụ cả Word và Excel), hãy sửa dòng 23 thành:

if file_ext in ['.docx', '.xlsx', '.pdf']:

Đổi tên thư mục kết quả: Tìm dòng 8 và 9 để đổi tên hậu tố của thư mục được tạo ra:

pdf_root = os.path.join(parent_dir, f"{base_name} [Tên mới]")

Lưu lại: Nhấn Ctrl + S để lưu và chạy lại chương trình.
