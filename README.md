B1. tạo 1 thư mục tên "EVN" ngang hàng với file "configuration.yaml". nghĩa là file "configuration.yaml" nằm ở đâu thì bạn tạo thư mục tên EVN ở đấy

B2. tải file EVN.py về máy rồi mở file lên Thêm Mã khách Hàng của bạn vào ở dòng số 9 có tên: "Ma_Khach_Hang" rồi lưu lại, xong coppy file đó  vào thư mục EVN vừa mới tạo

B3: cấu hình trong file "sensors.yaml" theo mẫu dưới đây:


    - platform: command_line
      name: python EVN Miền Bắc
      command: "python3 /config/EVN/EVN.py"
      value_template: '{{ value_json.name }}'
      scan_interval:
        minutes: 180
      json_attributes:
        - name
        - MaKhachHang
        - TenKhachHang
        - DiaChi
        - SDT
        - NoiCapDien
        - DiaChiNoiCapDien
        - MaSoCongTo
        - ChiSoCu
        - ChiSoMoi
        - TrangThaiMatDien
        - LanThayDoiCuoi
        - Source
        - UocTinhTienDienThangNay
        - SL_Dien_Theo_ngay
        - LichCatDien
        - Tien_Dien_Thang_Nay
        - Tien_Dien_Thang_Truoc
        - About
        
B4. cấu hình xong lưu file lại rồi vào HomeAssistant check config, sẽ báo: "Cấu hình hợp lệ!"  rồi khởi động lại HomeAssistant

B5. khởi động lại xong các bạn kiểm tra xem đã có sensor.python_evn_mien_bac chưa nhé

B6. Cấu hình LoveLace UI, các bạn tạo 1 thẻ type cards bất kỳ rồi các b chọn "Sửa mã nguồn" xóa toàn bộ nội dung trong thẻ đó đi rồi coppy nội dung trong file LoveLace_UI.txt or https://github.com/marion001/EVN_NPC_PY_HASS/blob/main/LovaLace_UI.txt dán vào là xong
