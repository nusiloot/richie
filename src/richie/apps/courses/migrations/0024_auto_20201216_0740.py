# Generated by Django 3.1.4 on 2020-12-16 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0023_auto_20201202_1146"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blogpost",
            options={
                "ordering": ["-pk"],
                "verbose_name": "blog post",
                "verbose_name_plural": "blog posts",
            },
        ),
        migrations.AlterModelOptions(
            name="blogpostpluginmodel",
            options={
                "verbose_name": "blog post plugin",
                "verbose_name_plural": "blog post plugins",
            },
        ),
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ["-pk"],
                "verbose_name": "category",
                "verbose_name_plural": "categories",
            },
        ),
        migrations.AlterModelOptions(
            name="categorypluginmodel",
            options={
                "verbose_name": "category plugin",
                "verbose_name_plural": "category plugins",
            },
        ),
        migrations.AlterModelOptions(
            name="course",
            options={"verbose_name": "course", "verbose_name_plural": "courses"},
        ),
        migrations.AlterModelOptions(
            name="coursepluginmodel",
            options={
                "verbose_name": "course plugin",
                "verbose_name_plural": "course plugins",
            },
        ),
        migrations.AlterModelOptions(
            name="courserun",
            options={
                "verbose_name": "course run",
                "verbose_name_plural": "course runs",
            },
        ),
        migrations.AlterModelOptions(
            name="courseruntranslation",
            options={
                "verbose_name": "Course run translation",
                "verbose_name_plural": "Course run translations",
            },
        ),
        migrations.AlterModelOptions(
            name="licence",
            options={"verbose_name": "licence", "verbose_name_plural": "licences"},
        ),
        migrations.AlterModelOptions(
            name="licencepluginmodel",
            options={
                "verbose_name": "licence plugin",
                "verbose_name_plural": "licence plugins",
            },
        ),
        migrations.AlterModelOptions(
            name="licencetranslation",
            options={
                "verbose_name": "Licence translation",
                "verbose_name_plural": "licence translations",
            },
        ),
        migrations.AlterModelOptions(
            name="organization",
            options={
                "ordering": ["-pk"],
                "verbose_name": "organization",
                "verbose_name_plural": "organizations",
            },
        ),
        migrations.AlterModelOptions(
            name="organizationpluginmodel",
            options={
                "verbose_name": "organization plugin",
                "verbose_name_plural": "organization plugins",
            },
        ),
        migrations.AlterModelOptions(
            name="organizationsbycategorypluginmodel",
            options={
                "verbose_name": "organizations by category plugin",
                "verbose_name_plural": "organizations by category plugins",
            },
        ),
        migrations.AlterModelOptions(
            name="pagerole",
            options={"verbose_name": "page role", "verbose_name_plural": "page roles"},
        ),
        migrations.AlterModelOptions(
            name="person",
            options={"verbose_name": "person", "verbose_name_plural": "persons"},
        ),
        migrations.AlterModelOptions(
            name="personpluginmodel",
            options={
                "verbose_name": "person plugin",
                "verbose_name_plural": "person plugins",
            },
        ),
        migrations.AlterModelOptions(
            name="program",
            options={
                "ordering": ["-pk"],
                "verbose_name": "program",
                "verbose_name_plural": "programs",
            },
        ),
        migrations.AlterModelOptions(
            name="programpluginmodel",
            options={
                "verbose_name": "program plugin",
                "verbose_name_plural": "program plugins",
            },
        ),
        migrations.AddField(
            model_name="course",
            name="code",
            field=models.CharField(
                blank=True,
                help_text="Unique course code",
                max_length=100,
                null=True,
                verbose_name="code",
            ),
        ),
    ]
