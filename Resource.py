class Resource:

    def __init__(self, **kwargs):
        self.imgs = {}
        for k, v in kwargs.items():
            self.imgs[k] = v

    def __getitem__(self, key):
        return self.imgs[key]
