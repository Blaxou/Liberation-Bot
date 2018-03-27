import json

class Database(object):
    """
This class manages the dabase in the LBot
    """

    def __init__(self, filename):
        self.filename = filename

    def presence_check(self):

        try:
            self.read()
            return True
        except Exception as e:
            return (False, Exception)

    def read(self):

        return json.load(open(self.filename, 'r'))

    def write(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f)

    def get_user_data(self, userID):

        return self.read()['users'][str(userID)]

    def add_lesson(self, userID, lesson):

        db = self.read()

        db['users'][str(userID)]['lessons'].append(lesson)

        self.write(db)

    def remove_lesson(self, userID, lesson):

        db = self.read()

        db['users'][str(userID)]['lessons'].remove(lesson)

        self.write(db)

    def register_user(self, userID):

        db = self.read()

        db['users'][str(userID)] = {"lessons": []}

        self.write(db)
