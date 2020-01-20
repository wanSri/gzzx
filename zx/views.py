import xlrd
from rest_framework import viewsets
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from utils import constants
from utils.parseUtil import parse as parse_util
from django.db import transaction
from rest_framework.pagination import PageNumberPagination

from controller import zxcontroller
from serializers import zxserializer

# Create your views here.

# 基于函数的视图。通过添加装饰器的方式
from zx.models import Equ, EquRecode, ZhuanLine, Equipment, Eapi, LineOfBusinessOutlets


@api_view(['POST'])
@parser_classes([MultiPartParser])
@transaction.atomic
def uploadConfigFile(request):
    file = request.FILES.get('file')
    if file.name:
        Equ.objects.filter(router=file.name).delete()
        str2 = file.read().decode()
        parse_template = constants.PARSE_TEMPLATE
        new_list, results = parse_util(str2, parse_template)
        bulk_list = []
        i = 0
        for e in results:
            equ = Equ()
            for n in new_list:
                setattr(equ, n, e[new_list.index(n)])
            setattr(equ, 'router', file.name)
            bulk_list.append(equ)
            i += 1
            if i == 100:
                Equ.objects.bulk_create(bulk_list)
                bulk_list = []
                i = 0
        if bulk_list is not None:
            Equ.objects.bulk_create(bulk_list)
        response = {
            "code": 200,
            "data": [],
            "msg": 'success',
        }

        return Response(data={
            "code": 200,
            "data": [],
            "msg": 'success'
        })
    else:
        pass


class EquViewSet(viewsets.ModelViewSet):
    serializer_class = zxserializer.EquSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        params = self.request.query_params
        return zxcontroller.EquController.get_querySet(params)


def save_object(file, table_name):
    data = xlrd.open_workbook(file_contents=file.read())
    table = data.sheets()[0]
    nrows = table.nrows
    allc = table_name._meta.get_fields()
    list1 = list(map(lambda x: x.attname, allc))
    list1.pop(0)
    n = 0
    add_list = []
    for i in range(1, nrows):
        row = table.row_values(i)
        obj = ZhuanLine()
        for j in range(len(list1)):
            setattr(obj, list1[j], row[j])
        add_list.append(obj)
    table_name.objects.bulk_create(add_list)


# 专线
class ZhuanLineListView(APIView):

    def post(self, request, *args, **kwargs):
        file = request.FILES.get("file")
        try:
            save_object(file, ZhuanLine)
        except Exception as e:
            return Response({
                "code": 400,
                "data": [],
                "msg": "导入失败"
            })

        return Response("success")

    def get(self, request):
        queryset = ZhuanLine.objects.all()
        pg = PageNumberPagination()
        zxs = pg.paginate_queryset(queryset=queryset, request=request, view=self)
        ser = zxserializer.ZXSerializer(instance=zxs, many=True)
        return Response(ser.data)


class ZhuanLineDetail(APIView):
    # 注意不加request 报错，get() got multiple values for argument 'pk'
    def get(self, request, pk):
        zl = ZhuanLine.objects.filter(pk=pk).first()
        if zl:
            return Response({
                'code': 200,
                'data': zxserializer.ZXSerializer(instance=zl).data,
                'msg': ''
            })

        return Response({
            'code': 400,
            'data': {},
            'msg': '数据不存在'
        })


class EqupmentListView(APIView):

    def post(self, request, *args, **kwargs):
        file = request.FILES.get("file")
        try:
            save_object(file, Equipment)
        except Exception as e:
            return Response({
                "code": 400,
                "data": [],
                "msg": "导入失败"
            })

        return Response("success")

    def get(self, request):
        queryset = Equipment.objects.all()
        pg = PageNumberPagination()
        equips = pg.paginate_queryset(queryset=queryset, request=request, view=self)
        ser = zxserializer.EquipSerializer(instance=queryset, many=True)
        return Response({
            'code': 200,
            'data': ser.data,
            'msg': 'success'
        })


class EquipDetailView(APIView):
    def get(self, request, pk):
        equip = Equipment.objects.filter(pk=pk).first()
        if equip:
            return Response({
                'code': 200,
                'data': zxserializer.EquipSerializer(instance=equip).data,
                'msg': '',
            })
        return Response({
            'code': 400,
            'data': {},
            'msg': '数据不存在',
        })


# 生成表
@api_view(['GET'])
@transaction.atomic()
def generateTable(request):
    zxs = ZhuanLine.objects.all()
    if zxs is not None:
        for zx in zxs:
            lineClassfity = zx.lineClassfity
            port = zx.aPortType + zx.aToPort
            lineNo = zx.lineNum
            bandwidth = zx.bandwidth
            bOrganisation = zx.bOrganisation
            if lineClassfity == "Extranet":
                aEquireID = zx.aEquireID
                equipments = Equipment.objects.filter(eid=aEquireID)
                if equipments is not None:
                    equipment = equipments[0]
                    netEName = equipment.netEName
                    operator = zx.aperator
                    lineType = zx.lineType
                    equConfig = Equ.objects.filter(router=netEName).filter(port=zx.aToPort)[0]
                    ipAddr = equConfig.ip
                    ACL = equConfig.acl

                eapi = Eapi(netEquName=netEName,
                            lineNo=lineNo,
                            port=port,
                            bandwidth=bandwidth,
                            operator=operator,
                            lineType=lineType,
                            ipAddr=ipAddr,
                            ACL=ACL,
                            department=bOrganisation)
                eapi.save()
            elif lineClassfity == '汇接网':
                netName = bOrganisation
                routerName = zx.bEquireName
                bEquireID = zx.bEquireID
                aEquireID = zx.aEquireID
                equipments = Equipment.objects.filter(eid=bEquireID)
                aeqipment = Equipment.objects.filter(eid=aEquireID)[0]

                if equipments is not None:
                    equipment = equipments[0]
                    equipmentMode = equipment.type
                    managAddr = equipment.ip
                    equConfig = Equ.objects.filter(router=aeqipment.netEName).filter(port=zx.aToPort)[0]
                    bIP = equConfig.ip.split('.')
                    bIP[3] = str(int(bIP[3]) + 1)
                    bIp = '.'.join(bIP)
                lineOfBusinessOutlets = LineOfBusinessOutlets(
                    netName=netName,
                    routerName=routerName,
                    equipmentMode=equipmentMode,
                    managAddr=managAddr,
                    port=aeqipment.netEName + " " + zx.aPortType + zx.aToPort,
                    netLineNo=lineNo,
                    brandWidth=bandwidth,
                    bIP=bIp
                )
                lineOfBusinessOutlets.save()
            else:
                return Response({
                    'code': 400,
                    'data': {},
                    'msg': '失败'
                })
    return Response({
        'code': '200',
        'data': {},
        'msg': 'success'
    })


class EapiListView(APIView):
    def get(self, request):
        queryset = Eapi.objects.all()
        pg = PageNumberPagination()
        eaips = pg.paginate_queryset(queryset=queryset, request=request, view=self)
        ser = zxserializer.EaipSerializer(instance=eaips, many=True)
        return Response({
            'code': 200,
            'data': ser.data,
            'msg': 'success'
        })


class LoboListView(APIView):
    def get(self, request):
        queryset = LineOfBusinessOutlets.objects.all()
        pg = PageNumberPagination()
        lobos = pg.paginate_queryset(queryset=queryset, request=request, view=self)
        ser = zxserializer.LineOfBusinessOutletsSerializer(instance=lobos, many=True)
        return Response({
            'code': 200,
            'data': ser.data,
            'msg': 'success'
        })


@api_view(['GET'])
def exportblo(request, start, limit):
    s = int(start)
    l = int(limit)
    if s == 0 and l == 0:
        los = LineOfBusinessOutlets.objects.all()
    else:
        los = LineOfBusinessOutlets.objects.order_by('id')[s:l]
    ser = zxserializer.LineOfBusinessOutletsSerializer(instance=los, many=True)
    return Response({
        'code': 200,
        'data': {
            'header': ['网点名称', '路由器名称', '设备型号', '管理地址', '端口', '网点专线号', '带宽', 'B端IP'],
            'body': ser.data
        }
    })


@api_view(['GET'])
def exporteapi(request, start, limit):
    s = int(start)
    l = int(limit)
    if start == 0 and limit == 0:
        los = Eapi.objects.all()
    else:
        los = Eapi.objects.order_by('id')[s:l]

    ser = zxserializer.EaipSerializer(instance=los, many=True)
    return Response({
        'code': 200,
        'data': {
            'header': ['网络设备名称', '端口', '专线号', '带宽', '运营商', '专线类型', 'IP地址', 'ACL', '单位'],
            'body': ser.data
        },
        'msg': 'success'
    })
