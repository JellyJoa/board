from django import forms
from sun.models import Board, Comment

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['b_title', 'b_author', 'b_content']
        labels = {
            'b_title': '제목',
            'b_author': '작성자',
            'b_content': '내용'
        }

        widgets = {
            'b_title': forms.TextInput(
                attrs={
                    'class': 'form-control w-50',
                    'placeholder': '제목을 입력해주세요'
                }
            ),
            'b_author': forms.TextInput(
                attrs={
                    'class': 'form-control w-28',
                    'placeholder': '작성자를 입력해주세요'
                }
            ),
            'b_content': forms.Textarea(
                attrs={
                    'class': 'form-control w-75',
                    'placeholder': '내용을 입력해주세요'
                }
            )
        }

class BoardDetailForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = '__all__'

        labels = {
            'b_title': '제목',
            'b_author': '작성자',
            'b_content': '내용',
            'b_comment_count': '댓글 수',
            'b_like_count': '좋아요 수'
        }

        widgets = {
            'b_title': forms.TextInput(
                attrs={
                    'class': 'form-control w-50',
                }
            ),
            'b_author': forms.TextInput(
                attrs={
                    'class': 'form-control w-28',
                }
            ),
            'b_content': forms.Textarea(
                attrs={
                    'class': 'form-control w-75',
                }
            ),
            'b_comment_count': forms.TextInput(
                attrs={
                    'class': 'form-control w-25'
                }
            ),
            'b_like_count': forms.TextInput(
                attrs={
                    'class': 'form-control w-25'
                }
            )
        }

