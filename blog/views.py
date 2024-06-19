from django.views.generic import TemplateView

# Create your views here.
class blog(TemplateView):
    template_name = "blog/blog.html"

