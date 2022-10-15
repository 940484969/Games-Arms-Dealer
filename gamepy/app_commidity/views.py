from django.shortcuts import render, redirect,HttpResponse
from app_commidity.models import *
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.


from django.views import View


# Create your views here.

class IndexShow(View):
    def get(self, request):
        return render(request, "index.html")


class ProductShow(View):
    """
    商品详情显示
    """

    def get(self, request):
        return render(request, "product.html")


class Category(View):
    """
    种类显示
    """

    def get(self, request):
        try:
            cate = request.get_full_path().split('/')[2]
            if cate == 'action':
                obj = CommodityKind.objects.filter(com_name='动作')
            elif cate == 'venture':
                obj = CommodityKind.objects.filter(com_name='冒险')
            elif cate == 'single':
                obj = CommodityKind.objects.filter(com_name='单人')
            elif cate == 'multiplayer':
                obj = CommodityKind.objects.filter(com_name='多人')
            elif cate == 'drama':
                obj = CommodityKind.objects.filter(com_name='剧情')
            elif cate == 'sports':
                obj = CommodityKind.objects.filter(com_name='体育')
            elif cate == 'horror':
                obj = CommodityKind.objects.filter(com_name='心理恐怖')
            obj2 = CommodityKind.objects.first()
            cate_name = obj[0].com_name
            cate_part = obj.first().commoditysku_set.all()
            # print(cate_part)
            # cate_part = obj.first().commoditysku_set.all()
            '''分页'''
            current_page = request.GET.get('page')
            paginator = Paginator(cate_part, 4)
            try:
                posts = paginator.page(current_page)
                # 含有属性：
                # per_page:每页显示条数
                # count数据总数
                # num_pages:总页数
                # page_range:总页数索引范围
                # page：page对象
                # 如果输入的页面不是整数,就返回到第一页
            except PageNotAnInteger as e:
                posts = paginator.page(1)

                # 如果输入的页码数负数,则显示到最后一页
            except EmptyPage as e:
                posts = paginator.page(paginator.num_pages)
                # has_next              是否有下一页
                # next_page_number      下一页页码
                # has_previous          是否有上一页
                # previous_page_number  上一页页码
                # object_list           分页之后的数据列表
                # number                当前页
                # paginator             paginator对象
            # return HttpResponse('666')
            return render(request, "category.html", locals())
        except Exception:
            print(111111111111)
            return redirect(reverse('app_commidity:index'))

    # Action
# Venture
# Single
# Multiplayer
# Drama
# Sports
# Horror

# class Action(View):
#     """
#     动作类
#     """
#     def get(self, request):
#         return render(request, "category.html")
#
#
# class Venture(View):
#     """
#     冒险类
#     """
#     def get(self, request):
#         return render(request, "category.html")
#
# class Single(View):
#     """
#     担任类
#     """
#
#     def get(self, request):
#         return render(request, "category.html")
#
# class Multiplayer(View):
#     """
#     多人类
#     """
#
#     def get(self, request):
#         return render(request, "category.html")
#
# class Drama(View):
#     """
#     剧情类
#     """
#
#     def get(self, request):
#         return render(request, "category.html")
#
#
# class Sports(View):
#     """
#     体育类
#     """
#
#     def get(self, request):
#         return render(request, "category.html")
#
#
# class Horror(View):
#     """
#     恐怖类
#     """
#
#     def get(self, request):
#         return render(request, "category.html")
#

# Action
# Venture
# Single
# Multiplayer
# Drama
# Sports
# Horror
