### Module 9 Docker
#### TASK 9.3 

 1. Creating "pyapp" project folder.

 ![](Screenshots/1.png)
 
 2. Creating next files:
 
 - app.py - python script file;
 - requirements.txt - project requirements file;
 - index.html in templates folder - file with html code;
 - Dockerfile - file with configuration of docker.
 
 ![](Screenshots/2.png)
 
 3. "app.py" file contains:
 
```python
 from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
	"https://images.pexels.com/photos/1666012/pexels-photo-1666012.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
	"https://images.pexels.com/photos/4215113/pexels-photo-4215113.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
	"https://images.pexels.com/photos/1785493/pexels-photo-1785493.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
	"https://images.pexels.com/photos/4261096/pexels-photo-4261096.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
	"https://images.pexels.com/photos/5273712/pexels-photo-5273712.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
	"https://images.pexels.com/photos/5166338/pexels-photo-5166338.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
	"https://images.pexels.com/photos/1755243/pexels-photo-1755243.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
	"https://images.pexels.com/photos/2365457/pexels-photo-2365457.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
	"https://images.pexels.com/photos/2724664/pexels-photo-2724664.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
	"https://images.pexels.com/photos/2387876/pexels-photo-2387876.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
	"https://images.pexels.com/photos/2444429/pexels-photo-2444429.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
	"https://images.pexels.com/photos/3389536/pexels-photo-3389536.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
```
 
 4. "Dockerfile" file contains:
  
```bash
  # our base image
FROM alpine:3.5

# Install python and pip
RUN apk add --update py2-pip

# upgrade pip
RUN pip install --upgrade pip

# install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# copy files required for the app to run
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "/usr/src/app/app.py"]
```
  
  4. "Dockerfile" file contains:
  
```html
  <html>
  <head>
    <style type="text/css">
      body {
        background: black;
        color: white;
      }
      div.container {
        max-width: 1500px;
        margin: 100px auto;
        border: 20px solid white;
        padding: 10px;
        text-align: center;
      }
      h4 {
        text-transform: uppercase;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Mount photo of the day</h1>
      <img src="{{url}}" />
    </div>
  </body>
</html>
```
 5. Build docker image.
  
 ![](Screenshots/3.png)
 
 ![](Screenshots/4.png)
 
 6. Update version of python.
 
 ![](Screenshots/5.png)
 
 ![](Screenshots/6.png)
 
 7. Rup docker container.
 
 ![](Screenshots/7.png)
 
 ![](Screenshots/8.png)
<<<<<<< HEAD
 
 8. Check result in brouser.
 
 ![](Screenshots/9.png)
 
=======
 ![Alt Text](https://github.com/Yevhenii-Orlov/DevOps_online_Kiev_2020Q42021Q1/blob/main/m9/Task9.3/Screenshots/9.gif)
 
>>>>>>> 695e55de8487820ef42471b6c98eb6376351b2c0
