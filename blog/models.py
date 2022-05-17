from django.contrib.auth.models import AbstractUser
from django.db import models


class Post(models.Model):
    '''
    Модель поста блога пользователя.
    '''
    author = models.ForeignKey(
        'CustomUser',
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='автор')
    blog = models.ForeignKey(
        'Blog',
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='блог'
    )
    title = models.CharField('заголовок', max_length=12)
    text = models.CharField('текст', max_length=140)
    pub_date = models.DateTimeField('дата создания', auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['author', 'title'], name='unique_post')]
        ordering = ['-pub_date']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Blog(models.Model):
    '''
    Модель блога.
    '''
    author = models.OneToOneField(
        'CustomUser',
        on_delete=models.CASCADE,
        related_name='blog',
        verbose_name='автор',
        unique=True)
    created_date = models.DateTimeField('дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['created_date']


class CustomUser(AbstractUser):
    '''
    Кастомная модел пользователя.
    При сохранении пользователя создается личный блог.
    '''
    read_post = models.ManyToManyField(Post)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        Blog.objects.get_or_create(author=self)


class BlogFollow(models.Model):
    '''
    Модель подписки
    '''
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='followers',
        verbose_name='блог'
    )
    follower = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='blogs',
        verbose_name='подписчики'
    )

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['blog', 'follower'], name='uniq_follow')]
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ['pk']


# class PostState(models.Model):
#     user = models.ForeignKey(
#         CustomUser,
#         on_delete=models.CASCADE,
#         related_name='post_state',
#         verbose_name='пользователь'
#     )
#     post = models.ManyToManyField(Post, unique=True)

#     class Meta:
#         constraints = [models.UniqueConstraint(
#             fields=['user', 'post'], name='uniq_read')]
#         verbose_name = 'Состояние'
#         verbose_name_plural = 'Состояния'
