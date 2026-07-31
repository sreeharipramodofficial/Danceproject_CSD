from django.shortcuts import render,redirect
from .models import Student
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, "home.html")
@login_required
def add_student(request):
    if request.method=="POST":
        name=request.POST["name"]
        dance_form=request.POST["dance_form"]
        batch=request.POST["batch"]
        phone=request.POST["phone"]

        Student.objects.create(
            name=name,
            dance_form=dance_form,
            batch=batch,
            phone=phone
        )

        return redirect("view_students")
    return render(request,"add_student.html")

@login_required
def view_students(request):
    students= Student.objects.all()
    return render(request, "view_students.html", {"students":students})

@login_required
def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method=="POST":
        student.name=request.POST["name"]
        student.dance_form=request.POST["dance_form"]
        student.batch=request.POST["batch"]
        student.phone=request.POST["phone"]

        student.save()
        return redirect("/view/")
    return render(request, "edit_student.html",{"student":student})

@login_required
def delete_student(request, id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect("/view/")

