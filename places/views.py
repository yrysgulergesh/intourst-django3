from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import FormView, DetailView
from .models import Place, Feedback
from .forms import PlaceForm, FeedbackForm



def places(request):
    place_objects = Place.objects.all()
    return render(request, 'places/places.html', {'places': place_objects})


def create_place(request):
    if request.method == "POST":
        place_form = PlaceForm(request.POST)
        if place_form.is_valid():
            place_form.save()
            return redirect(places)

    place_form = PlaceForm()
    return render(request, 'places/form.html', {'place_form': place_form})


def place(request, id):
    try:
        place_object = Place.objects.get(id=id)
        return render(request, 'places/place.html', {'place_object': place_object})
    except Place.DoesNotExist as e:
        return HttpResponse(f'Not found: {e}', status=404)


def edit_place(request, id):
    place_object = Place.objects.get(id=id)

    if request.method == 'POST':
        place_form = PlaceForm(data=request.POST, instance=place_object)
        if place_form.is_valid():
            place_form.save()
            return redirect(place, id=id)

    place_form = PlaceForm(instance=place_object)
    return render(request, 'places/form.html', {'place_form': place_form})


def delete_place(request, id):
    place_object = Place.objects.get(id=id)
    place_object.delete()
    return redirect(places)


class FeedbackView(FormView):
    template_name = 'places/feedback_form.html'
    form_class = FeedbackForm
    success_url = '/places/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class FeedbackDetailView(DetailView):
    queryset = Feedback.objects.all()
    template_name = 'places/feedback.html'
