# Generated by Django 4.2.4 on 2023-11-22 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SavingProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField()),
                ('dcls_month', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('join_deny', models.IntegerField()),
                ('join_way', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('bank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saving_products', to='finlife.bank')),
            ],
        ),
        migrations.CreateModel(
            name='SavingOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField()),
                ('dcls_month', models.TextField()),
                ('intr_rate', models.FloatField()),
                ('intr_rate2', models.FloatField()),
                ('save_trm', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saving_options', to='finlife.savingproducts')),
            ],
        ),
        migrations.CreateModel(
            name='DepositProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField()),
                ('dcls_month', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('join_deny', models.IntegerField()),
                ('join_way', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('bank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deposit_products', to='finlife.bank')),
            ],
        ),
        migrations.CreateModel(
            name='DepositOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField()),
                ('dcls_month', models.TextField()),
                ('intr_rate', models.FloatField()),
                ('intr_rate2', models.FloatField()),
                ('save_trm', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposit_options', to='finlife.depositproducts')),
            ],
        ),
    ]
