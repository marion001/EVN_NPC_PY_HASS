# encoding: utf-8
# import datetime
import json
import requests
import datetime
from datetime import datetime
from datetime import timedelta, date
from requests.structures import CaseInsensitiveDict
Ma_Khach_Hang = "XXXXXXXXXXXX" #Mã Khách Hàng EVN Miền Bắc, thay mã khách hàng của bạn tại đây
MaVung = Ma_Khach_Hang[0:6]
MaDiemDo = Ma_Khach_Hang+"001"
SetNgayThang = datetime.now().strftime('%d-%m-%Y')
TruNgayThang = date.today() - timedelta(days=4)
CongNgayCatDien = date.today() + timedelta(days=7)
api_home1 = 'https://billnpccc.enterhub.asia/mobileapi/home/'+Ma_Khach_Hang
API_Co_Mat_Dien = 'https://billnpccc.enterhub.asia/mobileapi/thong-tin-cat-dien/get/'+MaVung+'/'+Ma_Khach_Hang
Api_Dien_Ngay = 'https://meterindex.enterhub.asia/SLngay?MA_DDO='+MaDiemDo+'&STARTTIME='+TruNgayThang.strftime("%d-%m-%Y")+'&STOPTIME='+SetNgayThang+''
API_Lich_Cat_Dien = 'https://billnpccc.enterhub.asia/PowerLossByCustomerID?ma_khang='+Ma_Khach_Hang+'&tu_ngay='+SetNgayThang+'&den_ngay='+CongNgayCatDien.strftime("%d-%m-%Y")+'&ma_ddo='+MaDiemDo+''
#####################################################################
#Api Home
headers1 = CaseInsensitiveDict()
headers1["Host"] = "billnpccc.enterhub.asia"
headers1["Content-Type"] = "application/json"
headers1["Accept"] = "application/json"
headers1["User-Agent"] = "NPCApp/1 CFNetwork/1333.0.4 Darwin/21.5.0"
headers1["Accept-Language"] = "vi-VN,vi;q=0.9"
resp1 = requests.get(api_home1, headers=headers1)
y = resp1.json()
# API requests
resp2 = requests.request("GET", API_Co_Mat_Dien, headers={}, data={})
resp3 = requests.request("GET", Api_Dien_Ngay, headers={}, data={})
y3 = (resp3.json()) 
resp4 = requests.request("GET", API_Lich_Cat_Dien, headers={}, data={})
y4 = (resp4.json()) 
if y4["alert"] == "Không có lịch cắt điện":
    DataCD = y4["alert"]
    NgayCatDien = ""
    KhuVucCatDien = "-"
    NoiDungCatDien = "-"
else:
    DataCD = 'Từ: '+y4["data"][0]["ngay_catdien"][11:-7]+' đến '+y4["data"][0]["ngay_tailap"][11:-7]
    NgayCatDien = y4["data"][0]["ngay_catdien"][8:-13]+'-'+y4["data"][0]["ngay_catdien"][5:-16]+'-'+y4["data"][0]["ngay_catdien"][0:-19]
    KhuVucCatDien = y4["data"][0]["khuvuc_matdien"]
    NoiDungCatDien = y4["data"][0]["noi_dung"]
##replace true, false json TrangThai_ThanhToan
if (y["data"]["customerInfo"]["invoice"][1]["paid"] == True):
    TTTT2 = "Đã thanh toán"
else:
    TTTT2 = "Chưa thanh toán"
if (y["data"]["customerInfo"]["invoice"][0]["paid"] == True):
    TTTT1 = "Đã thanh toán"
else:
    TTTT1 = "Chưa thanh toán"
#Ước Tính Tiền Điện Theo Bậc
SoDien = round(y3[3]["CHI_SO_KET_THUC"] - y["data"]["customerInfo"]["chiSoDienList"][0]["chiSoMoi"])
# Từ 1 đến 50 số điện
if SoDien <= 50:
    Tong = SoDien * 1678
    VAT = Tong / 10
    TongTienCanTT = Tong + VAT
elif (SoDien >= 51) and (SoDien <= 100):    #từ 51-100 số điện
    TienBac1 = 50 * 1678
    SoDienThuaB1 = SoDien - 50
    if (SoDienThuaB1 >= 1) and (SoDienThuaB1 <= 50):
        SoTienBac2 =  SoDienThuaB1 * 1734
        Tong = TienBac1 + SoTienBac2
        VAT = Tong / 10
        TongTienCanTT = Tong + VAT
elif (SoDien >= 101) and (SoDien <= 200):   #từ 101-200 số điện
    TienBac1 = 50 * 1678
    SoDienThuaB1 = SoDien - 50
    if (SoDienThuaB1 >= 1) and (SoDienThuaB1 <= 150):
        SoDienThua2 = SoDienThuaB1 - 50
        TienBac2 = 50 * 1734
    if (SoDienThua2 >= 1) and (SoDienThua2 <= 100):
        TienBac3 = SoDienThua2 * 2014
        Tong = TienBac1 + TienBac2 + TienBac3
        VAT = Tong / 10
        TongTienCanTT = Tong + VAT
elif (SoDien >= 201) and (SoDien <= 300):   #từ 201-300 số điện
    TienBac1 = 50 * 1678
    SoDienThuaB1 = SoDien - 50
    if (SoDienThuaB1 >= 1) and (SoDienThuaB1 <= 250):
        SoDienThua2 = SoDienThuaB1 - 50
        TienBac2 = 50 * 1734
    if (SoDienThua2 >= 1) and (SoDienThua2 <= 200):
        SoDienThua3 = SoDienThua2 - 100
        TienBac3 = 100 * 2014
    if (SoDienThua3 >= 1) and (SoDienThua3 <= 150):
        TienBac4 = SoDienThua3 * 2536
        Tong = TienBac1 + TienBac2 + TienBac3 + TienBac4
        VAT = Tong / 10
        TongTienCanTT = Tong + VAT
elif (SoDien >= 301) and (SoDien <= 400):   #từ 301-400 số điện
    TienBac1 = 50 * 1678
    SoDienThuaB1 = SoDien - 50
    if (SoDienThuaB1 >= 1) and (SoDienThuaB1 <= 350):
        SoDienThua2 = SoDienThuaB1 - 50
        TienBac2 = 50 * 1734
    if (SoDienThua2 >= 1) and (SoDienThua2 <= 300):
        SoDienThua3 = SoDienThua2 - 100
        TienBac3 = 100 * 2014
    if (SoDienThua3 >= 1) and (SoDienThua3 <= 200):
        SoDienThua4 = SoDienThua3 - 100
        TienBac4 = 100 * 2536
    if (SoDienThua4 >= 1) and (SoDienThua4 <= 100):
        SoDienThua5 = SoDienThua4 - 100
        TienBac5 = SoDienThua4 * 2834
        Tong = TienBac1 + TienBac2 + TienBac3 + TienBac4 + TienBac5
        VAT = Tong / 10
        TongTienCanTT = Tong + VAT
elif (SoDien >= 401):      #Trên 400 số điện
    TienBac1 = 50 * 1678
    SoDienThuaB1 = SoDien - 50
    if (SoDienThuaB1 >= 1):
        SoDienThua2 = SoDienThuaB1 - 50
        TienBac2 = 50 * 1734
    if (SoDienThua2 >= 1):
        SoDienThua3 = SoDienThua2 - 100
        TienBac3 = 100 * 2014
    if (SoDienThua3 >= 1):
        SoDienThua4 = SoDienThua3 - 100
        TienBac4 = 100 * 2536
    if (SoDienThua4 >= 1):
        SoDienThua5 = SoDienThua4 - 100
        TienBac5 = 100 * 2834
    if (SoDienThua5 >= 1):
        TienBac6 = SoDienThua5 * 2927
        Tong = TienBac1 + TienBac2 + TienBac3 + TienBac4 + TienBac5 + TienBac6
        VAT = Tong / 10
        TongTienCanTT = Tong + VAT
else:
    Tong = "Có Lỗi Xảy Ra"
    VAT = "Có Lỗi Xảy Ra"
    TongTienCanTT = "Có Lỗi Xảy Ra"
Vu_Tuyen_Json = {
    "name": "Get Data EVN Miền Bắc",
    "MaKhachHang": Ma_Khach_Hang,
    "TenKhachHang": y["data"]["customerInfo"]["name"],
    "DiaChi": y["data"]["customerInfo"]["address"], 
    "SDT": y["data"]["customerInfo"]["phone"],
    "NoiCapDien": y["data"]["customerInfo"]["electricityCompany"]["name"],
    "DiaChiNoiCapDien": y["data"]["customerInfo"]["electricityCompany"]["address"],
    "MaSoCongTo": y["data"]["customerInfo"]["soCongToList"][0],
    "ChiSoCu": str(y["data"]["customerInfo"]["chiSoDienList"][0]["chiSoCu"]) + "(kWh)",
    "ChiSoMoi": str(y["data"]["customerInfo"]["chiSoDienList"][0]["chiSoMoi"]) + "(kWh)",
    "TrangThaiMatDien": (resp2.json()["alert"]),
    "LanThayDoiCuoi": datetime.now().strftime('%H:%M'),
	"UocTinhTienDienThangNay": {
        "ThoiDiemHienTai": {
            "Tinh_Den_Ngay": y3[3]["THOI_GIAN_BAT_DAU"][8:10]+'/'+y3[3]["THOI_GIAN_BAT_DAU"][5:7]+'/'+y3[3]["THOI_GIAN_BAT_DAU"][0:4],
            "Dien_Nang_Tieu_Thu": str(SoDien)+"(kWh)",
            "Tien_Chua_thue": "{:,}".format(Tong)+"(VNĐ)",
            "Tien_Thue_VAT": "{:,}".format(VAT)+"(VNĐ)",
            "Tong_Tien_Can_TT": "{:,}".format(TongTienCanTT).split(".",1)[0]+"(VNĐ)"
    }
    },
    "SL_Dien_Theo_ngay": {
       "HomKia": {
             "Ngay": y3[3]["THOI_GIAN_BAT_DAU"][8:10]+'/'+y3[3]["THOI_GIAN_BAT_DAU"][5:7]+'/'+y3[3]["THOI_GIAN_BAT_DAU"][0:4],
             "ChiSoChot": str(y3[3]["CHI_SO_KET_THUC"])+"(kWh)",
             "SanLuongTieuThu": str(y3[3]["SAN_LUONG"])+"(kWh)"
    },
       "HomKiaf": {
             "Ngay": y3[5]["THOI_GIAN_BAT_DAU"][8:10]+'/'+y3[5]["THOI_GIAN_BAT_DAU"][5:7]+'/'+y3[5]["THOI_GIAN_BAT_DAU"][0:4],
             "ChiSoChot": str(y3[5]["CHI_SO_KET_THUC"])+"(kWh)",
             "SanLuongTieuThu": str(y3[5]["SAN_LUONG"])+"(kWh)"
    },
       "HomKiafNua": {
             "Ngay": y3[7]["THOI_GIAN_BAT_DAU"][8:10]+'/'+y3[7]["THOI_GIAN_BAT_DAU"][5:7]+'/'+y3[7]["THOI_GIAN_BAT_DAU"][0:4],
             "ChiSoChot": str(y3[7]["CHI_SO_KET_THUC"])+"(kWh)",
             "SanLuongTieuThu": str(y3[7]["SAN_LUONG"])+"(kWh)"
    }},
	"LichCatDien": {
		"Ngay": NgayCatDien,
		"Thoigian": DataCD,
		"KhuVuc": KhuVucCatDien,
		"NoiDung": NoiDungCatDien
    },
    "Tien_Dien_Thang_Nay": {
       "Ky": y["data"]["customerInfo"]["invoice"][0]["period"],
       "Thang": y["data"]["customerInfo"]["invoice"][0]["month"],
       "Nam": y["data"]["customerInfo"]["invoice"][0]["year"],
       "SanLuong": str(y["data"]["customerInfo"]["invoice"][0]["usageAmount"])+"(kWh)",
       "SoTien_ThanhToan": format (y["data"]["customerInfo"]["invoice"][0]["paymentTotalAmount"], ',d')+"(VNĐ)",
       "TrangThai_ThanhToan": TTTT1,
       "Ti_Le_ThayDoi": str(y["data"]["customerInfo"]["chiSoDienList"][0]["sanLuongChangeRate"])+"%",
       "PhuongThucThanhToan": y["data"]["customerInfo"]["invoice"][0]["pttt"],
       "ThoiGianThanhToan": y["data"]["customerInfo"]["invoice"][0]["ngayTao"][11:16]+'-'+y["data"]["customerInfo"]["invoice"][0]["ngayTao"][8:10]+'/'+y["data"]["customerInfo"]["invoice"][0]["ngayTao"][5:7]+'/'+y["data"]["customerInfo"]["invoice"][0]["ngayTao"][0:4]
    },
    "Tien_Dien_Thang_Truoc": {
       "Ky": y["data"]["customerInfo"]["invoice"][1]["period"],
       "Thang": y["data"]["customerInfo"]["invoice"][1]["month"],
       "Nam": y["data"]["customerInfo"]["invoice"][1]["year"],
       "SanLuong": str(y["data"]["customerInfo"]["invoice"][1]["usageAmount"])+"(kWh)",
       "SoTien_ThanhToan": format (y["data"]["customerInfo"]["invoice"][1]["paymentTotalAmount"], ',d')+"(VNĐ)",
       "TrangThai_ThanhToan": TTTT2

    },
    "About": {
       "Code By": "Vũ Tuyển",
       "Source": "Python",
       "Facebook": "https://www.facebook.com/TWFyaW9uMDAx",
       "Mail": "tuyenbau1997@gmail.com"
    }
    }
resultJSON = json.dumps(Vu_Tuyen_Json, indent=4, ensure_ascii=False)
print(resultJSON)
