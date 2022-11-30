from django.views.generic import ListView

from employee.models import Employee, Division


class DivisionListView(ListView):
    model = Division
    template_name = "division_list.html"

    def get_queryset(self):
        queryset = super().get_queryset().select_related('parent')
        if division := self.kwargs.get('division_slug'):
            self.employees = Employee.objects.filter(division__slug=division).select_related('division', 'position')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if hasattr(self, 'employees'):
            context['employees'] = self.employees

        return context
