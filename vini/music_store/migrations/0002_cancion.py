# Generated by Django 4.2.1 on 2023-07-02 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=200)),
                ('imagen', models.ImageField(null=True, upload_to='img/')),
                ('musica', models.FileField(upload_to='musica/')),
                ('fecha_publicacion', models.DateField()),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_store.genero')),
            ],
        ),
    ]
