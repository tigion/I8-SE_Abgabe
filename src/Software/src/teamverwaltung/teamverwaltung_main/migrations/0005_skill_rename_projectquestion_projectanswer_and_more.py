# Generated by Django 4.0.4 on 2022-04-15 22:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teamverwaltung_main', '0004_role_student_poll_rolequestion_projectquestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameModel(
            old_name='ProjectQuestion',
            new_name='ProjectAnswer',
        ),
        migrations.RenameModel(
            old_name='RoleQuestion',
            new_name='RoleAnswer',
        ),
        migrations.CreateModel(
            name='SkillAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveIntegerField(default=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamverwaltung_main.poll')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teamverwaltung_main.skill')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='teamverwaltung_main.student')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamverwaltung_main.project')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teamverwaltung_main.role')),
            ],
        ),
    ]
