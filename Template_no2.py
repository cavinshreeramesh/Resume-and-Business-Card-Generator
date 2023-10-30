#import sys
#sys.path.append("C:/Users/Cavin/Desktop/kolege/stody/sem 3/APP/python mini project//Resume_creators/Resume_constants")
#from Resume_constants.Resume_constants2 import *
from Resume_constants import Resume_constants2

#with open("Resume_constants2.py") as f:  #run the file with the resume details
    #exec(f.read())

file_content=r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- SEO(Search Engine Operation) -->
    <meta name="keywords" content="web development, website development, web application">
    <meta name="description" content="">

    <!-- FONTS -->
    <link rel="stylesheet" href="html templates\Temp2.css">
    <link href='https://fonts.googleapis.com/css?family=Open+Sans:300,400,600' rel='stylesheet' type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=Raleway:100' rel='stylesheet' type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=Montserrat' rel='stylesheet' type='text/css'>
</head>

<body>
<!-- PAGE STUFF -->
<div class="rela-block page">
    <div class="rela-block top-bar">
        <div class="caps name">
            <div class="abs-center">'''+Resume_constants2.name+r'''</div>
        </div>
    </div>
    <div class="side-bar">
        <div class="mugshot">
            <div class="logo">
                <svg viewbox="0 0 80 80" class="rela-block logo-svg">
                    <path d="M 10 10 L 52 10 L 72 30 L 72 70 L 30 70 L 10 50 Z" stroke-width="2.5" fill="none" />
                </svg>
                <p class="logo-text">kj</p>
            </div>
        </div>
        <p>123 '''+Resume_constants2.addressline1+r'''</p>
        <p>'''+Resume_constants2.addressline2+r'''</p>
        <p>'''+Resume_constants2.phoneno+r'''</p>
        <p>'''+Resume_constants2.email+r'''</p><br>
        <p class="rela-block social twitter">'''+Resume_constants2.twitter+r'''</p>
        <p class="rela-block social pinterest">'''+Resume_constants2.pinterest+r'''</p>
        <p class="rela-block social linked-in">'''+Resume_constants2.linkedin+r'''</p>
        <p class="rela-block caps side-header">Expertise</p>
        <p class="rela-block list-thing">'''+Resume_constants2.skill1+r'''</p>
        <p class="rela-block list-thing">'''+Resume_constants2.skill2+r'''</p>
        <p class="rela-block list-thing">'''+Resume_constants2.skill3+r'''</p>
        <p class="rela-block list-thing">'''+Resume_constants2.skill4+r'''</p>
        <p class="rela-block caps side-header">Education</p>
        <p class="rela-block list-thing">'''+Resume_constants2.education1+r'''</p>
        <p class="rela-block list-thing">'''+Resume_constants2.education2+r'''</p>
        <p class="rela-block list-thing">'''+Resume_constants2.education3+r'''</p>
    </div>
    <div class="rela-block content-container">
        <h2 class="rela-block caps title">'''+Resume_constants2.position+r'''</h2>
        <div class="rela-block separator"></div>
        <div class="rela-block caps greyed">Profile</div>
        <p class="long-margin">'''+Resume_constants2.desc+r''' </p>
        <div class="rela-block caps greyed">Experience</div>

        <h3>Job #1</h3>
        <p class="light">'''+Resume_constants2.job1+r'''</p>
        <p class="justified">'''+Resume_constants2.job1desc+r'''</p>

        <h3>Job #2</h3>
        <p class="light">'''+Resume_constants2.job3+r'''</p>
        <p class="justified">'''+Resume_constants2.job3desc+r'''</p>

        <h3>Job #3</h3>
        <p class="light">'''+Resume_constants2.job3+r'''</p>
        <p class="justified">'''+Resume_constants2.job3desc+r'''</p>
    </div>
</div>
</body>
</html>'''

with open('resume.html','wb') as f:
    f.write(bytes(file_content,encoding='utf8'))

#instantiate package
from html2image import Html2Image #instantiate package
hti = Html2Image()

hti = Html2Image()

hti.screenshot(
    html_file='resume.html', css_file=r'html templates\Temp2.css',
    save_as='resume_image.jpg'
)