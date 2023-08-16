from django.contrib import admin
from app.models import slider,banner_area,main_cat,cat,sub_cat,section,product,product_image,additional,data,color,brand,coupen_code
# Register your models here.

class product_images(admin.TabularInline):
    model = product_image

class additionals(admin.TabularInline):
    model = additional



class product_admin(admin.ModelAdmin):
    inlines  = (product_images,additionals)
    list_display = ('product_name','price','categories','color','section')
    list_editable  = ('categories','section','color')


admin.site.register(coupen_code)
admin.site.register(section)
admin.site.register(product,product_admin)
admin.site.register(product_image)
admin.site.register(additional)
admin.site.register(color)
admin.site.register(brand)


admin.site.register(slider)
admin.site.register(banner_area)
admin.site.register(main_cat)
admin.site.register(cat)
admin.site.register(sub_cat)
admin.site.register(data)


