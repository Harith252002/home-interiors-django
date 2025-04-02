from django.shortcuts import render, redirect,HttpResponse
from .models import Product, CartItem

def product_list(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart')

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')


def home(request):
    return HttpResponse('Hello, World!')
 

# from django.core.mail import send_mail
 

from django.http import JsonResponse
from django.core.mail import send_mail

def book_consultation(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        category_name = request.POST.get("category_name")

        subject = "New Consultation Request"
        message = f"""
        Talk to a Designer

        Name: {name}
        Email: {email}
        Phone: {phone}
        Category: {category_name}
        """

        try:
            send_mail(subject, message, "your_email@example.com", [email])
            return JsonResponse({"success": True, "message": "Consultation booked successfully!"})
        except Exception as e:
            return JsonResponse({"success": False, "message": "Failed to send email. Please try again!"}, status=500)

    return JsonResponse({"success": False, "message": "Invalid request!"}, status=400)


    return render(request, "cateogriesdetail.html")
def confirmation_page(request):
    return render(request, "consultation_form.html")