from django.shortcuts import render, redirect
from online_bank.models import Contact
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password

# View to handle account creation
def contact(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        # Check if the username already exists
        if Contact.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'contact.html', {'username': username})

        # Ensure all fields are filled in
        elif username and password and address and gender:  
            latest_account = Contact.objects.order_by('acc_no').last()
            new_account_number = latest_account.acc_no + 1 if latest_account else 10000000

            # Create and save new contact
            hashed_password = make_password(password)
            contact = Contact(username=username, password=hashed_password, address=address, gender=gender, acc_no=new_account_number)
            contact.save()

            # Redirect to the form page with the new account details
            return render(request, 'form.html', {'username': username, 'new_account_number': new_account_number})
        else:
            messages.error(request, "Please fill in all required fields.")

    return render(request, 'contact.html')

# View to handle login
def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if user exists with the provided username
        contact = Contact.objects.filter(username=username,password=password)
        
        if contact and check_password(password, contact.password):
            return render(request, 'home.html', {'contact': contact})
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'index.html')

def display(request):
    return render(request, 'display.html')
        
def transfer(request):
    return render(request, 'transfer.html')

def deposit(request):
    return render(request, 'deposit.html')

def withdraw(request):
    return render(request, 'withdraw.html')

# Optional: Logout view to clear session data
def logout_view(request):
    request.session.flush()
    messages.success(request, "You have successfully logged out.")
    return redirect('index')
