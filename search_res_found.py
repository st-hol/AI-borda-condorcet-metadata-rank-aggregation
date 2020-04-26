class SearchResultFound:

    def __init__(self, json, voter_engine):
        self.voter_engine = voter_engine

        try:
            self.position = json['position']
        except KeyError:
            self.position = None

        try:
            self.title = json['title']
        except KeyError:
            self.title = None

        try:
            self.link = json['link']
        except KeyError:
            self.link = None

        try:
            self.domain = json['domain']
        except KeyError:
            self.domain = None

        try:
            self.snippet = json['snippet']
        except KeyError:
            self.snippet = None

        try:
            self.snippet_matched = json['snippet_matched']
        except KeyError:
            self.snippet_matched = None

    def __str__(self):
        # Override to print a readable string presentation of your object
        # below is a dynamic way of doing this without explicity constructing the string manually
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])

    def pretty_print(self):
        print("-" * 100)
        print("voter engine: ", self.voter_engine)
        print("position: ", self.position)
        print("title: ",  self.title)
        print("link: ",  self.link)
        print("domain: ",  self.domain)
        print("snippet: ",  self.snippet)
        print("snippet_matched: ",  self.snippet_matched)
        print("-" * 100)
