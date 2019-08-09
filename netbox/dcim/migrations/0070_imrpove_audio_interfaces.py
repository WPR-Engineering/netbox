
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0069_audio_interface_to_interface'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interface',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[['Virtual interfaces', [[0, 'Virtual'], [200, 'Link Aggregation Group (LAG)']]], ['Ethernet (fixed)', [[800, '100BASE-TX (10/100ME)'], [1000, '1000BASE-T (1GE)'], [1150, '10GBASE-T (10GE)'], [1170, '10GBASE-CX4 (10GE)']]], ['Ethernet (modular)', [[1050, 'GBIC (1GE)'], [1100, 'SFP (1GE)'], [1200, 'SFP+ (10GE)'], [1300, 'XFP (10GE)'], [1310, 'XENPAK (10GE)'], [1320, 'X2 (10GE)'], [1350, 'SFP28 (25GE)'], [1400, 'QSFP+ (40GE)'], [1500, 'CFP (100GE)'], [1510, 'CFP2 (100GE)'], [1520, 'CFP4 (100GE)'], [1550, 'Cisco CPAK (100GE)'], [1600, 'QSFP28 (100GE)']]], ['Wireless', [[2600, 'IEEE 802.11a'], [2610, 'IEEE 802.11b/g'], [2620, 'IEEE 802.11n'], [2630, 'IEEE 802.11ac'], [2640, 'IEEE 802.11ad']]], ['FibreChannel', [[3010, 'SFP (1GFC)'], [3020, 'SFP (2GFC)'], [3040, 'SFP (4GFC)'], [3080, 'SFP+ (8GFC)'], [3160, 'SFP+ (16GFC)']]], ['Serial', [[4000, 'T1 (1.544 Mbps)'], [4010, 'E1 (2.048 Mbps)'], [4040, 'T3 (45 Mbps)'], [4050, 'E3 (34 Mbps)']]], ['Stacking', [[5000, 'Cisco StackWise'], [5050, 'Cisco StackWise Plus'], [5100, 'Cisco FlexStack'], [5150, 'Cisco FlexStack Plus'], [5200, 'Juniper VCP']]], ['Aduio', [[6000, 'Analog Audio'], [6100, 'AES/EBU'], [6200, 'Microphone']]], ['GPIO', [[6500, 'GPIO Input'], [6600, 'GPIO Output'], [6700, 'GPIO Virtual']]], ['Other', [[32767, 'Other']]]], default=1200),
        ),
        migrations.AlterField(
            model_name='interfacetemplate',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[['Virtual interfaces', [[0, 'Virtual'], [200, 'Link Aggregation Group (LAG)']]], ['Ethernet (fixed)', [[800, '100BASE-TX (10/100ME)'], [1000, '1000BASE-T (1GE)'], [1150, '10GBASE-T (10GE)'], [1170, '10GBASE-CX4 (10GE)']]], ['Ethernet (modular)', [[1050, 'GBIC (1GE)'], [1100, 'SFP (1GE)'], [1200, 'SFP+ (10GE)'], [1300, 'XFP (10GE)'], [1310, 'XENPAK (10GE)'], [1320, 'X2 (10GE)'], [1350, 'SFP28 (25GE)'], [1400, 'QSFP+ (40GE)'], [1500, 'CFP (100GE)'], [1510, 'CFP2 (100GE)'], [1520, 'CFP4 (100GE)'], [1550, 'Cisco CPAK (100GE)'], [1600, 'QSFP28 (100GE)']]], ['Wireless', [[2600, 'IEEE 802.11a'], [2610, 'IEEE 802.11b/g'], [2620, 'IEEE 802.11n'], [2630, 'IEEE 802.11ac'], [2640, 'IEEE 802.11ad']]], ['FibreChannel', [[3010, 'SFP (1GFC)'], [3020, 'SFP (2GFC)'], [3040, 'SFP (4GFC)'], [3080, 'SFP+ (8GFC)'], [3160, 'SFP+ (16GFC)']]], ['Serial', [[4000, 'T1 (1.544 Mbps)'], [4010, 'E1 (2.048 Mbps)'], [4040, 'T3 (45 Mbps)'], [4050, 'E3 (34 Mbps)']]], ['Stacking', [[5000, 'Cisco StackWise'], [5050, 'Cisco StackWise Plus'], [5100, 'Cisco FlexStack'], [5150, 'Cisco FlexStack Plus'], [5200, 'Juniper VCP']]], ['Aduio', [[6000, 'Analog Audio'], [6100, 'AES/EBU'], [6200, 'Microphone']]], ['GPIO', [[6500, 'GPIO Input'], [6600, 'GPIO Output'], [6700, 'GPIO Virtual'], [6800, 'GPIO']]], ['Other', [[32767, 'Other']]]], default=1200),
        ),
    ]
