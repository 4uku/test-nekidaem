from django.core.mail import send_mail

from blog.models import CustomUser, Post


def my_job():
    users = CustomUser.objects.filter(is_active=True)
    for user in users:
        last_posts = Post.objects.filter(
            blog__followers__in=user.blogs.values('id'))[:5]
        message = 'Новые посты:'
        for post in last_posts:
            message += '\nАвтор: '\
                       f'{post.author.username}\n{post.title}\n{post.text}\n'
        send_mail(
            'Новые посты',
            message,
            'admin@test.ru',
            [f'{user.username}@test.ru']
        )
