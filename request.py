import requests


class SendRequest:
    def __init__(self, URL, Header,Body):
        self.URL=URL
        self.Header=Header
        self.Body=Body
    def POST_Send(self):
        request =requests.post(self.URL, headers=self.Header , json =self.Body )
        print(request.text)
        return request