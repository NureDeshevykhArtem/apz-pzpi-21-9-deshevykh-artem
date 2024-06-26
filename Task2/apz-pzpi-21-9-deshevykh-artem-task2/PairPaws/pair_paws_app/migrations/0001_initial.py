# Generated by Django 4.2.7 on 2024-05-01 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=50)),
                ('breed', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('pets', models.ManyToManyField(related_name='owners', to='pair_paws_app.pet')),
            ],
        ),
        migrations.CreateModel(
            name='PetMateRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=10)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pair_paws_app.pet')),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requested_requests', to='pair_paws_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='PetMateMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted_at', models.DateTimeField(auto_now_add=True)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matched_partners', to='pair_paws_app.user')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pair_paws_app.petmaterequest')),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pair_paws_app.user'),
        ),
    ]
