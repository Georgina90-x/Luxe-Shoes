from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ A view to render the shopping bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shoesize = None
    if 'shoe_size' in request.POST:
        shoesize = request.POST['shoe_size']
    bag = request.session.get('bag', {})

    """ Logic for adding shoe sizes to the shopping bag """
    if shoesize:
        if item_id in list(bag.keys()):
            if shoesize in bag[item_id]['items_by_shoesize'].keys():
                bag[item_id]['items_by_shoesize'][shoesize] += quantity
            else:
                bag[item_id]['items_by_shoesize'][shoesize] = quantity
        else:
            bag[item_id] = {'items_by_shoesize': {shoesize: quantity}}
    else:

        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of a product in the shopping bag """

    quantity = int(request.POST.get('quantity'))
    shoesize = None
    if 'shoe_size' in request.POST:
        shoesize = request.POST['shoe_size']
    bag = request.session.get('bag', {})

    """ Logic for adjusting products with shoe sizes in the shopping bag """
    if shoesize:
        if quantity > 0:
            bag[item_id]['items_by_shoesize'][shoesize] = quantity
        else:
            del bag[item_id]['items_by_shoesize'][shoesize]
            if not bag[item_id]['items_by_shoesize']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the product from the shopping bag """
    try:
        shoesize = None
        if 'shoe_size' in request.POST:
            shoesize = request.POST['shoe_size']
        bag = request.session.get('bag', {})

        if shoesize:
            del bag[item_id]['items_by_shoesize'][shoesize]
            if not bag[item_id]['items_by_shoesize']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
