from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomUserCreationForm, FarmerDetailForm
from .models import *
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import logging
logger = logging.getLogger(__name__)


def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            if user.role == 'farmer':
                return redirect('register_farmer_detail', user_id=user.id)
            else:
                login(request, user)
                return redirect('dashboard')
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': user_form})

def register_farmer_detail(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    if request.method == 'POST':
        form = FarmerDetailForm(request.POST)
        if form.is_valid():
            farmer_detail = form.save(commit=False)
            farmer_detail.user = user
            farmer_detail.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = FarmerDetailForm()
    return render(request, 'register_farmer_detail.html', {'form': form})

def admin_check(user):
    return user.role == 'admin'

def farmer_check(user):
    return user.role == 'farmer'

@login_required
def dashboard(request):
    if request.user.role == 'admin':
        return redirect('/admin-dashboard')
    elif request.user.role == 'farmer':
        return redirect('/farmer-dashboard')
    else:
        return redirect('login')

@login_required
@user_passes_test(admin_check)
def admin_dashboard(request):
    return render(request, 'index.html')

@login_required
@user_passes_test(admin_check)
def adminhome(request):
    return render(request, 'index.html')



@login_required
@user_passes_test(farmer_check)
def farmer_dashboard(request):
    farmer_detail = FarmerDetail.objects.get(user=request.user)
    logger.info("dhas")
    user_id = request.user.id
    request.session['user_id'] = user_id
    logger.info(user_id)
    return render(request, 'farmer/index.html',  {'user_id': user_id})



def personal_information(request, user_id):
    #user = get_object_or_404(CustomUser, id=user_id)
    
    farmer = get_object_or_404(FarmerDetail, user_id=user_id)
    

    if request.method == 'POST':
        'phone','pincode','village','taluk','district','state','country'
        user_id=user_id
        phone  = request.POST.get('phone')
        pincode  = request.POST.get('pincode')
        village  = request.POST.get('village')
        taluk  = request.POST.get('taluk')
        district  = request.POST.get('district')
        state  = request.POST.get('state')
        country  = request.POST.get('country')
        
        farmer = FarmerDetail.objects.get(user_id=user_id)
        farmer_exists = FarmerDetail.objects.filter(user_id=user_id).exists()
        
        logger.info(farmer)

        if phone and pincode :
            if(farmer_exists):

                
            # Step 1: Fetch the FarmerDetail record where id = 1
                    farmer = FarmerDetail.objects.get(user_id=user_id)
        
                    # Step 2: Update the fields you want to change
                    farmer.phone = phone  
                    farmer.pincode = pincode
                    farmer.village = village
                    farmer.taluk = taluk
                    farmer.district = district
                    farmer.state = state
                    farmer.country = country
                    

                        # Step 3: Save the changes to the database
                    farmer.save()

                
                    return redirect('farmer_success')  # Redirect to a success page or other desired page
            else:
                FarmerDetail.objects.create(user_id=user_id,phone = phone,pincode = pincode,village = village,taluk = taluk,district = district,state = state,country = country)    
                return redirect('farmer_success')  # Redirect to a success page or other desired page
        else:
            return HttpResponse("Missing fields", status=400)

    return render(request, 'farmer/personal_information.html', { 'user_id': user_id, 'farmer': farmer})

@login_required
def farmer_success(request):
    
    #user_id = request.session.get('user_id')
    user_id = request.user.id
    return render(request, 'farmer/farmer_success.html',  {'user_id': user_id})

@login_required
def products(request):
    id=1
    #profile = Farmer.objects.get(id=1)
    

    #return render(request, 'profile.html', {'profile': profile})
    return render(request, 'farmer/products.html')


@login_required
def projection(request):
    id=1
    #profile = Farmer.objects.get(id=1)
    

    #return render(request, 'profile.html', {'profile': profile})
    return render(request, 'farmer/projection.html')


@login_required
def my_contacts(request):
    id=1
    #profile = Farmer.objects.get(id=1)
    

    #return render(request, 'profile.html', {'profile': profile})
    return render(request, 'farmer/my_contacts.html')

