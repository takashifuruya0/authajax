from django.shortcuts import reverse
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, RedirectView, ListView
from django.contrib import messages
from web.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ArticleForm
from rules.contrib.views import PermissionRequiredMixin


# Create your views here.


class ArticleListView(LoginRequiredMixin, ListView):
    template_name = "web/article_list.html"
    model = Article


class ArticleDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    template_name = "web/article_detail.html"
    model = Article
    permission_required = 'web.rules_read_article'
    permission_denied_message = "Error"


class ArticleUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = "web/article_update.html"
    model = Article
    form_class = ArticleForm
    permission_required = 'web.rules_update_article'


    def get_success_url(self):
        return reverse('web:article_detail', kwargs={'pk': self.object.pk})


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "web/article_create.html"
    model = Article
    form_class = ArticleForm

    def get_success_url(self):
        return reverse('web:article_detail', kwargs={'pk': self.object.pk})


class ArticleDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Article
    form_class = ArticleForm
    template_name = "web/article_delete.html"
    permission_required = "web.rules_delete_article"
    permission_denied_message = "Not owned by you"

    def get_success_url(self):
        return reverse('web:article_list')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, '「{}」を削除しました'.format(self.object))
        return result
