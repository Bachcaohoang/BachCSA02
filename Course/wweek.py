--create table HocSinh(
--HocSinhID INT Primary Key,
  --HoTen VARCHAR(50),
  --NgaySinh dATE,
  --GioiTinh VARCHAR(50),
  --Lop INT);
--INSERT INTO HocSinh (HocSinhID, HoTen, NgaySinh, GioiTinh, Lop)
--VALUES 
--(1, 'Nguyen Van A', '2005-09-01', 'Nam', '10A1'),
--(2, 'Tran Thi B', '2005-08-15', 'Nu', '10A1'),
--(3, 'Le Van C', '2005-07-20', 'Nam', '10A2'),
--(4, 'Pham Thi D', '2006-01-01', 'Nu', '10A2'),
--(5, 'Hoang Van E', '2006-02-12', 'Nam', '10A3');
  --CREATE TABLE  MonHoc(
    --MonHocID INT Primary Key,
    --TenMon VARCHAR(50));
 --INSERT INTO MonHoc (MonHocID, TenMon)
--VALUES 
--(1, 'Toan'),
--(2, 'Ly'),
--(3, 'Hoa'),
--(4, 'Van'),
--(5, 'Anh');
--create table Diem(
  --HocSinhID int,
  --MonHocID int,
  --DiemSo decimal(10, 2),
  --NgayThi  date,
   --FOREIGN KEY  (HocSinhID) REFERENCES HocSinh(HocSinhID),
  --FOREIGN KEY  (MonHocID) REFERENCES MonHoc(MonHocID)
--);
--iNSERT INTO Diem (HocSinhID, MonHocID, DiemSo, NgayThi)
--VALUES 
--(1, 1, 8.5, '2023-06-01'), 
--(1, 2, 7.0, '2023-06-01'), 
--(1, 3, 6.5, '2023-06-01'), 
--(2, 1, 9.0, '2023-06-02'), 
--(2, 2, 8.5, '2023-06-02'), 
--(3, 1, 5.0, '2023-06-03'), 
--(3, 3, 4.5, '2023-06-03'),
--(4, 4, 7.5, '2023-06-04'),
--(4, 5, 8.0, '2023-06-04'), 
--(5, 1, 5.5, '2023-06-05'),
--(5, 2, 6.0, '2023-06-05'); -- Hoang Van E, Ly