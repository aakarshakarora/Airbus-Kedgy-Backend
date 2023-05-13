# Generated by Django 4.1.1 on 2023-05-13 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_store', '0008_alter_assembly_edate_alter_assembly_sdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assembly',
            name='approved_by',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assembly_approvals', to='data_store.user'),
        ),
        migrations.AlterField(
            model_name='fabrication',
            name='approved_by',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fabrication_approvals', to='data_store.user'),
        ),
        migrations.AlterField(
            model_name='subassembly',
            name='approved_by',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subassembly_approvals', to='data_store.user'),
        ),
    ]
