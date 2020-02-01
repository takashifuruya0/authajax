from django.shortcuts import reverse
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, RedirectView, ListView
from django.contrib import messages
from web.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ArticleForm


# Create your views here.


class ArticleListView(LoginRequiredMixin, ListView):
    template_name = "web/article_list.html"
    model = Article


class ArticleDetailView(LoginRequiredMixin, DetailView):
    template_name = "web/article_detail.html"
    model = Article


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "web/article_update.html"
    model = Article
    form_class = ArticleForm

    def get_success_url(self):
        return reverse('web:article_detail', kwargs={'pk': self.object.pk})


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "web/article_create.html"
    model = Article
    form_class = ArticleForm

    def get_success_url(self):
        return reverse('web:article_detail', kwargs={'pk': self.object.pk})


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    form_class = ArticleForm
    template_name = "web/article_delete.html"

    def get_success_url(self):
        return reverse('web:article_list')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, '「{}」を削除しました'.format(self.object))
        return result
