from django.shortcuts import render
from django.views.generic import TemplateView


def home_page_view(request):
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "Thank you for visiting",
    }
    return render(request, "home.html", context)


class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123"
        context["phone_number"] = "054-903-2222"

        return context
