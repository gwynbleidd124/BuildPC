from django.views.generic import DetailView

from Build.models import Computer


# class PCConfigurationDetailView(LoginRequiredMixin, DetailView):
#     model = Computer
#     template_name = 'configuration_detail.html'
#     context_object_name = 'configuration'
#     login_url = 'login'
#
#     def get_queryset(self):
#         return Computer.objects.filter(kwargs={'slug': self.objects.slug})



