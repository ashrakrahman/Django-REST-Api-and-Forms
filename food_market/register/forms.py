from django import forms
from info.models import Product

class RegistrationForm(forms.ModelForm):
    product_bid = forms.IntegerField()

    class Meta :
        model = Product
        fields = ('product_name',
                  'product_description',
                  'product_price',
                  'company_country',
                  'company_name',
                  'product_bid',
        )

    def save(self, commit=True):
        product = super(RegistrationForm,self).save(commit=True)
        product.product_name= self.cleaned_data['product_name']
        product.product_description = self.cleaned_data['product_description']
        product.product_price = self.cleaned_data['product_price']
        product.company_country = self.cleaned_data['company_country']
        product.company_name = self.cleaned_data['company_name']
        product.poduct_bid = self.cleaned_data['product_bid']

        if commit:
            product.save()

        return product