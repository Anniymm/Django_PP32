from django.shortcuts import render, get_object_or_404
from .models import Product
# logikebi 
# yvela productis chveneba 

# shellshi dasatestad 
# def product_list(request):
#     products = Product.objects.all()
    # for p in products:
    #     print(p.name)
 
def product_list(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products": products})

#misamrtshi:  products/1
def product_detail(request, pk):
    product = get_object_or_404(Product, pk = pk)
    return render(request, "products/product_detail.html", {"product": product})


