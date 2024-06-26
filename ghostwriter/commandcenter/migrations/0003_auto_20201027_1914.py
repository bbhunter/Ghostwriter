# Generated by Django 3.0.10 on 2020-10-27 19:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reporting", "0018_auto_20201027_1914"),
        ("commandcenter", "0002_auto_20201009_1918"),
    ]

    operations = [
        migrations.AddField(
            model_name="reportconfiguration",
            name="default_docx_template",
            field=models.ForeignKey(
                help_text="Select a default Word template",
                limit_choices_to={"doc_type__doc_type__iexact": "docx"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="reportconfiguration_docx_set",
                to="reporting.ReportTemplate",
            ),
        ),
        migrations.AddField(
            model_name="reportconfiguration",
            name="default_pptx_template",
            field=models.ForeignKey(
                help_text="Select a default Word template",
                limit_choices_to={"doc_type__doc_type__iexact": "pptx"},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="reportconfiguration_pptx_set",
                to="reporting.ReportTemplate",
            ),
        ),
    ]
