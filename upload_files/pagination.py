from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginate(self, posts_list):
    paginator = Paginator(posts_list, 25)
    page = self.GET.get('page')
    try:
        matched_data = paginator.page(page)
    except PageNotAnInteger:
        matched_data = paginator.page(1)
    except EmptyPage:
        matched_data = paginator.page(paginator.num_pages)
    return matched_data
