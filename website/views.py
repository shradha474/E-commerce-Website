

# Create your views here.
from .models import Products, Index_skirts,Index_sarees,checkout, Index_kids, Index_footwear, Index_products, Index_salwar, Index_watch, Index_dress, Index_sweaters, Index_jeans, Index_shirts
from django.views import generic
from django.views.generic import TemplateView
from django.template import loader
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.views.generic import View
from .forms import UserForm

##from .models import Products

# Create your views here.

def homepageview(request):

  all_products= Products.objects.all()


  template = loader.get_template('index.html')

  context = { 'all_products': all_products, }

  return render(request, 'index.html', context)



class aboutview(TemplateView):

	template_name="about.html"

class checkoutview(generic.ListView):

         template_name="checkout.html"

         context_object_name='all_products'

         def get_queryset(self):
              return Products.objects.all()

         def get_context_data(self, **kwargs):
             context = super(checkoutview, self).get_context_data(**kwargs)
             context['all_dresses'] = Index_dress.objects.all()[:5]
             # ^^^ bad duplication.
             return context





class dressview(generic.ListView):

    	template_name="dresses.html"

    	context_object_name='all_dresses'

    	def get_queryset(self):
             return Index_dress.objects.all()

        def get_context_data(self, **kwargs):
            context = super(dressview, self).get_context_data(**kwargs)
            context['all_sweaters'] = Index_sweaters.objects.all()[:5]
            # ^^^ bad duplication.
            return context

class faqview(TemplateView):

	template_name="faq.html"

class jeansview(generic.ListView):

    	template_name="jeans.html"

    	context_object_name='all_jeans'

    	def get_queryset(self):
             return Index_jeans.objects.all()

        def get_context_data(self, **kwargs):
            context = super(jeansview, self).get_context_data(**kwargs)
            context['all_shirts'] = Index_shirts.objects.all()[:5]
            # ^^^ bad duplication.
            return context


class mailview(TemplateView):

	template_name="mail.html"

class productsview(generic.ListView):

    	template_name="products.html"

        context_object_name='all_products'

        def get_queryset(self):
             return Index_products.objects.all()

        def get_context_data(self, **kwargs):
            context = super(productsview, self).get_context_data(**kwargs)
            context['all_sandals'] = Index_footwear.objects.all()[:5]
            # ^^^ bad duplication.
            return context

class salwarsview(generic.ListView):

    	template_name="salwars.html"

    	context_object_name='all_salwar'

    	def get_queryset(self):
             return Index_salwar.objects.all()

        def get_context_data(self, **kwargs):
            context = super(salwarsview, self).get_context_data(**kwargs)
            context['all_skirts'] = Index_skirts.objects.all()[:5]
            # ^^^ bad duplication.
            return context

class sandalsview(generic.ListView):

    	template_name="sandals.html"

        context_object_name='all_sandals'

        def get_queryset(self):
             return Index_footwear.objects.all()

        def get_context_data(self, **kwargs):
            context = super(sandalsview, self).get_context_data(**kwargs)
            context['all_products'] = Index_products.objects.all()[:5]
            # ^^^ bad duplication.
            return context

class sareesview(generic.ListView):

    	template_name="sarees.html"

    	context_object_name='all_sarees'

    	def get_queryset(self):
             return Index_sarees.objects.all()

        def get_context_data(self, **kwargs):
            context = super(sareesview, self).get_context_data(**kwargs)
            context['all_jeans'] = Index_jeans.objects.all()[:5]
            # ^^^ bad duplication.
            return context

class shirtsview(generic.ListView):

    	template_name="shirts.html"

    	context_object_name='all_shirts'

    	def get_queryset(self):
             return Index_shirts.objects.all()

        def get_context_data(self, **kwargs):
            context = super(shirtsview, self).get_context_data(**kwargs)
            context['all_salwar'] = Index_salwar.objects.all()[:5]
            # ^^^ bad duplication.
            return context

class kidswearview(generic.ListView):

    	template_name="kidswear.html"

        context_object_name='all_kids'

        def get_queryset(self):
             return Index_kids.objects.all()

        def get_context_data(self, **kwargs):
            context = super(kidswearview, self).get_context_data(**kwargs)
            context['all_sweaters'] = Index_sweaters.objects.all()[:5]
            # ^^^ bad duplication.
            return context



class skirtsview(generic.ListView):

       template_name="skirts.html"

       context_object_name='all_skirts'

       def get_queryset(self):
            return Index_skirts.objects.all()

       def get_context_data(self, **kwargs):
           context = super(skirtsview, self).get_context_data(**kwargs)
           context['all_sarees'] = Index_sarees.objects.all()[:5]
           # ^^^ bad duplication.
           return context

class sweatersview(generic.ListView):

    	template_name="sweaters.html"
    	context_object_name='all_sweaters'

    	def get_queryset(self):
             return Index_sweaters.objects.all()

        def get_context_data(self, **kwargs):
            context = super(sweatersview, self).get_context_data(**kwargs)
            context['all_dresses'] = Index_dress.objects.all()[:5]
            # ^^^ bad duplication.
            return context

class UserFormView(View):
    form_class = UserForm
    template_name = 'formtemp.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form  })

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
           user = form.save(commit=False)
           username = form.cleaned_data['username']
           password = form.cleaned_data['password']
           user.set_password(password)
           user.save()

           user = authenticate(username=username, password=password)

           if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

        return render(request, self.template_name, {'form': form  })

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'formtemp.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'formtemp.html', {'error_message': 'Invalid login'})
    return render(request, 'formtemp.html')


def single_sweaterView(request, pk):
    index_sweater = Index_sweaters.objects.get(pk=pk)
    context = {'index_sweater': index_sweater, }

    return render(request, 'single.html', context)

def single_skirtsView(request, pk):
    index_skirt = Index_skirts.objects.get(pk=pk)
    context = {'index_skirt': index_skirt, }

    return render(request, 'single.html', context)


def single_jeansView(request, pk):
    index_jeans = Index_jeans.objects.get(pk=pk)
    context = {'index_jeans': index_jeans, }

    return render(request, 'single.html', context)

def single_shirtsView(request, pk):
    index_shirts = Index_shirts.objects.get(pk=pk)
    context = {'index_shirts': index_shirts, }

    return render(request, 'single.html', context)


def single_salwarsView(request, pk):
    index_salwar = Index_salwar.objects.get(pk=pk)
    context = {'index_salwar': index_salwar, }

    return render(request, 'single.html', context)

def productsView(request, pk):
    index_products = Index_products.objects.get(pk=pk)
    context = {'index_products': index_products, }

    return render(request, 'single.html', context)


def single_sareesView(request, pk):
    index_sarees = Index_sarees.objects.get(pk=pk)
    context = {'index_sarees': index_sarees, }

    return render(request, 'single.html', context)

def single_sandalsView(request, pk):
    index_footwear = Index_footwear.objects.get(pk=pk)
    context = {'index_footwear': index_footwear, }

    return render(request, 'single.html', context)

def single_indexView(request, pk):
    products = Products.objects.get(pk=pk)
    context = {'products': products, }

    return render(request, 'single.html', context)

def single_kidsView(request, pk):
    index_kids = Index_kids.objects.get(pk=pk)
    context = {'index_kids': index_kids, }

    return render(request, 'single.html', context)


def singleView(request, pk):
    index_dress = Index_dress.objects.get(pk=pk)
    context = {'index_dress': index_dress, }

    return render(request, 'single.html', context)
