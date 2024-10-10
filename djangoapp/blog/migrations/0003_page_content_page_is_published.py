# Generated by Django 5.1.1 on 2024-10-10 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='is_published',
            field=models.BooleanField(default=False, help_text='Este campo precisa estar selecionado para página ser exibida!'),
        ),
    ]
