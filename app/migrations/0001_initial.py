# Generated by Django 2.1.3 on 2019-02-09 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract_BL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractname', models.CharField(max_length=50)),
                ('contract_id', models.CharField(max_length=20)),
                ('sha256', models.CharField(max_length=100)),
                ('filename', models.CharField(max_length=100)),
                ('share1', models.CharField(max_length=30)),
                ('share2', models.CharField(max_length=30)),
                ('share3', models.CharField(max_length=30)),
                ('status1', models.CharField(max_length=20)),
                ('status2', models.CharField(max_length=20)),
                ('status3', models.CharField(max_length=20)),
                ('finaldestination', models.CharField(max_length=30)),
                ('vessel', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Contract_CI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractname', models.CharField(max_length=50)),
                ('contract_id', models.CharField(max_length=20)),
                ('sha256', models.CharField(max_length=100)),
                ('filename', models.CharField(max_length=100)),
                ('share1', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Contract_DO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractname', models.CharField(max_length=50)),
                ('contract_id', models.CharField(max_length=20)),
                ('sha256', models.CharField(max_length=100)),
                ('filename', models.CharField(max_length=100)),
                ('share1', models.CharField(max_length=30)),
                ('share3', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Contract_LC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractname', models.CharField(max_length=50)),
                ('contract_id', models.CharField(max_length=20)),
                ('sha256', models.CharField(max_length=100)),
                ('filename', models.CharField(max_length=100)),
                ('share1', models.CharField(max_length=30)),
                ('share2', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Contract_LCR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractname', models.CharField(max_length=50)),
                ('contract_id', models.CharField(max_length=20)),
                ('sha256', models.CharField(max_length=100)),
                ('filename', models.CharField(max_length=100)),
                ('share3', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=20)),
                ('advisingbank', models.CharField(max_length=30)),
                ('applicant', models.CharField(max_length=30)),
                ('beneficiary', models.CharField(max_length=30)),
                ('amount', models.CharField(max_length=20)),
                ('particalshipment', models.CharField(max_length=20)),
                ('transshipment', models.CharField(max_length=20)),
                ('loding', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Contract_OS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractname', models.CharField(max_length=50)),
                ('sha256', models.CharField(max_length=100)),
                ('filename', models.CharField(max_length=100)),
                ('share1', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=20)),
                ('item1', models.CharField(max_length=10)),
                ('item2', models.CharField(max_length=10, null=True)),
                ('item3', models.CharField(max_length=10, null=True)),
                ('item4', models.CharField(max_length=10, null=True)),
                ('item5', models.CharField(max_length=10, null=True)),
                ('description1', models.CharField(max_length=30)),
                ('description2', models.CharField(max_length=30, null=True)),
                ('description3', models.CharField(max_length=30, null=True)),
                ('description4', models.CharField(max_length=30, null=True)),
                ('description5', models.CharField(max_length=30, null=True)),
                ('quantity1', models.CharField(max_length=20)),
                ('quantity2', models.CharField(max_length=20, null=True)),
                ('quantity3', models.CharField(max_length=20, null=True)),
                ('quantity4', models.CharField(max_length=20, null=True)),
                ('quantity5', models.CharField(max_length=20, null=True)),
                ('price1', models.CharField(max_length=20)),
                ('price2', models.CharField(max_length=20, null=True)),
                ('price3', models.CharField(max_length=20, null=True)),
                ('price4', models.CharField(max_length=20, null=True)),
                ('price5', models.CharField(max_length=20, null=True)),
                ('amount1', models.CharField(max_length=20)),
                ('amount2', models.CharField(max_length=20, null=True)),
                ('amount3', models.CharField(max_length=20, null=True)),
                ('amount4', models.CharField(max_length=20, null=True)),
                ('amount5', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contract_SR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractname', models.CharField(max_length=50)),
                ('contract_id', models.CharField(max_length=20)),
                ('sha256', models.CharField(max_length=100)),
                ('filename', models.CharField(max_length=100)),
                ('share4', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=20)),
                ('consignee', models.CharField(max_length=30)),
                ('notify', models.CharField(max_length=30)),
                ('lport', models.CharField(max_length=30)),
                ('dport', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('user_role', models.CharField(max_length=10)),
                ('user_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('businessnum', models.CharField(max_length=30)),
                ('tbc', models.CharField(max_length=30)),
                ('otpkey', models.CharField(max_length=20)),
                ('user_pw', models.CharField(max_length=100)),
                ('c_date', models.DateTimeField(null=True)),
                ('tel', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=5000)),
                ('c_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_id', models.CharField(max_length=20)),
                ('OS_hash', models.CharField(max_length=100)),
                ('SR_hash', models.CharField(max_length=100)),
                ('CI_hash', models.CharField(max_length=100)),
                ('LCR_hash', models.CharField(max_length=100)),
                ('LC_hash', models.CharField(max_length=100)),
                ('BL_hash', models.CharField(max_length=100)),
                ('DO_hash', models.CharField(max_length=100)),
                ('user1', models.CharField(max_length=30)),
                ('user2', models.CharField(max_length=30)),
                ('user3', models.CharField(max_length=30)),
                ('user4', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='contract_sr',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Member'),
        ),
        migrations.AddField(
            model_name='contract_os',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Member'),
        ),
        migrations.AddField(
            model_name='contract_lcr',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Member'),
        ),
        migrations.AddField(
            model_name='contract_lc',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Member'),
        ),
        migrations.AddField(
            model_name='contract_do',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Member'),
        ),
        migrations.AddField(
            model_name='contract_ci',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Member'),
        ),
        migrations.AddField(
            model_name='contract_bl',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Member'),
        ),
    ]