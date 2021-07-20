from django.http import HttpResponse

class AdminRequiredMixin:
    
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_staff == True:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse('<h2>you are not admin</h2>') 