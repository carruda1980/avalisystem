from django.test import TestCase

from model_mommy import mommy

from api.models import Produto

class ProdutoTest(TestCase):
    
    def setUp(self):
        self.produto = mommy.make(Produto)
        self.fields = [i.name for i in self.produto._meta.fields]

    def test_id_exists(self):
        self.assertTrue('id' in self.fields)

    def test_produto_exists(self):
        self.assertTrue('produto' in self.fields)

    def test_produto_has_maxlength_255(self):
        self.assertTrue(self.produto._meta.fields[1].max_length == 255)