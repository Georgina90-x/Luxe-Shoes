from django.shortcuts import render, redirect


def view_bag(request):
    """ A view to render the shopping bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

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

    request.session['bag'] = bag
    return redirect(redirect_url)
