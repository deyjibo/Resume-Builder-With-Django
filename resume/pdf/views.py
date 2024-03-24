from django.shortcuts import render

import sqlite3


def start(request):
    return render(request, "index.html")


def data(request):
    if request.method == "POST":
        Name = request.POST.get("Name", '')
        phone = request.POST.get("phone", '')
        add = request.POST.get("add", '')
        dob = request.POST.get("dob", '')
        gen = request.POST.get("gen", '')
        lang = request.POST.get("lang", '')
        email = request.POST.get("email", '')
        university = request.POST.get("university", '')
        course = request.POST.get("course", '')
        year = request.POST.get("year", '')
        perc = request.POST.get("perc", '')
        college = request.POST.get("college", '')
        course1 = request.POST.get("course1", '')
        year1 = request.POST.get("year1", '')
        perc1 = request.POST.get("perc1", '')
        skills = request.POST.get("skills", 'no skill')
        strength = request.POST.get("strength", '')
        career = request.POST.get("career", '')
        area = request.POST.get("area", '')
        para = {"Name": Name,
                "phone": phone,
                "add": add,
                "dob": dob,
                "gen": gen, "lang": lang, "email": email, "university": university, "course": course, "year": year,
                "perc": perc, "college": college, "course1": course1, "year1": year1, "perc1": perc1, "skills": skills, "strength": strength, "area": area, "career": career}
        try:
            # Your database operations here
            # # ...
            # Connect to an SQLite database (e.g., 'sql.db')
            sqliteConnection = sqlite3.connect('sql.db', check_same_thread=False)
            cursor = sqliteConnection.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, name TEXT, addr TEXT, dob TEXT, gen TEXT, email TEXT);''')

            # Insert data into the table
            query = "INSERT INTO users (name, addr, dob, gen, email) VALUES ('{}', '{}', '{}', '{}', '{}');".format(Name, add, dob, gen, email)
            print(query)
            res = cursor.execute(query)

            # Commit changes and close the connection
            sqliteConnection.commit()
        except sqlite3.Error as error:
            print('Error occurred:', error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print('SQLite Connection closed')

    return render(request, 'resume.html', para)
    
def home(request):
    x=Profile.objects.all()
    return render(request,'home.html',{'a':x})