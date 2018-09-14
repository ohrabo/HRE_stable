from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from taggit.models import Tag

from library.forms import EmailTextForm
from .models import Text

class TextListView(ListView):
    queryset = Text.published.all()
    context_object_name = 'library'
    paginate_by = 3
    template_name = 'library/list.html'

def text_list(request, tag_slug=None):
    texts_list = Text.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        texts_list = texts_list.filter(tags__in=[tag])

    paginator = Paginator(texts_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        library = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        library = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        library = paginator.page(paginator.num_pages)
    return render(request,
                  'library/list.html',
                  {'page': page,
                      'library': library,
                       'tag': tag})


def text_detail(request, year, month, day, text):
    text = get_object_or_404(Text, slug=text,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    # List of similar articles
    text_tags_ids = text.tags.values_list('id', flat=True)
    similar_articles = Text.published.filter(tags__in=text_tags_ids).exclude(id=text.id)
    similar_articles = similar_articles.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
    return render(request,
                  'library/detail.html',
                  {'text': text,
                   'similar_articles': similar_articles})

def text_share(request, text_id):
    # Retrieve article by id
    text = get_object_or_404(Text, id=text_id, status='published')
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailTextForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            text_url = request.build_absolute_uri(text.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], text.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(text.title, text_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@hre.com', [cd['to']])
            sent = True
    else:
        form = EmailTextForm()
    return render(request, 'library/share.html', {'text': text,
                                                    'form': form,
                                                    'sent': sent})