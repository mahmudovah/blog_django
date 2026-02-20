from django.shortcuts import render,redirect
from .models import Category, Product

def cat_pro_list(request):
    if request.method == "POST":
        title = request.POST.get("title")
        stock = request.POST.get("stock")
        price = request.POST.get("price")
        status = request.POST.get("status")
        category_id = request.POST.get("category")
        
        categor = Category.objects.get(id=category_id)
        product = Product.objects.create(
            category=categor,
            title=title,
            stock=stock,
            price=price,
            status=status
        )
        
        return redirect("cat_pro_list")
    
    products = Product.objects.all()
    categories = Category.objects.all()

    return render(request,"product.html", context={"products":products, "categories":categories})