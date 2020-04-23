import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('ipam', '0019_virtualization'), ('ipam', '0020_ipaddress_add_role_carp')]

    dependencies = [
        ('ipam', '0018_remove_service_uniqueness_constraint'),
        ('virtualization', '0001_virtualization'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['protocol', 'port']},
        ),
        migrations.AddField(
            model_name='service',
            name='virtual_machine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='virtualization.VirtualMachine'),
        ),
        migrations.AlterField(
            model_name='service',
            name='device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='dcim.Device', verbose_name='device'),
        ),
        migrations.AlterField(
            model_name='ipaddress',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(10, 'Loopback'), (20, 'Secondary'), (30, 'Anycast'), (40, 'VIP'), (41, 'VRRP'), (42, 'HSRP'), (43, 'GLBP'), (44, 'CARP')], help_text='The functional role of this IP', null=True, verbose_name='Role'),
        ),
    ]
