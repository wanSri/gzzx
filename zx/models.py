from django.db import models


# Create your models here.


# 配置文件
class Equ(models.Model):
    router = models.CharField(max_length=40)
    portType = models.CharField(max_length=20, null=True)
    port = models.CharField(max_length=20)
    acl = models.CharField(max_length=255)
    des = models.CharField(max_length=60, null=True)
    ip = models.CharField(max_length=256, null=True)
    bandwidth = models.CharField(null=True, max_length=20)


# 专线表
class ZhuanLine(models.Model):
    ci = models.CharField(max_length=255, help_text="CI")
    lineType = models.CharField(max_length=50, help_text="专线类型", null=True)
    lineClassfity = models.CharField(max_length=50, help_text="线路分类", null=True)
    lineNum = models.CharField(max_length=255, help_text="专线号", null=True)
    linefunction = models.CharField(max_length=255, help_text="专线用途", null=True)
    rentFee = models.CharField(max_length=10, help_text="专线月租", null=True)
    startTime = models.CharField(max_length=50, help_text="专线开通时间", null=True)
    ToBType = models.CharField(max_length=50, help_text="B端机构类型", null=True)
    aOrganisation = models.CharField(max_length=50, help_text="A端机构", null=True)
    aEquireID = models.CharField(max_length=50, help_text="a端接入设备ID", null=True)
    aPortType = models.CharField(max_length=50, help_text="A端接入端口类型", null=True)
    aPortID = models.CharField(max_length=50, help_text="A端接入端口ID", null=True)
    aToPort = models.CharField(max_length=50, help_text="A端接入端口号", null=True)
    bOrganisation = models.CharField(max_length=50, help_text="B端机构", null=True)
    bEquireID = models.CharField(max_length=50, help_text="B端接入设备ID", null=True)
    bEquireName = models.CharField(max_length=50, help_text="B端接入设备名称", null=True)
    bPortID = models.CharField(max_length=50, help_text="B端接入端口ID", null=True)
    bPortType = models.CharField(max_length=50, help_text="B端接入端口类型", null=True)
    bToPort = models.CharField(max_length=50, help_text="B端接入端口号", null=True)
    lineProperty = models.CharField(max_length=10, help_text="专线属性", null=True)
    bandwidth = models.CharField(max_length=10, help_text="带宽", null=True)
    opptNetAddr = models.CharField(max_length=50, help_text="对端公网地址", null=True)
    opptMonitorAddr = models.CharField(max_length=50, help_text="对端隧道监控地址", null=True)
    lingQuityDepart = models.CharField(max_length=255, help_text="专线产权单位", null=True)
    aperator = models.CharField(max_length=10, help_text="运营商", null=True)
    subjectType = models.CharField(max_length=50, help_text="科目类型", null=True)
    backupsLine = models.CharField(max_length=50, help_text="备份线路", null=True)
    ciResponForOrgan = models.CharField(max_length=50, help_text="CI负责机构", null=True)
    ciResponForDepart = models.CharField(max_length=50, help_text="CI负责部门", null=True)
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True, null=True)
    updateByPerson = models.CharField(max_length=10, null=True, help_text="最后修改人")
    maintainSource = models.CharField(max_length=50, null=True, help_text="维护来源")
    configurationStatus = models.CharField(max_length=10, null=True, help_text="配置项状态")
    remark = models.CharField(max_length=255, null=True, help_text="备注")


# 设备表
class Equipment(models.Model):
    eid = models.CharField(max_length=50)
    netEName = models.CharField(max_length=50, help_text="网络设备名称", null=True)
    ip = models.CharField(max_length=50, null=True)
    resouceNo = models.CharField(max_length=50, null=True)
    serialNum = models.CharField(max_length=50, null=True)
    brand = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    subclass = models.CharField(max_length=50, null=True)
    estabLevel = models.CharField(max_length=20, null=True)
    netArea = models.CharField(max_length=50, null=True)
    functionType = models.CharField(max_length=20, null=True)
    quipWwn = models.CharField(max_length=50, null=True)
    equipStatus = models.CharField(max_length=20, null=True)
    physicalLocation = models.CharField(max_length=50, null=True)
    powerSupplyMode = models.CharField(max_length=50, null=True)
    aPowerId = models.CharField(max_length=50, null=True)
    bPowerId = models.CharField(max_length=50, null=True)
    otherIpAddr = models.CharField(max_length=2048, null=True)
    macAddr = models.CharField(max_length=50, null=True)
    equipPurpose = models.CharField(max_length=50, null=True)
    NumOfPowerModules = models.CharField(max_length=10, null=True)
    osVersion = models.CharField(max_length=100, null=True)
    purchaseTime = models.CharField(max_length=20, null=True)
    installTime = models.CharField(max_length=20, null=True)
    runDay = models.CharField(max_length=10, null=True)
    equipBackups = models.CharField(max_length=100, null=True)
    createTime = models.CharField(max_length=20, null=True)
    lastUpdateTime = models.CharField(max_length=20, null=True)
    updateByName = models.CharField(max_length=10, null=True)
    bmc = models.CharField(max_length=50, null=True)
    ciOrganization = models.CharField(max_length=50, null=True)
    ciDepartment = models.CharField(max_length=50, null=True)
    maintainSource = models.CharField(max_length=50, null=True)
    remark = models.CharField(max_length=100, null=True)
    configurationItemStatus = models.CharField(max_length=10, null=True)
    belongToGroup = models.CharField(max_length=20, null=True)
    label = models.CharField(max_length=50, null=True)
    commandSet = models.CharField(max_length=255, null=True)


# 外联接入端口表
class Eapi(models.Model):
    netEquName = models.CharField(max_length=50, null=True)
    lineNo = models.CharField(max_length=100, null=True)
    port = models.CharField(max_length=50, null=True)
    bandwidth = models.CharField(max_length=10, null=True)
    operator = models.CharField(max_length=10, null=True)
    lineType = models.CharField(max_length=10, null=True)
    ipAddr = models.CharField(max_length=50, null=True)
    ACL = models.CharField(max_length=50, null=True)
    department = models.CharField(max_length=100, null=True)


# 营业部网点线路
class LineOfBusinessOutlets(models.Model):
    netName = models.CharField(max_length=50, null=True)
    routerName = models.CharField(max_length=20, null=True)
    equipmentMode = models.CharField(max_length=50, null=True)
    managAddr = models.CharField(max_length=50, null=True)
    port = models.CharField(max_length=50, null=True)
    netLineNo = models.CharField(max_length=50, null=True)
    brandWidth = models.CharField(max_length=10, null=True)
    bIP = models.CharField(max_length=50, null=True)


# 解析文件记录表
class EquRecode(models.Model):
    router = models.CharField(max_length=40)
