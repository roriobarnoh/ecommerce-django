from django.contrib import admin
from .models import Categories, CustomerOrders, MerchantUser, ProductVarient, OrderDeliveryStatus, ProductReviews, ProductReviewVoting, Products, ProductQuestions, ProductMedia, ProductDetails, ProductAbout, ProductTags, ProductTransaction, ProductVarientItems, SubCategories, CustomerUser, StaffUser, AdminUser


# Register your models here.
admin.site.register(Categories)
admin.site.register(CustomerOrders)
admin.site.register(MerchantUser)
admin.site.register(ProductVarient)
admin.site.register(OrderDeliveryStatus)
admin.site.register(ProductReviews)
admin.site.register(ProductReviewVoting)
admin.site.register(Products)
admin.site.register(ProductQuestions)
admin.site.register(ProductMedia)
admin.site.register(ProductDetails)
admin.site.register(ProductAbout)
admin.site.register(ProductTransaction)
admin.site.register(ProductVarientItems)
admin.site.register(SubCategories)
admin.site.register(CustomerUser)
admin.site.register(StaffUser)
admin.site.register(AdminUser)
