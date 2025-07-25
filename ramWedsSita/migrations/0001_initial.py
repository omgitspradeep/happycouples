# Generated by Django 3.1 on 2021-04-25 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InviteeRS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('Mr. ', 'Male'), ('Ms. ', 'Female')], max_length=6)),
                ('address', models.CharField(max_length=50)),
                ('inviteStatus', models.CharField(choices=[('Wedding', 'Wedding'), ('Reception', 'Reception')], default='W', max_length=20)),
                ('inviteeMessage', models.TextField(blank=True, default='You are cordially invited to the beautiful ceremony of my wedding. Your blessings matter the most to us!', max_length=500)),
                ('siteVisited', models.BooleanField(default=False)),
                ('secretCode', models.CharField(blank=True, editable=False, max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WisherRS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wishes', models.CharField(max_length=500)),
                ('posted', models.DateTimeField(auto_now=True)),
                ('invitee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ramWedsSita.inviteers')),
            ],
        ),
    ]
