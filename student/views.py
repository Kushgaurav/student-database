from django.shortcuts import render, redirect

from django.contrib.auth.models import auth

from student.models import studentDetail

from django.contrib import messages

# from student.sForm import sForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/dashboard')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def dashboard(request):
    if request.user.is_authenticated:

        if studentDetail.objects.all().count() > 0:
            # students = studentDetail.objects.all()
            if request.method == "GET":
                dataBase = request.GET.get('search')
                # and dataBase != "Search..." and dataBase != " ":
                if dataBase is not None and dataBase != "":
                    students = studentDetail.objects.filter(
                        fullName__icontains=dataBase)
                    search = request.GET.get('search')
                else:
                    # geting details from database 10 records
                    students = studentDetail.objects.all().order_by('-id')[:10]
                    search = "Search..."
            data = {
                'students': students,
                'searchingMessage': search
            }
            return render(request, './pages/dashboard.html', data)
        else:
            data = {
                'message': 'No Data Found'
            }
            return render(request, './pages/dashboard.html', data)
    else:
        return redirect('login')


def studentform(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            #      form = sForm()
            # data = {
            #     'form': form
            # }
            # # if request.method == "POST":
            # #     if sForm = studentform(request.POST, request.FILES):
            # #         sForm.save()

            # # messages.success(request, "Form submitted successfully")

            fullName = request.POST.get('fullName')
            collageId = request.POST.get('collageId')
            subject = request.POST.get('subject')
            mobileNumber = request.POST.get('mobileNumber')
            email = request.POST.get('email')
            date = request.POST.get('date')
            file = request.POST.get('file')
            course = request.POST.get('course')
            # filename = request.POST.get('filename')
            student = studentDetail(fullName=fullName, collageId=collageId, subject=subject,
                                    mobileNumber=mobileNumber, email=email, date=date, file=file, course=course)
            if request.FILES:
                student.file = request.FILES['file']

            student.save()
            # taking id from database
            id = studentDetail.objects.get(id=student.id)

            messages.success(
                request, "Form submitted successfully At id number Regesterd Id - " + str(id.id))
            return render(request, './pages/studentform.html')
        else:
            messages.error(request, "Something went wrong please try again")
            return render(request, './pages/studentform.html')
    else:
        return redirect('login')


def view(request):
    if request.user.is_authenticated:
        if studentDetail.objects.all().count() > 0:
            students = studentDetail.objects.all()
            data = {
                'students': students
            }
            return render(request, './pages/view.html', data)
        else:
            data = {
                'message': 'No Data Found'
            }
            return render(request, './pages/view.html', data)
    else:
        return redirect('login')


def edit(request):
    if request.user.is_authenticated:

        # taking data from database by id

        if request.method == "GET":
            id = request.GET.get('id')
            student = studentDetail.objects.get(id=id)
            data = {
                'student': student
            }
            return render(request, './pages/edit.html', data)
        else:
            return redirect("dashboard")
    else:
        return redirect('login')


def update(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            id = request.POST.get('id')
            fullName = request.POST.get('fullName')
            collageId = request.POST.get('collageId')
            subject = request.POST.get('subject')
            mobileNumber = request.POST.get('mobileNumber')
            email = request.POST.get('email')
            date = request.POST.get('date')
            file = request.POST.get('file')
            course = request.POST.get('course')
            # filename = request.POST.get('filename')
            student = studentDetail(id=id, fullName=fullName, collageId=collageId, subject=subject,
                                    mobileNumber=mobileNumber, email=email, date=date, file=file, course=course)
            if request.FILES:
                student.file = request.FILES['file']

            # student.save()
            #  updating data in database
            studentDetail.objects.filter(id=id).delete()

            student.save()
            #  updating data in database
            # studentDetail.objects.filter(id=id).update(student)

            messages.success(request, "Form updated successfully")
            return redirect('dashboard')
        else:
            return redirect('dashboard')
    else:
        return redirect('login')


def delete(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            id = request.POST.get('id')
            studentDetail.objects.filter(id=id).delete()
            messages.success(request, "Form deleted successfully")
            return redirect('dashboard')
        else:
            return redirect('view')
    else:
        return redirect('login')
