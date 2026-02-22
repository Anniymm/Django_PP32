from django.contrib import admin
from .models import Product

# -pirveli gza ubralod martivad rogor davamatot
# admin.site.register(Product)

# meore gza damatebiti featurebistvus
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ("name", "price", "in_stock") # aq rasac etyvi veebs yvelaferi chans gaxsnis dros
#     list_filter = ("in_stock",) # filtracia
#     search_fields = ("name",) # searchi
#     ordering = ("-price",) # roca minuss uwert zrdadidan-qvemot chamodis
#     list_editable = ("price", "in_stock") # inlidan rom shedzlot cvlileba  - (list_display_links + list_editable)
#     # readonly_fields = ("name", ) # edit ar shemidzlia

# -----------------------------------------------------------------------------------------------

@admin.action(description="Mark selected products as out of stock")
def mark_out_of_stock(modeladmin, request, queryset):
    queryset.update(in_stock = False)


@admin.action(description="Mark selected products as in  stock")
def mark_in_stock(modeladmin, request, queryset):
    queryset.update(in_stock = True)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "in_stock") # aq rasac etyvi veebs yvelaferi chans gaxsnis dros
    list_filter = ("in_stock",) # filtracia
    search_fields = ("name",) # searchi
    ordering = ("-price",) # roca minuss uwert zrdadidan-qvemot chamodis
    list_editable = ("price", "in_stock") # inlidan rom shedzlot cvlileba  - (list_display_links + list_editable)
    # readonly_fields = ("name", ) # edit ar shemidzlia
    actions = [mark_out_of_stock, mark_in_stock] # roca custom actionebs amatebs es aucilebelia 


admin.site.site_header = "My Shop Header"
admin.site.site_title = "My shop Portal"
admin.site.index_title = "Welcome to my shop"
