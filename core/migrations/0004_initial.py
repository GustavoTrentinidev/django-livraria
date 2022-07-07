# Generated by Django 4.0.5 on 2022-07-07 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0003_delete_autor_delete_categoria_delete_editora_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('site', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('ISBN', models.CharField(max_length=32)),
                ('quantidade', models.IntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='livros', to='core.categoria')),
                ('editora', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='livros', to='core.editora')),
            ],
        ),
    ]