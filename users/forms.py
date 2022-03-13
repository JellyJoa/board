# from django import forms
# from users.models import Member
# from django.contrib.auth.forms import UserCreationForm
#
# class SignupForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['email'].required = True
#     class Meta(UserCreationForm.Meta):
#         model = Member
#         fields = ['username', 'email', 'password']
#         labels = {
#             'username': '사용자이름',
#             'email': '이메일',
#             'password': '비밀번호'
#         }
#
#         widgets = {
#             'username': forms.TextInput(
#                 attrs={
#                     'class' : 'form-control',
#                     'placeholder': '사용자이름을 입력하세요'
#                 }
#             ),
#             'email': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': '이메일을 입력하세요'
#                 }
#             ),
#             'password': forms.PasswordInput(
#                 attrs={
#                     'class' : 'form-control',
#                     'placeholder' : '비밀번호를 입력하세요'
#                 }
#             )
#         }
#
#         def clean_email(self):
#             email = self.cleaned_data.get('email')
#             if email:
#                 qs = Member.objects.filter(email=email)
#                 if qs.exists():
#                     raise forms.ValidationError("이미 등록된 이메일")
#             return email