import json


# record class  - represent a record.
class Record:
    def __init__(self, link, image, title, content):
        self.link = link
        self.image = image
        self.title = title
        self.content = content

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @staticmethod
    def from_json(json_string):
        dictionary = json.loads(json_string.decode("utf-8"))
        link = str(dictionary["link"])
        image = str(dictionary["image"])
        title = str(dictionary["title"])
        content = str(dictionary["content"])
        return Record(link, image, title, content)
