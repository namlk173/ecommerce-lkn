from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Clothes, Customer, MobilePhone, Product, User, Book


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['name', 'username', 'email', 'password1', 'password2']
    def __init__(seft, *args, **kwargs):
        super(MyUserCreationForm, seft).__init__(*args, **kwargs)
        seft.fields['name'].widget.attrs['class'] = 'form-control  bg-dark text-white form-register'
        seft.fields['username'].widget.attrs['class'] = 'form-control  bg-dark text-white form-register'
        seft.fields['email'].widget.attrs['class'] = 'form-control  bg-dark text-white form-register'
        seft.fields['password1'].widget.attrs['class'] = 'form-control  bg-dark text-white form-register'
        seft.fields['password2'].widget.attrs['class'] = 'form-control  bg-dark text-white form-register'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
    def __init__(seft, *args, **kwargs):
        super(BookForm, seft).__init__(*args, **kwargs)
        seft.fields['name'].widget.attrs['placeholder'] = 'Tên sản phẩm'
        seft.fields['name'].widget.attrs['style'] = 'width:38%'
        seft.fields['description'].widget.attrs['placeholder'] = 'Mô tả sản phẩm'
        seft.fields['description'].widget.attrs['class']  = 'decription-product'
        seft.fields['price'].widget.attrs['placeholder'] = 'Giá sản phẩm (đ)'
        seft.fields['company'].widget.attrs['placeholder'] = 'Công ty phụ trách sách'
        seft.fields['publish_date'].widget.attrs['placeholder'] = 'Ngày xuất bản'
        seft.fields['width'].widget.attrs['placeholder'] = 'chiều rộng (cm)'
        seft.fields['height'].widget.attrs['placeholder'] = 'Chiều dài (cm)'
        seft.fields['number_page'].widget.attrs['placeholder'] = 'Số trang'
        seft.fields['author'].widget.attrs['placeholder'] = 'Tác giả/ Dịch giả'
        seft.fields['book_category'].widget.attrs['placeholder'] = 'Loại sách'


class MobilePhoneForm(forms.ModelForm):
    class Meta:
        model = MobilePhone
        fields = '__all__'
    def __init__(seft, *args, **kwargs):
        super(MobilePhoneForm, seft).__init__(*args, **kwargs)
        seft.fields['name'].widget.attrs['placeholder'] = 'Tên sản phẩm'
        seft.fields['name'].widget.attrs['style'] = 'width:38%'
        seft.fields['price'].widget.attrs['placeholder']  = 'Giá sản phẩm (đ)'
        seft.fields['description'].widget.attrs['placeholder']  = 'Mô tả ngắn sản phẩm'
        seft.fields['description'].widget.attrs['class']  = 'decription-product'
        seft.fields['brand'].widget.attrs['placeholder'] = 'Hãng sản phẩm (VD Iphone..)'
        seft.fields['gen'].widget.attrs['placeholder'] = 'Thế hệ sản phẩm'
        seft.fields['pin'].widget.attrs['placeholder'] = 'Dung lượng pin (mAh)'
        seft.fields['screen_type'].widget.attrs['placeholder'] = 'Loại màn hình'
        seft.fields['screen_size'].widget.attrs['placeholder'] = 'Kích thước màn hình (inches)'
        seft.fields['screen_size'].widget.attrs['style'] = 'width: 38%'
        seft.fields['chip'].widget.attrs['placeholder'] = 'Vi xử lý'
        seft.fields['gpu'].widget.attrs['placeholder'] = 'Vi xử lý đồ họa'
        seft.fields['sim_number'].widget.attrs['placeholder'] = 'Số sim tối đa'
        seft.fields['weight'].widget.attrs['placeholder'] = 'Trọng lượng sản phẩm'
        seft.fields['weight'].widget.attrs['style'] = 'width: 38%'
        seft.fields['size_of_phone'].widget.attrs['placeholder'] = 'Kích thước sản phẩm'
        seft.fields['dpg'].widget.attrs['placeholder'] = 'Độ phân giải màn hình (pixel)' 
        seft.fields['ram'].widget.attrs['placeholder'] = 'Bộ nhớ Ram (GB)'
        seft.fields['rom'].widget.attrs['placeholder'] = 'Bộ nhớ Rom (GB)'
        

class ClothesForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = '__all__'
    def __init__(seft, *args, **kwargs):
        super(ClothesForm, seft).__init__(*args, **kwargs)
        seft.fields['name'].widget.attrs['placeholder'] = 'Tên sản phẩm'
        seft.fields['name'].widget.attrs['style'] = 'width:38%'
        seft.fields['description'].widget.attrs['placeholder'] = 'Mô tả sản phẩm'
        seft.fields['description'].widget.attrs['class']  = 'decription-product'
        seft.fields['price'].widget.attrs['placeholder'] = 'Giá sản phẩm (đ)'
        seft.fields['material'].widget.attrs['placeholder'] = 'Chất liệu'
        seft.fields['origin'].widget.attrs['placeholder'] = 'xuất xứ'
        seft.fields['brand'].widget.attrs['placeholder'] = 'Hãng'
        seft.fields['size'].widget.attrs['placeholder'] = 'Kích cỡ'
        seft.fields['type'].widget.attrs['placeholder'] = 'Loại sẩn phẩm'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']


