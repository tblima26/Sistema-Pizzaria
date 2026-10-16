from decimal import Decimal
from django import forms
from .models import Pizza


CLASSE_INPUT = (
    'w-full rounded-xl border border-stone-700 '
    'bg-stone-900 px-4 py-3 text-stone-100 '
    'placeholder-stone-500 outline-none transition '
    'focus:border-orange-500 focus:ring-2 '
    'focus:ring-orange-500/20'
)

CLASSE_SELECT = (
    'w-full cursor-pointer rounded-xl border '
    'border-stone-700 bg-stone-900 px-4 py-3 '
    'text-stone-100 outline-none transition '
    'focus:border-orange-500 focus:ring-2 '
    'focus:ring-orange-500/20'
)


class PrecoPizzaField(forms.DecimalField):
    def to_python(self, value):
        if isinstance(value, str):
            value = value.strip().replace('R$', '').strip()

            if ',' in value:
                value = value.replace('.', '').replace(',', '.')

        return super().to_python(value)


class PizzaForm(forms.ModelForm):
    preco = PrecoPizzaField(
        max_digits=7,
        decimal_places=2,
        min_value=Decimal('0'),
        widget=forms.TextInput(attrs={
            'class': CLASSE_INPUT,
            'placeholder': 'Ex.: 39,90',
            'id': 'preco',
            'inputmode': 'decimal',
        })
    )

    categoria = forms.ChoiceField(
        choices=Pizza.CATEGORIAS,
        widget=forms.Select(attrs={
            'class': CLASSE_SELECT,
        })
    )

    class Meta:
        model = Pizza
        fields = ['nome', 'preco', 'categoria', 'ingredientes']

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': CLASSE_INPUT,
                'placeholder': 'Nome da pizza',
            }),

            'ingredientes': forms.Textarea(attrs={
                'class': (
                    'w-full resize-y rounded-xl border '
                    'border-stone-700 bg-stone-900 px-4 py-3 '
                    'text-stone-100 placeholder-stone-500 '
                    'outline-none transition focus:border-orange-500 '
                    'focus:ring-2 focus:ring-orange-500/20'
                ),
                'placeholder': 'Descreva os ingredientes da pizza...',
                'rows': 4,
            }),
        }