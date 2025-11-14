class basicMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print(request,"hello")
        print(request.method,"method")
        if(request.path=="/addstudent/"):
            response=self.get_response(request)
            return response
        

