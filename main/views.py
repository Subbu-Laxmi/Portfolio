from django.shortcuts import render,  get_object_or_404
from .models import Project
from django.http import FileResponse, HttpResponse, Http404
import os
from django.conf import settings

def view_resume(request):
    resume_path = os.path.join(settings.BASE_DIR, 'main', 'static', 'main', 'Subbu_Laxmi_Laxmanan Resume.pdf')
    if os.path.exists(resume_path):
        return FileResponse(open(resume_path, 'rb'), content_type='application/pdf')
    else:
        raise Http404("Resume not found")

def download_resume(request):
    resume_path = os.path.join(settings.BASE_DIR, 'main', 'static', 'main', 'Subbu_Laxmi_Laxmanan Resume.pdf')
    if os.path.exists(resume_path):
        response = FileResponse(open(resume_path, 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Subbu_Laxmi_Laxmanan_Resume.pdf"'
        return response
    else:
        raise Http404("Resume not found")
def home(request):
    about_me = {
        "name": "SUBBU LAXMI LAXMANAN ",
        "bio": "Enthusiastic and detail-oriented fresher with a strong foundation in programming. Passionate about solving challenges through innovative solutions and eager to contribute to collaborative projects. Committed to continuous learning and adapting to new technologies to achieve excellence. Improved alumni engagement through real-time communication features. ",
        "profile_image": "static/Profile-pic.jpg",  
    }

    return render(request, 'main/index.html', {"about_me": about_me})

def education(request):
    education = [
        {
            "degree": "Master of Computer Applications (MCA)",
            "university": "Manonmaniam Sundaranar University",
            "year": "2023 - 2025",
            "cgpa" : "8.7"
        },
        {
            "degree": "Bachelor of Computer Science (B.Sc)",
            "university": "Manonmaniam Sundaranar University",
            "year": "2020 - 2023",
            "cgpa" : "8.5"
        },
    ]
    return render(request, 'main/education.html', {"education": education})

def projects(request):
    projects = [
        {
            "title" : "OCR Based Expense Tracker (Web Application)",
            "description" : "The AI-Powered OCR-Based Expense Tracker is a web application designed to automates expense tracking by extracting data from receipts using OCR technology and categorize expenses and provide smart budget recommendations based on user spending patterns.",
            "tech": "HTML, CSS, JavaScript, Flask, Tesseract OCR, SQLite",
            
            "link": "https://github.com/Subbu-Laxmi/",
        },
        {
        "title": "Alumni Connect (Web Application)",
        "description": "Alumni Connect is a web application designed to enhance connections with alumni communities of an educational institutions. It provides a platform for organizing events, sharing job opportunities and facilitating communication among alumni.",
        "tech": "HTML, CSS, JavaScript, PHP, MongoDB",
       
        "link": "https://github.com/Subbu-Laxmi/Alumni-Connect"
        },
        {
        "title": "Virtual Assistant For Windows (Desktop Application)",
        "description": "Developed an AI-powered virtual assistant to process natural language commands, automating routine tasks and improving efficiency.The application integrates advanced speech recognition to accurately capture voice inputs and uses natural language processing techniques to interpret user intent. ",
        "tech": "Python (Tkinter), Speech Recognition, Natural Language Processing.",
        "images": [
                "/static/about-alumni.png",
        ],
        "link": "https://github.com/Subbu-Laxmi/ecommerce"
    },  
    {
        "title" : "Poll Website (Web Application)",
        "description" : "Developed a dynamic web-based polling platform that enables users to create, share, and participate in polls seamlessly. Implemented secure user authentication and authorization to ensure that poll creation and voting processes are safe and reliable. ",
        "tech" : "Django (Python), ReatJS, SQL ",
        "images" : [

        ],
       "link" : "https://github.com/Subbu-Laxmi/"
    },
    ]
    return render(request, 'main/projects.html', {"projects": projects})

def skills(request):
    languages = [
        {"title" : "English"}, 
        {"title" : "Tamil"}
    ]

    skills = [
        {
            "Programming_Languages" : "Python, Java, PHP, JavaScript ",
            "Frameworks": "Flask, Django, Flutter, Bootstrap, React JS",
            "Tools" : "Tesseract OCR, NumPy, Pandas, OpenCV, Scikit-learn, TensorFlow, PyTorch, Postman" ,
            "Databases" : "SQL, MongoDB" 
        }
    ]

    soft_skills = [
        "Effective Communication",
        "Problem Solving",
        "Time Management",
        "Team Collaboration",
        "Active Listening",
        "Adaptability"
    ]

    return render(request, 'main/skills.html', {"skills" : skills ,"soft_skills": soft_skills, "languages" : languages})

def certifications(request):
    certifications = [
        {
            "name": "TCS iON Career Edge - Young Professional", 
            "issuer": "TCS iON",
            "issued_at": "May 2025",  
            "link": "https://drive.google.com/file/d/1b7634Ko1aZ_xfssSTrBTzP55vd6vRLF3/view?usp=drivesdk"
        },
        {
            "name": "Data Analytics Job Simulation", 
            "issuer": "Deloitte",
            "issued_at": "April 2025",  
            "link": "https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/9PBTqmSxAf6zZTseP/io9DzWKe3PTsiS6GG_9PBTqmSxAf6zZTseP_dbkK3aGXiKza2dS6n_1745423015697_completion_certificate.pdf"
        },
        {
            "name": "Power BI for Beginners", 
            "issuer": "Simplilearn powered by Microsoft",
            "issued_at": "March 2025",  
            "link": "https://simpli.app.link/Q4xErS39nRb"
        },
        {
            "name": "Introduction to Artificial Intelligence", 
            "issuer": "Simplilearn ",
            "issued_at": "March 2025",  
            "link": "https://simpli.app.link/afT9Vc8trRb"
        },
        {
            "name": "Python Zero to Hero", 
            "issuer": "GUVI",
            "issued_at": "February 2025",  
            "link": "https://www.guvi.in/verify-certificate.html?id=0g3Uxb4y6212I7D62L&course=pythonzerotoheroenglish "
        },
        {
            "name": "Data Visualization Using Python ", 
            "issuer": "Cognitive Class (powered by IBM Developer Skills Network)", 
            "issued_at": "February 2025",  
            "link": "https://courses.cognitiveclass.ai/certificates/ff8be2fff2204db0bf4382faf4164266 "
        },
        {
            "name": "SQL and Relational Databases 101 ", 
            "issuer": "Cognitive Class (powered by IBM Developer Skills Network)", 
            "issued_at": "February 2025",  
            "link": "https://courses.cognitiveclass.ai/certificates/6b7a68a2f54240f48f6378489c9cd6cc "
        },
        {
            "name": "Generative AI", 
            "issuer": "GUVI", 
            "issued_at": "February 2025",  
            "link": "https://www.guvi.in/share-certificate/6345074Q5U789blHa1 "
        },
        {
            "name": "Machine Learning with Python",
            "issuer": "Cognitive Class (powered by IBM Developer Skills Network)", 
            "issued_at": "January 2025",  
            "link": "https://courses.cognitiveclass.ai/certificates/98483c834eab445fb30d43b4157acfdd "
        },
        {
            "name": "Python (Basic) Skill Test",
            "issuer": "HackerRank", 
            "issued_at": "November 2024",  
            "link": " https://www.hackerrank.com/certificates/dc67d63d1e8d"
        },
        {
            "name": "Python Fundamentals for Beginners",
            "issuer": "Great Learning", 
            "issued_at": "November 2024",  
            "link": " https://olympus.mygreatlearning.com/courses/12682/certificate?pb_id=581"
        },
    ]

    workshops = [
        {"title": "AI & Machine Learning Bootcamp", "date": "January 2025"},
        {"title": "Flutter - Mobile App Development", "date": "August 2024"},
    ]
    return render(request, 'main/certifications.html', {"certifications" : certifications , "workshops" : workshops})


def hobby(request):
    hobby = {
       "hobbies": ["Drawing", "Developing Mini Projects","Learning New Programming Languages", "Exploring Tech Blogs","Reading Books",]
    }

    return render(request, "main/hobby.html", {"hobby": hobby})


def contact(request):
    contact = {
        "email": "lsubbulaxmi802@gmail.com",
        "location": "Tenkasi, India"
    }
    socials = {
        "linkedin" : "https://www.linkedin.com/in/subbu-laxmi-889947318/",
        "git-hub" : "https://github.com/Subbu-Laxmi",
        "leetcode" : "https://leetcode.com/u/Subbu_Laxmi_L/",
        "hackerrank" : "https://www.hackerrank.com/profile/lsubbulaxmi802"
    }
    return render(request, 'main/contact.html', {"contact" : contact ,"socials":socials})