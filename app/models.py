from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.db.models.signals import pre_save
# Create your models here.

class slider(models.Model):
    discount  =  (
        ("hot deals", "hot deals"),
        ('new things', 'new things'),
    )
    Image = models.ImageField(upload_to="media/slider_images")
    Discount_div1 = models.CharField(choices=discount,max_length=100)
    Sale  = models.IntegerField()
    Brand_Name = models.CharField(max_length=200)
    Discount = models.IntegerField()
    Link = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Brand_Name
    
    
class banner_area(models.Model):
    discount  =  (
        ("hot deals", "hot deals"),
        ('new things', 'new things'),
    )
    Image = models.ImageField(upload_to="media/baner_images")
    Discount_div1 = models.CharField(max_length=100)
    quote  = models.CharField(max_length=100)
    Discount = models.IntegerField()
    Link = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.quote    
    
    
    
class main_cat(models.Model):
    name = models.CharField(max_length=100)
    
    def  __str__(self):
        return self.name
    
    
class cat(models.Model):
    main_cat = models.ForeignKey(main_cat,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def  __str__(self):
        return self.name    +"..."+ self.main_cat.name
    
    
class sub_cat(models.Model):
    cat = models.ForeignKey(cat,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def  __str__(self):
        return self.cat.main_cat.name + "...."+ self.cat.name + "...." + self.name
    
    


class section(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class color(models.Model):
    color_code = models.CharField(max_length=100)

    def __str__(self):
        return self.color_code



class brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return  self.name



class product(models.Model):
    total_quantity = models.IntegerField()
    Availablity = models.IntegerField()
    featured_image = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    Discount = models.IntegerField()
    Tax = models.IntegerField(null=True)
    Packing_cost = models.IntegerField(null=True)
    product_information =  RichTextField()
    model_name = models.CharField(max_length=100)
    categories = models.ForeignKey(cat,on_delete=models.CASCADE)
    color = models.ForeignKey(color,on_delete=models.CASCADE,null=True)
    brand = models.ForeignKey(brand,on_delete=models.CASCADE,null=True)
    tags = models.CharField(max_length=100)
    Discription =  RichTextField()
    section = models.ForeignKey(section,on_delete=models.DO_NOTHING)
    slug  = models.SlugField(default='',max_length=500,null=True ,blank=True)
    
    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("product_detail", kwargs={'slug': self.slug})

    class Meta:
        db_table = "app_Product"

def create_slug(instance, new_slug=None):
    slug = slugify(instance.product_name)
    if new_slug is not None:
        slug = new_slug
    qs = product.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, product)




class coupen_code(models.Model):
    code = models.CharField(max_length=100)
    discount = models.IntegerField()

    def __str__(self):
        return  self.code

class product_image(models.Model):
    product =  models.ForeignKey(product,on_delete=models.CASCADE)
    image_url = models.CharField(max_length=100)
    

    
    
class additional(models.Model):
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    specification = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)
       
       

class data(models.Model):
    username = models.CharField( max_length=50)
    email  = models.EmailField()
    password =models.CharField(max_length=50)
          