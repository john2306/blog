# Generated by Django 3.0.4 on 2020-03-26 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Título:')),
                ('description', models.CharField(blank=True, help_text='Descripción corto del artículo o frases relevantes de la misma.', max_length=255, null=True, verbose_name='Descripción:')),
                ('image', models.URLField(blank=True, default='https://www.karlosperu.com/wp-content/uploads/2019/09/conectividad.png', help_text='Buscar imagen relacionado al artículo y pegar aquí la dirección URL de la imagen.', null=True, verbose_name='Imagen de portada (URL)')),
                ('slug', models.SlugField(blank=True, max_length=300, null=True)),
                ('category', models.CharField(blank=True, choices=[('general', 'General'), ('datascience', 'Ciencia de datos'), ('neurociencia', 'Neurociencia'), ('projects', 'Proyectos')], default='general', max_length=20, null=True, verbose_name='Categoría')),
                ('body', tinymce.models.HTMLField(blank=True, help_text='Te recomendamos diseñar el artículo en Word y pegar en esta parte.', null=True, verbose_name='CONTENIDO te recomendamos diseñar el artículo en Word y pegar en esta parte: ')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('delete', models.BooleanField(default=False, verbose_name='Borrado/No borrado')),
                ('status', models.BooleanField(default=True, verbose_name='Publicar/No publicar')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=140)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='articles.Article')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
