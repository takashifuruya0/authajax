from allauth.account import views
from allauth.account.forms import LoginForm
from django.shortcuts import HttpResponse, Http404, redirect
import json


class HomeView(views.TemplateView):
    template_name = 'accounts/home.html'


class SigninView(views.LoginView):
    template_name = 'accounts/signin.html'

    def dispatch(self, request, *args, **kwargs):
        response = super(SigninView, self).dispatch(request, *args, **kwargs)
        return response

    def form_valid(self, form):
        return super(SigninView, self).form_valid(form)


class SignupView(views.SignupView):
    template_name = 'accounts/signup.html'

    def get_context_data(self, **kwargs):
        context = super(SignupView, self).get_context_data(**kwargs)
        return context


class SignoutView(views.LogoutView):

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.logout()
        return redirect('/')


def ajax_login(request):
    if request.method == 'POST':
        # ログイン処理
        form = LoginForm(request.POST)
        if form.is_valid():
            status = "OK"
            form.login(request)
        else:
            status = "NG"
        # レスポンス形成
        res = {
            "status": status,
            "username": request.user.get_username(),
        }
        json_str = json.dumps(res, ensure_ascii=False, indent=2)
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=None)
        return response
    else:
        raise Http404
