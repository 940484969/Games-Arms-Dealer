from django.shortcuts import render, redirect, HttpResponse
from app_commidity.models import *
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.


from django.views import View


# Create your views here.

class IndexShow(View):
    """
    主页显示
    """

    def get(self, request):
        carousel = HomeCarousel.objects.all()
        # print(carousel)
        # print(carousel[0].sku_id.commditypicture_set.all()[0].comm_picture.name)
        promotion = HomePromotion.objects.all()
        # print(promotion)
        # print(promotion.count())
        # print(promotion[0].sku_id.commditypicture_set.all()[0].comm_picture.name)
        sku = CommoditySku.objects.all()

        return render(request, "index.html", locals())


class ProductShow(View):
    """
    商品详情显示
    """

    def get(self, request):
        # print()
        id = request.GET.get('i')
        obj = CommoditySku.objects.filter(sku_id=id).first()
        # print(obj)


        pic = obj.commditypicture_set.all()

        # print(pic)
        return render(request, "product.html", locals())


class Category(View):
    """
    种类显示
    """

    def get(self, request, *args):
        try:
            # cate = request.get_full_path().split('/')[2]
            cate = args[0]
            # print(cate)
            if cate == '1':
                obj = CommodityKind.objects.filter(com_name='动作')
            elif cate == '2':
                obj = CommodityKind.objects.filter(com_name='冒险')
            elif cate == '4':
                obj = CommodityKind.objects.filter(com_name='单人')
            elif cate == '6':
                obj = CommodityKind.objects.filter(com_name='多人')
            elif cate == '8':
                obj = CommodityKind.objects.filter(com_name='剧情')
            elif cate == '9':
                obj = CommodityKind.objects.filter(com_name='体育')
            elif cate == '10':
                obj = CommodityKind.objects.filter(com_name='心理恐怖')
            # obj2 = CommodityKind.objects.first()
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
            # print(111111111111)
            return redirect(reverse('app_commidity:index'))


class ReviewShow(View):

    def get(self, request):
        id = request.GET.get('i')
        obj = CommoditySku.objects.filter(sku_id=id).first()
        rev = Review.objects.filter(sku_id__sku_id=id)
        # print(rev)
        return render(request, 'review.html', locals())

    def post(self, request):
        id = request.GET.get('i')
        obj = CommoditySku.objects.filter(sku_id=id).first()
        rev = Review.objects.filter(sku_id__sku_id=id)
        print(request.POST.get('i1'))
        # print(rev)
        return redirect('/review/')


# class ReviewGet(View):
#     def post(self, request):
#         id = request.GET.get('i')
#         obj = CommoditySku.objects.filter(sku_id=id).first()
#         rev = Review.objects.filter(sku_id__sku_id=id)
#         print(request.POST.get('i1'))
#         # print(rev)
#         return render(request, 'review.html', locals())

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
