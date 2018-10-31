from django.test import TestCase

# Create your tests here.

from products.models import Product

class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        Product.objects.create(product_name='Bla bla product', price='10', discount='0', description='sdfsdfsdfsdsfsfsf')

    def test_product_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('product_name').verbose_name
        self.assertEquals(field_label, 'product name')

    def test_name_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('product_name').max_length
        self.assertEquals(max_length, 128)

    def test_price_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'price')

    def test_price_max_digits(self):
        product = Product.objects.get(id=1)
        max_digits = product._meta.get_field('price').max_digits
        self.assertEquals(max_digits, 10)

    def test_object_name_is_email_and_name(self):
        product = Product.objects.get(id=1)
        expected_object_name = '%s ' % (product.product_name)
        self.assertEquals(expected_object_name, str(product))















