from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from orders.models import Order

@login_required
def dashboard(request):
    # Get the user's orders
    orders = Order.objects.filter(user=request.user)

    # You can add any other data you want to show here, like user profile info
    return render(request, 'user_profile/dashboard.html', {'orders': orders})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the dashboard after saving changes
    else:
        form = UserChangeForm(instance=request.user)
    
    return render(request, 'user_profile/profile_edit.html', {'form': form})