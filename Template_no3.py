from Resume_constants import Resume_constants3


file_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- SEO(Search Engine Operation) -->

    <meta name="keywords" content="web development, website development, web application">
    <meta name="description" content="">

    <link rel="stylesheet" href="html templates\Temp3.css">
    <link href='https://fonts.googleapis.com/css?family=Lato:400,300,700' rel='stylesheet' type='text/css'>
</head>

<body>
    <div class="container">
        <div class="header">
          <div class="full-name">
            <span class="first-name">'''+Resume_constants3.firstname+r'''</span>
            <span class="last-name">'''+Resume_constants3.lastname+r'''</span>
          </div>
          <div class="contact-info">
            <span class="email">Email: </span>
            <span class="email-val">'''+Resume_constants3.email+r'''</span>
            <span class="separator"></span>
            <span class="phone">Phone: </span>
            <span class="phone-val">'''+Resume_constants3.phoneno+r'''</span>
          </div>
      
          <div class="about">
            <span class="position">'''+Resume_constants3.position+r'''</span>
            <span class="desc">
              '''+Resume_constants3.positiondesc+r'''
            </span>
          </div>
        </div>
        <div class="details">
          <div class="section">
            <div class="section__title">Experience</div>
            <div class="section__list">
              <div class="section__list-item">
                <div class="left">
                  <div class="name">'''+Resume_constants3.company1+r'''</div>
                  <div class="addr">'''+Resume_constants3.company1address+r'''</div>
                  <div class="duration">'''+Resume_constants3.company1duration+r'''</div>
                </div>
                <div class="right">
                  <div class="name">'''+Resume_constants3.company1position+r'''</div>
                  <div class="desc">'''+Resume_constants3.company1desc+r'''</div>
                </div>
              </div>
              <div class="section__list-item">
                <div class="left">
                  <div class="name">'''+Resume_constants3.company2+r'''</div>
                  <div class="addr">'''+Resume_constants3.company2address+r'''</div>
                  <div class="duration">'''+Resume_constants3.company2duration+r'''</div>
                </div>
                <div class="right">
                  <div class="name">'''+Resume_constants3.company2position+r'''</div>
                  <div class="desc">'''+Resume_constants3.company2desc+r'''</div>
                </div>
              </div>
      
            </div>
          </div>
          <div class="section">
            <div class="section__title">Education</div>
            <div class="section__list">
              <div class="section__list-item">
                <div class="left">
                  <div class="name">'''+Resume_constants3.education1+r'''</div>
                  <div class="addr">'''+Resume_constants3.education1address+r'''</div>
                  <div class="duration">'''+Resume_constants3.education1duration+r'''</div>
                </div>
                <div class="right">
                  <div class="name">'''+Resume_constants3.education1degree+r'''</div>
                  <div class="desc">'''+Resume_constants3.education1course+r'''</div>
                </div>
              </div>
              <div class="section__list-item">
                <div class="left">
                  <div class="name">'''+Resume_constants3.education2+r'''</div>
                  <div class="addr">'''+Resume_constants3.education2address+r'''</div>
                  <div class="duration">'''+Resume_constants3.education2duration+r'''</div>
                </div>
                <div class="right">
                  <div class="name">'''+Resume_constants3.education2degree+r'''</div>
                  <div class="desc">'''+Resume_constants3.education2course+r'''</div>
                </div>
              </div>
      
            </div>
      
          </div>
          <div class="section">
            <div class="section__title">Projects</div>
            <div class="section__list">
              <div class="section__list-item">
                <div class="name">'''+Resume_constants3.project1+r'''</div>
                <div class="text">'''+Resume_constants3.project1desc+r'''</div>
              </div>
      
              <div class="section__list-item">
                <div class="name">'''+Resume_constants3.project2+r'''</div>
                <div class="text">'''+Resume_constants3.project2desc+r'''
                </div>
              </div>
            </div>
          </div>
          <div class="section">
            <div class="section__title">Skills</div>
            <div class="skills">
              <div class="skills__item">
                <div class="left">
                  <div class="name">
                    '''+Resume_constants3.skill1+r'''
                  </div>
                </div>
                <div class="right">
                  <input id="ck1" type="checkbox" checked />
      
                  <label for="ck1"></label>
                  <input id="ck2" type="checkbox" checked />
      
                  <label for="ck2"></label>
                  <input id="ck3" type="checkbox" />
      
                  <label for="ck3"></label>
                  <input id="ck4" type="checkbox" />
                  <label for="ck4"></label>
                  <input id="ck5" type="checkbox" />
                  <label for="ck5"></label>
      
                </div>
              </div>
      
            </div>
            <div class="skills__item">
              <div class="left">
                <div class="name">
                  '''+Resume_constants3.skill2+r'''</div>
              </div>
              <div class="right">
                <input id="ck1" type="checkbox" checked />
      
                <label for="ck1"></label>
                <input id="ck2" type="checkbox" checked />
      
                <label for="ck2"></label>
                <input id="ck3" type="checkbox" />
      
                <label for="ck3"></label>
                <input id="ck4" type="checkbox" />
                <label for="ck4"></label>
                <input id="ck5" type="checkbox" />
                <label for="ck5"></label>
      
              </div>
            </div>
      
          </div>
          <div class="section">
            <div class="section__title">
              Interests
            </div>
            <div class="section__list">
              <div class="section__list-item">
                '''+Resume_constants3.interests+r'''
              </div>
            </div>
          </div>
        </div>
      </div>
      </div>
</body>
</html>'''

with open('resume.html','wb') as f:
    f.write(bytes(file_content,encoding='utf8'))