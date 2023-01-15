class test:
    @staticmethod
    def assert_equals(path, value):

        if path == value:
            return
        else:
            raise ValueError