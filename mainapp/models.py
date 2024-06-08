from django.db import models


class MainProduct(models.Model):
    title = models.CharField('Название', max_length=100, blank=False)
    reduction = models.CharField('Аббревиатура', max_length=50, blank=False)
    category = models.CharField('Категория', max_length=50)
    similar = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='related_products', verbose_name='Составной товар')
    characteristics = models.JSONField('Характеристики', blank=True, default=dict)
    img = models.ForeignKey('ProductImage', null=True, blank=True, on_delete=models.SET_NULL,
                            related_name='main_product_image')

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(MainProduct, related_name='images', on_delete=models.CASCADE)
    img = models.ImageField('Изображение', upload_to='mainapp/images')

    def __str__(self):
        return f'Image for {self.product.title}'
