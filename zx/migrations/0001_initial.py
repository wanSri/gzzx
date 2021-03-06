# Generated by Django 2.2.6 on 2020-01-15 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eapi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('netEquName', models.CharField(max_length=50, null=True)),
                ('lineNo', models.CharField(max_length=100, null=True)),
                ('port', models.CharField(max_length=50, null=True)),
                ('bandwidth', models.CharField(max_length=10, null=True)),
                ('operator', models.CharField(max_length=10, null=True)),
                ('lineType', models.CharField(max_length=10, null=True)),
                ('ipAddr', models.CharField(max_length=50, null=True)),
                ('ACL', models.CharField(max_length=50, null=True)),
                ('department', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('router', models.CharField(max_length=40)),
                ('portType', models.CharField(max_length=20, null=True)),
                ('port', models.CharField(max_length=20)),
                ('acl', models.CharField(max_length=255)),
                ('des', models.CharField(max_length=60, null=True)),
                ('ip', models.CharField(max_length=256, null=True)),
                ('bandwidth', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=50)),
                ('netEName', models.CharField(help_text='网络设备名称', max_length=50, null=True)),
                ('ip', models.CharField(max_length=50, null=True)),
                ('resouceNo', models.CharField(max_length=50, null=True)),
                ('serialNum', models.CharField(max_length=50, null=True)),
                ('brand', models.CharField(max_length=50, null=True)),
                ('type', models.CharField(max_length=50, null=True)),
                ('subclass', models.CharField(max_length=50, null=True)),
                ('estabLevel', models.CharField(max_length=20, null=True)),
                ('netArea', models.CharField(max_length=50, null=True)),
                ('functionType', models.CharField(max_length=20, null=True)),
                ('quipWwn', models.CharField(max_length=50, null=True)),
                ('equipStatus', models.CharField(max_length=20, null=True)),
                ('physicalLocation', models.CharField(max_length=50, null=True)),
                ('powerSupplyMode', models.CharField(max_length=50, null=True)),
                ('aPowerId', models.CharField(max_length=50, null=True)),
                ('bPowerId', models.CharField(max_length=50, null=True)),
                ('otherIpAddr', models.CharField(max_length=2048, null=True)),
                ('macAddr', models.CharField(max_length=50, null=True)),
                ('equipPurpose', models.CharField(max_length=50, null=True)),
                ('NumOfPowerModules', models.CharField(max_length=10, null=True)),
                ('osVersion', models.CharField(max_length=100, null=True)),
                ('purchaseTime', models.CharField(max_length=20, null=True)),
                ('installTime', models.CharField(max_length=20, null=True)),
                ('runDay', models.CharField(max_length=10, null=True)),
                ('equipBackups', models.CharField(max_length=100, null=True)),
                ('createTime', models.CharField(max_length=20, null=True)),
                ('lastUpdateTime', models.CharField(max_length=20, null=True)),
                ('updateByName', models.CharField(max_length=10, null=True)),
                ('bmc', models.CharField(max_length=50, null=True)),
                ('ciOrganization', models.CharField(max_length=50, null=True)),
                ('ciDepartment', models.CharField(max_length=50, null=True)),
                ('maintainSource', models.CharField(max_length=50, null=True)),
                ('remark', models.CharField(max_length=100, null=True)),
                ('configurationItemStatus', models.CharField(max_length=10, null=True)),
                ('belongToGroup', models.CharField(max_length=20, null=True)),
                ('label', models.CharField(max_length=50, null=True)),
                ('commandSet', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LineOfBusinessOutlets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('netName', models.CharField(max_length=50, null=True)),
                ('routerName', models.CharField(max_length=20, null=True)),
                ('equipmentMode', models.CharField(max_length=50, null=True)),
                ('managAddr', models.CharField(max_length=50, null=True)),
                ('port', models.CharField(max_length=50, null=True)),
                ('netLineNo', models.CharField(max_length=50, null=True)),
                ('brandWidth', models.CharField(max_length=10, null=True)),
                ('bIP', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZhuanLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci', models.CharField(help_text='CI', max_length=255)),
                ('lineType', models.CharField(help_text='专线类型', max_length=50, null=True)),
                ('lineClassfity', models.CharField(help_text='线路分类', max_length=50, null=True)),
                ('lineNum', models.CharField(help_text='专线号', max_length=255, null=True)),
                ('linefunction', models.CharField(help_text='专线用途', max_length=255, null=True)),
                ('rentFee', models.CharField(help_text='专线月租', max_length=10, null=True)),
                ('startTime', models.CharField(help_text='专线开通时间', max_length=50, null=True)),
                ('ToBType', models.CharField(help_text='B端机构类型', max_length=50, null=True)),
                ('aOrganisation', models.CharField(help_text='A端机构', max_length=50, null=True)),
                ('aEquireID', models.CharField(help_text='a端接入设备ID', max_length=50, null=True)),
                ('aPortType', models.CharField(help_text='A端接入端口类型', max_length=50, null=True)),
                ('aPortID', models.CharField(help_text='A端接入端口ID', max_length=50, null=True)),
                ('aToPort', models.CharField(help_text='A端接入端口号', max_length=50, null=True)),
                ('bOrganisation', models.CharField(help_text='B端机构', max_length=50, null=True)),
                ('bEquireID', models.CharField(help_text='B端接入设备ID', max_length=50, null=True)),
                ('bEquireName', models.CharField(help_text='B端接入设备名称', max_length=50, null=True)),
                ('bPortID', models.CharField(help_text='B端接入端口ID', max_length=50, null=True)),
                ('bPortType', models.CharField(help_text='B端接入端口类型', max_length=50, null=True)),
                ('bToPort', models.CharField(help_text='B端接入端口号', max_length=50, null=True)),
                ('lineProperty', models.CharField(help_text='专线属性', max_length=10, null=True)),
                ('bandwidth', models.CharField(help_text='带宽', max_length=10, null=True)),
                ('opptNetAddr', models.CharField(help_text='对端公网地址', max_length=50, null=True)),
                ('opptMonitorAddr', models.CharField(help_text='对端隧道监控地址', max_length=50, null=True)),
                ('lingQuityDepart', models.CharField(help_text='专线产权单位', max_length=255, null=True)),
                ('aperator', models.CharField(help_text='运营商', max_length=10, null=True)),
                ('subjectType', models.CharField(help_text='科目类型', max_length=50, null=True)),
                ('backupsLine', models.CharField(help_text='备份线路', max_length=50, null=True)),
                ('ciResponForOrgan', models.CharField(help_text='CI负责机构', max_length=50, null=True)),
                ('ciResponForDepart', models.CharField(help_text='CI负责部门', max_length=50, null=True)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True, null=True)),
                ('updateByPerson', models.CharField(help_text='最后修改人', max_length=10, null=True)),
                ('maintainSource', models.CharField(help_text='维护来源', max_length=50, null=True)),
                ('configurationStatus', models.CharField(help_text='配置项状态', max_length=10, null=True)),
                ('remark', models.CharField(help_text='备注', max_length=255, null=True)),
            ],
        ),
    ]
