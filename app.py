# import helloworld273
from flask import Flask, render_template, Response
# emulated camera
from camera import Camera

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello from Flask App!!"

'''
reference: https://github.com/miguelgrinberg/flask-video-streaming/blob/master/app.py
'''


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=9000)
