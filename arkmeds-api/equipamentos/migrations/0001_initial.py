# Generated by Django 3.1.2 on 2020-11-01 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.PositiveIntegerField(editable=False, primary_key=True, serialize=False)),
                ('tipo', models.PositiveIntegerField(null=True)),
                ('nome', models.CharField(max_length=100, null=True)),
                ('nome_fantasia', models.CharField(max_length=100, null=True)),
                ('superior', models.CharField(max_length=100, null=True)),
                ('cnpj', models.CharField(max_length=20, null=True)),
                ('observacoes', models.TextField(max_length=500, null=True)),
                ('contato', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('telefone1', models.CharField(max_length=20, null=True)),
                ('ramal1', models.CharField(max_length=20, null=True)),
                ('telefone2', models.CharField(max_length=20, null=True)),
                ('ramal2', models.CharField(max_length=20, null=True)),
                ('fax', models.CharField(max_length=20, null=True)),
                ('cep', models.CharField(max_length=12, null=True)),
                ('rua', models.CharField(max_length=100, null=True)),
                ('numero', models.IntegerField(null=True)),
                ('bairro', models.CharField(max_length=100, null=True)),
                ('cidade', models.CharField(max_length=100, null=True)),
                ('estado', models.CharField(max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proprietario',
            fields=[
                ('id', models.PositiveIntegerField(editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('apelido', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ResponsavelTecnico',
            fields=[
                ('id', models.PositiveIntegerField(editable=False, primary_key=True, serialize=False)),
                ('has_avatar', models.BooleanField(default=False)),
                ('nome', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('has_resp_tecnico', models.BooleanField(default=False)),
                ('avatar', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEquipamento',
            fields=[
                ('id', models.PositiveIntegerField(editable=False, primary_key=True, serialize=False)),
                ('descricao', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.PositiveIntegerField(editable=False, primary_key=True, serialize=False)),
                ('fabricante', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('patrimonio', models.CharField(max_length=100)),
                ('numero_serie', models.CharField(max_length=100)),
                ('identificacao', models.CharField(max_length=100)),
                ('qr_code', models.IntegerField()),
                ('proprietario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='equipamentos.proprietario')),
                ('tipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='equipamentos.tipoequipamento')),
            ],
        ),
        migrations.CreateModel(
            name='ChamadoEquipamento',
            fields=[
                ('id', models.PositiveIntegerField(editable=False, primary_key=True, serialize=False)),
                ('chamados', models.IntegerField(null=True)),
                ('cor_prioridade', models.CharField(max_length=100, null=True)),
                ('prioridade', models.PositiveSmallIntegerField(null=True)),
                ('get_prioridade', models.CharField(max_length=100, null=True)),
                ('numero', models.IntegerField()),
                ('get_solicitante', models.CharField(max_length=100, null=True)),
                ('get_equipamento_servico', models.CharField(max_length=100, null=True)),
                ('get_criticidde', models.CharField(max_length=100)),
                ('tempo', models.JSONField(null=True)),
                ('tempo_fechamento', models.JSONField(null=True)),
                ('responsavel_str', models.CharField(max_length=100, null=True)),
                ('problema_str', models.CharField(max_length=100, null=True)),
                ('chamado_arquivado', models.BooleanField(default=False)),
                ('estado', models.PositiveIntegerField(editable=False, null=True)),
                ('equipamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='equipamentos.equipamento')),
                ('get_resp_tecnico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='equipamentos.responsaveltecnico')),
            ],
        ),
    ]
