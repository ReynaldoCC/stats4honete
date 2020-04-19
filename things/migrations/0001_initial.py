# Generated by Django 3.0 on 2020-04-18 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import things.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.CharField(blank=True, max_length=10, null=True)),
                ('server_game_name', models.CharField(blank=True, max_length=100, null=True)),
                ('game_name', models.CharField(blank=True, max_length=60, null=True)),
                ('game_version', models.CharField(blank=True, max_length=10, null=True)),
                ('match_name', models.CharField(blank=True, max_length=50, null=True)),
                ('map_name', models.CharField(blank=True, max_length=50, null=True)),
                ('map_version', models.CharField(blank=True, max_length=10, null=True)),
                ('match_date', models.DateField(blank=True, null=True)),
                ('match_time', models.TimeField(blank=True, null=True)),
                ('log_file', models.FileField(upload_to=things.models.scramble_upload_log, verbose_name='Archivo Log')),
                ('team_win', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('win_time', models.PositiveIntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'verbose_name': 'Juego',
                'verbose_name_plural': 'Juegos',
                'ordering': ('match_date',),
            },
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre del h€roe que se muestra.', max_length=50, verbose_name='Nombre')),
                ('slug', models.CharField(help_text='Nombre con que se identifica el h€roe en los logs.', max_length=50, verbose_name='Slug')),
                ('team', models.IntegerField(choices=[{'HELLBOURNE', 1}, {2, 'LEGION'}], default=1, help_text='Equipo o Facción al que pertenece el héroe.', verbose_name='Equipo')),
                ('type', models.IntegerField(choices=[{1, 'AGILIDAD'}, {2, 'FUERZA'}, {3, 'INTELIGENCIA'}], help_text='Tipo del héroe', verbose_name='Tipo')),
                ('atack', models.IntegerField(choices=[{'MELEE', 1}, {2, 'RANGO'}], verbose_name='Ataca')),
                ('image', models.ImageField(default=None, help_text='Avatar del héroe, que se muestra en la lista.', null=True, upload_to=things.models.scramble_upload_avatar, verbose_name='Avatar')),
                ('background', models.ImageField(default='', help_text='Background mostrado en la pagina de detalles del héroe.', upload_to=things.models.scramble_upload_background, verbose_name='Background')),
                ('detail_pic', models.ImageField(default='', help_text='Imagen con una descripción del héroe, sus habilidades y recomendaciones.', upload_to=things.models.scramble_upload_detail, verbose_name='Detalle')),
            ],
            options={
                'verbose_name': 'Heroe',
                'verbose_name_plural': 'Heroes',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Nombre')),
                ('description', models.TextField(max_length=300, verbose_name='Efecto')),
                ('imagen', models.ImageField(default=None, null=True, upload_to=things.models.scramble_upload_avatar, verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Objeto',
                'verbose_name_plural': 'Objetos',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ItemStrategic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_time', models.IntegerField(choices=[{1, 'STARTING'}, {2, 'MEDIUM'}, {2, 'END'}, {'OPTIONALS', 2}, {2, 'FULLPOWER'}], default=1, help_text='Momento de juego en que se debe obtener el objeto.', verbose_name='Momento del objeto')),
                ('item', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='things.Item')),
            ],
        ),
        migrations.CreateModel(
            name='LvlSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lvl_number', models.PositiveSmallIntegerField(verbose_name='Nivel')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('userprof', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Jugador',
                'verbose_name_plural': 'Jugadores',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Nombre')),
                ('description', models.TextField(max_length=200, verbose_name='Efecto')),
                ('imagen', models.ImageField(default=None, null=True, upload_to=things.models.scramble_upload_avatar, verbose_name='Logo')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Strategic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='Nombre')),
                ('description', models.TextField(max_length=600)),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='things.Hero', verbose_name='Héroe')),
                ('items', models.ManyToManyField(blank=True, through='things.ItemStrategic', to='things.Item')),
                ('skills', models.ManyToManyField(blank=True, through='things.LvlSkill', to='things.Skill')),
            ],
            options={
                'verbose_name': 'Estrategia',
                'verbose_name_plural': 'Estrategias',
                'ordering': ('name', 'hero__name'),
            },
        ),
        migrations.CreateModel(
            name='PlayersGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(blank=True, max_length=17, null=True)),
                ('player_pos', models.IntegerField(blank=True, default=100, null=True)),
                ('team', models.IntegerField(blank=True, default=0, null=True)),
                ('kills', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('dead', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('experiens', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True)),
                ('golds', models.IntegerField(blank=True, default=0, null=True)),
                ('assitances', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('damage', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True)),
                ('firstblood', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('firstblood_die', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='things.Game')),
                ('hero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='things.Hero')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='things.Player')),
            ],
            options={
                'verbose_name': 'Jugador en Juego',
                'verbose_name_plural': 'Jugadores en Juego',
            },
        ),
        migrations.AddField(
            model_name='lvlskill',
            name='skill',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='things.Skill'),
        ),
        migrations.AddField(
            model_name='lvlskill',
            name='strategic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='things.Strategic'),
        ),
        migrations.AddField(
            model_name='itemstrategic',
            name='strategic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='things.Strategic'),
        ),
        migrations.AddField(
            model_name='hero',
            name='skills',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='things.Skill', verbose_name='habilidades'),
        ),
        migrations.AddField(
            model_name='game',
            name='players_onplay',
            field=models.ManyToManyField(blank=True, related_name='players_onplay', through='things.PlayersGame', to='things.Player'),
        ),
    ]
