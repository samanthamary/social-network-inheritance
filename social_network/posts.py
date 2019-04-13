from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp
        self.user = None

    def set_user(self, user):
         self.user = user


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp)

    def __str__(self):
        post_time = datetime.strftime(self.timestamp, '%A, %b %d, %Y')
        return '@{fn} {ln}: "{text}"\n\t{time}'.format(fn=self.user.first_name, ln=self.user.last_name, text=self.text, time=post_time)


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url

    def __str__(self):
        post_time = datetime.strftime(self.timestamp, '%A, %b %d, %Y')
        return '@{fn} {ln}: "{text}"\n\t{url}\n\t{time}'.format(fn=self.user.first_name, ln=self.user.last_name, text=self.text, url=self.image_url, time=post_time)


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        post_time = datetime.strftime(self.timestamp, '%A, %b %d, %Y')
        return '@{fn} Checked In: "{text}"\n\t{lat}, {long}\n\t{time}'.format(fn=self.user.first_name, text=self.text, lat=self.latitude, long=self.longitude, time=post_time)
