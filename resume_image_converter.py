#instantiate package
from html2image import Html2Image #instantiate package
hti = Html2Image()

hti = Html2Image()

hti.screenshot(
    html_file='resume.html', css_file='resume_pattern1.css',
    save_as='resume_image.jpg'
)