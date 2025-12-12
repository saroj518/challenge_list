from django.shortcuts import render
from .models import Challenge, Solve
from django.views.generic import ListView, DetailView


class ChallengeListView(ListView):
    model = Challenge
    template_name = 'list.html'
    context_object_name = 'challenges'
    
class ChallengeDetailView(DetailView):
    model = Challenge
    template_name = 'detail.html'
    context_object_name = 'challenge'
    

class SolveView(DetailView):
    model = Challenge
    template_name = 'solve.html'
    context_object_name = 'challenge'
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        flag_submitted = request.POST.get('flag')
        is_correct = flag_submitted == self.object.flag

        Solve.objects.create(
            user=request.user,
            challenge=self.object,
            submitted_flag=flag_submitted,
            is_correct=is_correct
        )

        context = self.get_context_data(object=self.object)
        context['is_correct'] = is_correct
        return self.render_to_response(context)