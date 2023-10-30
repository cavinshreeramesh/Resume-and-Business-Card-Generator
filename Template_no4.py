from resume_constants import Resume_constants4

file_content =r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- SEO(Search Engine Operation) -->

    <meta name="keywords" content="web development, website development, web application">
    <meta name="description" content="">

    <link rel="stylesheet" href="html templates\Temp4.css">
</head>
<body>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link href='https://fonts.googleapis.com/css?family=Roboto:400,700' rel='stylesheet' type='text/css'>
	<div class="left-box">
	  <div class="top-left">
		<img src="http://images2.fanpop.com/images/photos/4700000/Codeman-cody-lambert-4776780-500-375.jpg" alt="Cody Man">
		<div class="name">'''+Resume_constants4.name+r'''</div>
		<div class="objective">
		  <img class="objective-img" src="https://cdn4.iconfinder.com/data/icons/eldorado-user/40/user-128.png">
		  <div class="objective-text">'''+Resume_constants4.desc+r'''
		  </div>
		</div>
		<div class="phone">
		  <img class="objective-img" src="http://icons.iconarchive.com/icons/icons8/android/512/Mobile-Phone-2-icon.png">
		  <div class="phone-text">'''+Resume_constants4.mobileno+r'''<br>mobile<br><br>'''+Resume_constants4.workno+r'''<br>work
		  </div>
		</div>
		<div class="email">
		  <img class="objective-img" src="http://static.wixstatic.com/media/d822a6_af29afe70e1a4e9891f94a627914b6ec.png">
		  <div class="email-text">'''+Resume_constants4.email+r'''<br>personal<br><br>'''+Resume_constants4.workemail+r'''<br>work
		  </div>
		</div>
	  </div>
	</div>
	<div class="work-experience">
	  <div class="work-img"> <img src="https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQ6IyssJOctWLhN5NZcbES8sa_qjjFGd_LYJEmaTBr12PVJaYUpXA">
	  </div>
	  <h1 class="work-title">Work Experience</h1>
	  <div class="job-box">
		<div class="job-title">'''+Resume_constants4.job1+" "+r'''@'''+Resume_constants4.job1employer+r'''</div>
		<div class="job-date">'''+Resume_constants4.job1duration+r'''</div>
		<div class="job-description">'''+Resume_constants4.job1desc+r'''</div>
	  </div>
	  <div class="job-box">
		<div class="job-title">'''+Resume_constants4.job2+" "+r'''@'''+Resume_constants4.job2employer+r'''</div>
		<div class="job-date">'''+Resume_constants4.job2duration+r'''</div>
		<div class="job-description">'''+Resume_constants4.job2desc+r'''</div>
	  </div>
	  <div class="job-box">
		<div class="job-title">'''+Resume_constants4.job3+" "+r'''@'''+Resume_constants4.job3employer+r'''</div>
		<div class="job-date">'''+Resume_constants4.job3duration+r'''</div>
		<div class="job-description">'''+Resume_constants4.job3desc+r'''</div>
	  </div>
	</div>
	<div class="education">
	  <div class="work-img"> <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAilBMVEX///8AAAB6enp3d3fw8PD4+Pj8/PywsLC+vr7MzMz09PTs7OxDQ0Ph4eGIiIiSkpLU1NRXV1clJSXb29tgYGBPT0+bm5ulpaWAgIA+Pj7R0dFnZ2dvb2/n5+e4uLgkJCQzMzMSEhIdHR1KSko5OTmqqqoZGRksLCxBQUFbW1vExMQLCwuPj4+GhobWHsYEAAAHgUlEQVR4nO2d6ZaiMBCFVSAsyqIouCDubbdjv//rjYgCQqJAAgl96vvVI07IhSyVqkrs9QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALoN4l2BJlHCeajwrkSDmNak3+9PLJN3RdgTtUtDnfWfzFS599da61LqvyIteVeJJWvv3C+y9da8K8YGpE0x8mKmWvdbqmttiPr692HH5V1FGpA6fisvZqx270WiaJhEen5wISPpvKtcnbV/LK0v4uh3athRtJ9K8mJ+tK5YO2v7/eBCZnPtwIs01ENNeTGHu7UjLk75wYWM5PCWgSMa79f2loG+iLO97glntiKdbLnUYaoLI/BeEdfaM9UXsRfE2omm9syyiC0zEawdpAcNyYsJOLfWqpZLHXhZOyiyXNgOLmSmXKyd9ZX94EJm37a1I6uspr7ybFu0dhzpX+v6Inbt+HbWXvuvL6VZ3040bF9WHOXFrC7PyrDH/OWt7sFvIy5lI6RbFrHloBqM9TVsudQhYOjbkf0RbzlYRj6T+eOdQ5c/9C5l0/7iLeIDe5ti2JHVBe/6l2JR09px5jveVS/Nbl7Ft4Oilj3ERotE5uwNe+UNAQEslzrE1s5n3DnvmlIw/zjsGGFTPpe2mIXvrJ0K0SKRIUWyDE9My6UOI6/wIpVL11tnnvGLb8e02/S5tMX++nApy6e/9vpSZqebtXPiXYuG8W/mi6BrIxaM/OFjkre6ZqOV4fwa2nHmdUPTYrLB2OJGmLNGZ4Hlq5puyt2zA1YawbCRs3Gy1XOq1C1+Va3DjLxcjEPV348vRqaPebE6NgyN7BIuY/cajTvj218D3vWtyPlaNmwcJWzdXiHCFvN1uArZbL+kasHUqKfqhVImku/crojnPL2NLXVCjK+N9PtXNeOHJHNSQWR2GtaQdzN20iJ+vGXSAnTBfAALr568G5ne9mwBxkUww2BrUSRQKZkw6F2hoUk7blJwVB1b8mQXHUYPaSs+gV8iq7cOmRKgbB6J0kOyL1R0zafPztCyBcYfmYJ4ckYekwhpNgd9kny69nk7BGasEojMbKmL7JWhGuw4qfu3UmvPDAWu2ZIPuYvKZdC+62o/uLDMjHo1SX8wX3CubXbK0ZV1Ko36Un6A/5J5KrNhhJ7xqYHci9fQ6ODxaXF+bbxT7gJM12OQTOO+3sZ6911DHzRlyW0GOuukkifX1zv5z89VreAgiJ4nWtrs80yP9hL7rmRNpReo5EZK7XlBivZh4eejIdOZcuzjp4V1tFdMoleo5e6XKIxXjDPPxT7dYRiwmET2QYh9iMj14ofIQGE+gyaJxyVr4q2Fb0KKPqcTuSHMesixkpxIeoXr/G2TuSi76p8ExU55F+kk7rqqLGynIO++SVqTsk55WoWoGKxJPFh559uUYEWtayxEDj5+1pPVfJOif4eFV5B0C4x7ceQ5ufYa//PWKcunU+2CEP+oXA/zqKgVmoUik9aId6AerWLjijAu0qSEvIl0wc56imPh5yBqhV6hyOQS0UU8kUJSp3yfOYbrevenowXEp0OtsJDHvfusMGJKaGkmsVMeCEvZYfg2H5JWYbGRpgvgT27+g02cKfOd8qvY9e7/FWG7HlOFfqHEdAFcIpCxveIdYErWEbmZ47se0q8ldgLQKiwaX7MqCvsfZ8pvQteT33Q9lgoL030aSawQjPo3JQTxXA0fHrrNeqW9lZQKiyNpsjysGG67dUrCPfLN2LQrWe2UCjH3SpeHVQOKZ4L5mlW7rJwmQacQF1eyayvsR2MmvlPGd9OkGnnkdAqXmBI9GoUR+E5ZNDhbUYjphukSnyLsPUs7Zbw3ulrXY6gQd9/Ua0AV2D8nkTCHLkOJSiE2vJss8elTFwJtrQW0QSwqhRdciWnKrRjJGVQKsRHsdFrrvELUw/aP1C/UeYU9A1tiugbovkIHV+Auncy6r1DFFbhJFzrdV4jd6LtN1zrdV4g1o77T651XiLBDaSYC3HmFBtbayBTYeYVDbIHzP6Sw6GaLyMRHO68Qa5VmFsDdV5iPG8aky8PuK8RO+JnlYU+M9Oc5WcEnQmyBYfoFMTZJeWQFn8D3w+WnL7RNSFbwCfxYmiyeEGHt0TYUuW0GLmhwzvrJRMjSH9cXeKNwzMfxNXmluEGhfWhPbTHVdIPXwS7ky/FOL+33R5QC7yBT15cONnrpfq5CwzR8uinq2ZwF/jYrMILvYDNtXmBP4ZnOflTaOJoW8duWMGrpqE+F18lR46ayTYvw2dwltXl6Mn6d1SwU5mgd5HaS2FNm7HZalEVtc5/enkHmc3VQe5O/zes3BdbtjDgDnr8nINu7pvVd5ccJa7ww/CYP5jt6QvxUgvu7a0bfXIxz5yOMcMV6ZN2vQsF+1wvpc3aH3EwGupC/yKK4PguLdeq5Qsp74p6k+sdhbyX/sYQXqHXiGOq+NK7WZidjydPbN8yoQIareoPx4v0QtFmMB566lAV/Z+9AytDVNdX3bOt3IAWr6SqQBnPL9qITmtyhkkrrsEgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIC/w3+3wofRvzTtHQAAAABJRU5ErkJggg==">
	  </div>
	  <h1>Education</h1>
	  <div class="job-box">
		<div class="job-title">'''+Resume_constants4.education1course+" "+r'''@'''+Resume_constants4.education1+r'''</div>
		<div class="job-date">'''+Resume_constants4.education1duration+r'''</div>
		<div class="job-description">'''+Resume_constants4.education1desc+r'''</div>
	  </div>
	  <div class="job-box">
		<div class="job-title">'''+Resume_constants4.education2course+" "+r'''@'''+Resume_constants4.education2+r'''</div>
		<div class="job-date">'''+Resume_constants4.education2duration+r'''</div>
		<div class="job-description">'''+Resume_constants4.education2desc+r'''</div>
	  </div>
	  <div class="job-box">
		<div class="job-title">'''+Resume_constants4.education3course+" "+r'''@'''+Resume_constants4.education3+r'''</div>
		<div class="job-date">'''+Resume_constants4.education3duration+r'''</div>
		<div class="job-description">'''+Resume_constants4.education3desc+r'''</div>
	  </div>
	</div>
	</div>
	<div class="skills">
	  <div class="work-img"> <img src="data:image/png;base64,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">
	  </div>
	  <h1>Skills</h1>
	  <div class="graph">
		<ul>
		  <li class="l1">'''+Resume_constants4.skill1+r'''</li>
		  <li class="l2">'''+Resume_constants4.skill2+r'''</li>
		  <li class="l3">'''+Resume_constants4.skill3+r'''</li>
		  <li class="l4">'''+Resume_constants4.skill4+r'''</li>
		</ul>
	  </div>
	</div>
	<div class="interest">
	  <div class="work-img"> <img src="data:image/png;base64,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">
	  </div>
	  <h1>Interests</h1>
      <div class="graph">
		<ul>
		  <li class="l1">'''+Resume_constants4.interest1+r'''</li>
		  <li class="l2">'''+Resume_constants4.interest2+r'''</li>
		  <li class="l3">'''+Resume_constants4.interest3+r'''</li>
		  <li class="l4">'''+Resume_constants4.interest4+r'''</li>
		</ul>
	  </div>
	</div>
  </body>'''

with open('resume.html','wb') as f:
    f.write(bytes(file_content,encoding='utf8'))