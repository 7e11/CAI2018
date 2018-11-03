import os, shutil, time

template = """<h2>TIME: </h2><video loop width="640" height="480" controls>
  <source src="videos/INDEX.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>"""

html_body = ""

indexes = os.listdir("../fake_redis")
indexes.sort()
for index in indexes:
    html_body += template.replace("INDEX", index).replace("TIME", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(index))))
    with open("../fake_redis/" + index) as file:
        token = file.read()
        shutil.copyfile("../fake_blockchain/" + token, "videos/" + index + ".mp4")

with open("template.html") as template:
    template = template.read().replace("BODY", html_body)
    with open("index.html", "w") as index:
        index.write(template)
