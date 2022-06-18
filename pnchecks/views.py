from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import FileFieldForm
from .utils import pneumonia_check


class FileFieldFormView(FormView):
    form_class = FileFieldForm
    template_name = 'pnchecks/index.html'
    success_url = '/result/'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        image = request.FILES.get('upload_image')
        if form.is_valid():
            result = pneumonia_check(image)
            return render(request, 'pnchecks/result.html', context=result)
        else:
            return self.form_invalid(form)


def result(request):
    return render(request, 'pnchecks/result.html')


def about(request):
    return render(request, 'pnchecks/about.html')


def contact(request):
    return render(request, 'pnchecks/contact.html')
