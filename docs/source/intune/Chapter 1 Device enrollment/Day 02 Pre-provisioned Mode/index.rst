Pre-provisioned mode
====================

Trong Sphinx (dùng với .. toctree::), tùy chọn :maxdepth: xác định mức độ sâu của mục lục con (nested pages) sẽ được hiển thị trong sidebar hoặc phần table of contents.

⸻

✅ Giải nghĩa :maxdepth:


Nghĩa là:

Chỉ hiển thị cấp 1 trong cây tài liệu. Những file index.rst của intune/ và jamf/ có thể có nội dung con, nhưng không hiện trong sidebar hoặc mục lục, trừ khi bạn tăng maxdepth.

⸻

📊 Ví dụ trực quan:

Giả sử bạn có cấu trúc như sau trong intune/index.rst:


   chapter1/device_enrollment
   chapter2/configuration

Nếu bạn dùng:

:maxdepth:	Sidebar hiển thị
1	Chỉ Intune Documentation
2	+ Chapter 1, Chapter 2 (trong sidebar)
3+	Cả tiêu đề con bên trong chương



⸻

✅ Khi nào dùng :maxdepth: 1?
	•	Khi bạn chỉ muốn hiển thị mục chính cấp cao nhất → cho gọn sidebar
	•	Tốt khi có nhiều chương lớn nhưng không muốn làm rối

⸻

✅ Khi nào dùng :maxdepth: 2+?
	•	Khi bạn muốn hiện tất cả phần con rõ ràng ngay từ sidebar (user điều hướng nhanh hơn)
	•	Thường dùng trong tài liệu kỹ thuật

⸻

Bạn muốn mình gợi ý cấu trúc toctree phù hợp cho tài liệu Intune/Jamf của bạn không?