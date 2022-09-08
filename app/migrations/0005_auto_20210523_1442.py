# Generated by Django 3.2.3 on 2021-05-23 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210522_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='request_specialty',
            field=models.CharField(choices=[('1', 'Neurology - Dr. Kenneth Chin Wei Yow'), ('2', 'Cardiology - Dr. Aw Zhi Wei'), ('3', 'Psychiatry - Dr. Leong Chee Kei'), ('4', 'Radiology - Dr. Kelwin Chew'), ('5', 'Dermatology - Dr. Tan Zhi Jun')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='patient',
            name='doctor',
            field=models.CharField(choices=[('1', 'Neurology - Dr. Kenneth Chin Wei Yow'), ('2', 'Cardiology - Dr. Aw Zhi Wei'), ('3', 'Psychiatry - Dr. Leong Chee Kei'), ('4', 'Radiology - Dr. Kelwin Chew'), ('5', 'Dermatology - Dr. Tan Zhi Jun')], default='1', max_length=1),
        ),
    ]