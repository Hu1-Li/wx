# coding=utf-8
import werobot
import tempfile
import requests
from werobot.replies import TextReply, ImageReply
from werobot import WeRoBot
robot = WeRoBot()
robot.config.from_pyfile("config.py")
client = robot.client

# message handler
@robot.text
def echo(message, session):
    session["count"] = session.get("count", 0) + 1
    if message.content.startswith("/site"):
        return "https://Hu1-Li.github.io"
    elif message.content.startswith("/count"):
        return "You have sent {0} messages".format(session["count"])
    elif message.content.startswith("/help"):
        return "Supported special message: /site, /count"
    else:
        #return message.raw
        return TextReply(message=message, content=message.content)

# handle image message
def url_img_to_fd(img_url):
    f = tempfile.NamedTemporaryFile(mode="wb", delete=False, dir=robot.config["DATA_DIR"], suffix=".jpeg")
    f.write(requests.get(img_url).content)
    f.close()
    return open(f.name, "rb")


@robot.image
def img(message):
    #media_id = client.upload_media("image", url_img_to_fd(message.img))["media_id"]
    media_id = message.media_id
    return ImageReply(message=message, media_id=media_id)

# handle voice message
@robot.voice
def voice(message):
    if message.recognition is None:
        return "Failed to recognize voice message"
    return "voice message: {0}".format(message.recognition.encode("utf-8"))

# handle location
@robot.location_event
def loc_evt(message):
    return "location: {0}, {1}".format(message.latitude, message.longitude)

@robot.location
def loc_msg(message):
    return "location: {0}, {1}".format(message.location, message.label.encode("utf-8"))

# handle click menu
@robot.key_click("about")
def about(message):
    return "你好"

robot.run()
