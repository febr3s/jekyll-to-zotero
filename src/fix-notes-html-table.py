import re

# Open the HTML file
with open('/home/febres/Documents/dev/MOREL 2.0/content/table.html', 'r') as file:
    html = file.read()

# Task 1: Delete "<p><br><br>" and "<br></p>"
html = re.sub(r'&lt;p&gt;<br><br>', '', html)
html = re.sub(r'&lt;p&gt;<br> <br>', '', html)
html = re.sub(r'&lt;p&gt;<br>', '', html)
html = re.sub(r'<br>&lt;/p&gt;', '', html)

# Task 2: Replace "<br /><br />" with "<br />"
html = re.sub(r'<br /> <br />', '<br />', html)
html = re.sub(r'<br> <br>', '<br>', html)
html = re.sub(r'<br><br>', '<br>', html)

# Write the modified HTML back to the file
with open('/home/febres/Documents/dev/MOREL 2.0/content/table.html', 'w') as file:
    file.write(html)
