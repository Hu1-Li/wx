import werobot
from werobot import WeRoBot
robot = WeRoBot()
robot.config.from_pyfile("config.py")
# custom menu
client = robot.client
client.create_menu({
    "button": [{
         "type": "click",
         "name": "About Me",
         "key": "about"
    }, {
        "name": "Menu",
        "sub_button": [{
            "type": "view",
            "name": "Personal Site",
            "url": ""
        }],
    }]
})
