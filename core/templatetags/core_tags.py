# from django import template
# from django.db.models import Count
# from accounts import models


# register = template.Library()


# @register.simple_tag
# def total_users():
# 	users=User.objects.all()
# 	return users.count()


# # @register.inclusion_tag('blog/post/latest_posts.html')
# # def show_latest_posts(count=5):
# #     latest_posts = Post.published.order_by('-publish')[:count]
# #     return {'latest_posts': latest_posts}


# # @register.simple_tag
# # def get_most_commented_posts(count=5):
# #     return Post.published.annotate(
# #                total_comments=Count('comments')
# #            ).order_by('-total_comments')[:count]


# # @register.filter(name='markdown')
# # def markdown_format(text):
# #     return mark_safe(markdown.markdown(text))