#0. Import thư viện
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

#1. Tạo bảng dữ liệu
data = {'Họ và tên': ['Nguyễn Văn A',
               'Trần Thị B',
               'Lê Văn C',
               'Phạm Thị D',
               'Hoàng Văn E',
               'Vũ Thị F',
               'Đỗ Văn G',
               'Bùi Thị H',
               'Ngô Văn I',
               'Dương Thị K'],
 'Điểm chuyên cần': [8.0, 9.0, 7.0, 6.5, 10.0, 8.5, 5.5, 9.5, 7.5, 8.0],
 'Điểm giữa kỳ': [7.5, 8.0, 6.0, 7.0, 9.0, 8.0, 5.0, 8.5, 6.5, 7.0],
 'Điểm cuối kỳ': [8.0, 8.5, 6.5, 7.5, 9.5, 8.0, 6.0, 9.0, 7.0, 7.5]}

df = pd.DataFrame(data)

#2. Tính điểm tổng kết
df['Tong_ket'] = (
    0.2 * df['Điểm chuyên cần']
    + 0.3 * df['Điểm giữa kỳ']
    + 0.5 * df['Điểm cuối kỳ']
)

#3. Xếp loại sinh viên
def xep_loai(diem):
    if diem >= 8.5:
        return 'Giỏi'
    elif diem >= 7:
        return 'Khá'
    elif diem >= 5:
        return 'Trung bình'
    else:
        return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

#4. Thống kê
diem_trung_binh = df['Tong_ket'].mean()
sv_cao_nhat = df.loc[df['Tong_ket'].idxmax()]
sv_thap_nhat = df.loc[df['Tong_ket'].idxmin()]
so_sv_dat = (df['Tong_ket'] >= 5).sum()

#6. Hiển thị tiêu đề và bảng điểm
st.title('QUẢN LÝ ĐIỂM SINH VIÊN')
st.subheader('Bảng điểm của 10 sinh viên')
st.dataframe(df)

#7. Hiển thị thống kê của lớp
st.subheader('Thống kê')
st.write(f'Điểm tổng kết trung bình của lớp: {diem_trung_binh:.2f}')
st.write(f"Sinh viên cao nhất: {sv_cao_nhat['Họ và tên']} - {sv_cao_nhat['Tong_ket']:.2f}")
st.write(f"Sinh viên thấp nhất: {sv_thap_nhat['Họ và tên']} - {sv_thap_nhat['Tong_ket']:.2f}")
st.write(f'Số sinh viên đạt: {so_sv_dat}/{len(df)}')

#8. Chọn sinh viên và hiển thị điểm
st.subheader('Tra cứu sinh viên')
ten_sv = st.selectbox('Chọn một sinh viên', df['Họ và tên'])
sv = df.loc[df['Họ và tên'] == ten_sv].iloc[0]

st.write(f"Điểm chuyên cần: {sv['Điểm chuyên cần']}")
st.write(f"Điểm giữa kỳ: {sv['Điểm giữa kỳ']}")
st.write(f"Điểm cuối kỳ: {sv['Điểm cuối kỳ']}")
st.write(f"Điểm tổng kết: {sv['Tong_ket']:.2f}")
st.write(f"Xếp loại: {sv['Xep_loai']}")

#9. Hiển thị biểu đồ điểm của cả 10 sinh viên
st.subheader('Biểu đồ điểm tổng kết')
#5. Vẽ biểu đồ cột ngang
plt.figure(figsize=(10, 6))
plt.barh(df['Họ và tên'], df['Tong_ket'], color='skyblue')
plt.title('Điểm tổng kết của 10 sinh viên')
plt.xlabel('Điểm tổng kết')
plt.ylabel('Tên sinh viên')
plt.xlim(0, 10)
plt.tight_layout()
st.pyplot(plt.gcf())
plt.close()

#10. Thông tin tác giả cuối trang; caption hiển thị chữ nhỏ
st.caption('Người tạo ứng dụng: Phạm Thị Mai Trinh | MSSV: 034308006565')
