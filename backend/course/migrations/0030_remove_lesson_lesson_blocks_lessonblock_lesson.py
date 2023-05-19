# Generated by Django 4.1.5 on 2023-04-12 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0029_remove_lesson_lesson_blocks_lesson_lesson_blocks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='lesson_blocks',
        ),
        migrations.AddField(
            model_name='lessonblock',
            name='lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lesson_blocks', to='course.lesson'),
        ),
    ]