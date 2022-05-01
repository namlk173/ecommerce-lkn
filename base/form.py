from attr import fields
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Clothes, Customer, MobilePhone, Product, User, Book, Address, Employee


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['full_name', 'username', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['class'] = 'form-control  bg-dark text-white form-register'
        self.fields['username'].widget.attrs['class'] = 'form-control  bg-dark text-white form-register'
        self.fields['email'].widget.attrs['class'] = 'form-control  bg-dark text-white form-register'
        self.fields['password1'].widget.attrs['class'] = 'form-control  bg-dark text-white form-register'
        self.fields['password2'].widget.attrs['class'] = 'form-control  bg-dark text-white form-register'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Tên sản phẩm'
        self.fields['name'].widget.attrs['style'] = 'width:38%'
        self.fields['description'].widget.attrs['placeholder'] = 'Mô tả sản phẩm'
        self.fields['description'].widget.attrs['class']  = 'decription-product'
        self.fields['price'].widget.attrs['placeholder'] = 'Giá sản phẩm (đ)'
        self.fields['company'].widget.attrs['placeholder'] = 'Công ty phụ trách sách'
        self.fields['publish_date'].widget.attrs['placeholder'] = 'Ngày xuất bản'
        self.fields['width'].widget.attrs['placeholder'] = 'chiều rộng (cm)'
        self.fields['height'].widget.attrs['placeholder'] = 'Chiều dài (cm)'
        self.fields['number_page'].widget.attrs['placeholder'] = 'Số trang'
        self.fields['author'].widget.attrs['placeholder'] = 'Tác giả/ Dịch giả'
        self.fields['book_category'].widget.attrs['placeholder'] = 'Loại sách'
        # ---------------------------------------------------------------------#
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['company'].widget.attrs['class'] = 'form-control'
        self.fields['publish_date'].widget.attrs['class'] = 'form-control'
        self.fields['width'].widget.attrs['class'] = 'form-control'
        self.fields['height'].widget.attrs['class'] = 'form-control'
        self.fields['number_page'].widget.attrs['class'] = 'form-control'
        self.fields['author'].widget.attrs['class'] = 'form-control'
        self.fields['book_category'].widget.attrs['class'] = 'form-control'



class MobilePhoneForm(forms.ModelForm):
    class Meta:
        model = MobilePhone
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(MobilePhoneForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Tên sản phẩm'
        self.fields['name'].widget.attrs['style'] = 'width:38%'
        self.fields['price'].widget.attrs['placeholder']  = 'Giá sản phẩm (đ)'
        self.fields['description'].widget.attrs['placeholder']  = 'Mô tả ngắn sản phẩm'
        self.fields['description'].widget.attrs['class']  = 'decription-product'
        self.fields['brand'].widget.attrs['placeholder'] = 'Hãng sản phẩm (VD Iphone..)'
        self.fields['gen'].widget.attrs['placeholder'] = 'Thế hệ sản phẩm'
        self.fields['pin'].widget.attrs['placeholder'] = 'Dung lượng pin (mAh)'
        self.fields['screen_type'].widget.attrs['placeholder'] = 'Loại màn hình'
        self.fields['screen_size'].widget.attrs['placeholder'] = 'Kích thước màn hình (inches)'
        self.fields['screen_size'].widget.attrs['style'] = 'width: 38%'
        self.fields['chip'].widget.attrs['placeholder'] = 'Vi xử lý'
        self.fields['gpu'].widget.attrs['placeholder'] = 'Vi xử lý đồ họa'
        self.fields['sim_number'].widget.attrs['placeholder'] = 'Số sim tối đa'
        self.fields['weight'].widget.attrs['placeholder'] = 'Trọng lượng sản phẩm'
        self.fields['weight'].widget.attrs['style'] = 'width: 38%'
        self.fields['size_of_phone'].widget.attrs['placeholder'] = 'Kích thước sản phẩm'
        self.fields['dpg'].widget.attrs['placeholder'] = 'Độ phân giải màn hình (pixel)' 
        self.fields['ram'].widget.attrs['placeholder'] = 'Bộ nhớ Ram (GB)'
        self.fields['rom'].widget.attrs['placeholder'] = 'Bộ nhớ Rom (GB)'
        # ----------------------------------------------------------------#
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class']  = 'form-control'
        self.fields['description'].widget.attrs['class']  = 'form-control'
        self.fields['brand'].widget.attrs['class'] = 'form-control'
        self.fields['gen'].widget.attrs['class'] = 'form-control'
        self.fields['pin'].widget.attrs['class'] = 'form-control'
        self.fields['screen_type'].widget.attrs['class'] = 'form-control'
        self.fields['screen_size'].widget.attrs['class'] = 'form-control'
        self.fields['chip'].widget.attrs['class'] = 'form-control'
        self.fields['gpu'].widget.attrs['class'] = 'form-control'
        self.fields['sim_number'].widget.attrs['class'] = 'form-control'
        self.fields['weight'].widget.attrs['class'] = 'form-control'
        self.fields['size_of_phone'].widget.attrs['class'] = 'form-control'
        self.fields['dpg'].widget.attrs['class'] = 'form-control' 
        self.fields['ram'].widget.attrs['class'] = 'form-control'
        self.fields['rom'].widget.attrs['class'] = 'form-control'

class ClothesForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(ClothesForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Tên sản phẩm'
        self.fields['name'].widget.attrs['style'] = 'width:38%'
        self.fields['description'].widget.attrs['placeholder'] = 'Mô tả sản phẩm'
        self.fields['description'].widget.attrs['class']  = 'decription-product'
        self.fields['price'].widget.attrs['placeholder'] = 'Giá sản phẩm (đ)'
        self.fields['material'].widget.attrs['placeholder'] = 'Chất liệu'
        self.fields['origin'].widget.attrs['placeholder'] = 'xuất xứ'
        self.fields['brand'].widget.attrs['placeholder'] = 'Hãng'
        self.fields['size'].widget.attrs['placeholder'] = 'Kích cỡ'
        self.fields['type'].widget.attrs['placeholder'] = 'Loại sẩn phẩm'
        # ------------------------------------------------------------#
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['material'].widget.attrs['class'] = 'form-control'
        self.fields['origin'].widget.attrs['class'] = 'form-control'
        self.fields['brand'].widget.attrs['class'] = 'form-control'
        self.fields['size'].widget.attrs['class'] = 'form-control'
        self.fields['type'].widget.attrs['class'] = 'form-control'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['country', 'province', 'district', 'ward', 'exact_address']
        

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        self.fields['country'].widget.attrs['class'] = 'form-control'
        self.fields['province'].widget.attrs['class'] = 'form-control'
        self.fields['district'].widget.attrs['class'] = 'form-control'
        self.fields['ward'].widget.attrs['class'] = 'form-control'
        self.fields['exact_address'].widget.attrs['class'] = 'form-control'
        