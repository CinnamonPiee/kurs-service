from .models import (
	BasePageFooter,
	BasePageSocialImages,
    BasePageFooterImage,
    BasePageHeader,
    BasePageSideMenu,
    BasePageNotification,
    BasePageAddOrderServiceModal,
)


def base_page(request):
    return {
        "base_page_side_menu": BasePageSideMenu.objects.first(),
        "base_page_header": BasePageHeader.objects.first(),
        "base_page_footer_image": BasePageFooterImage.objects.first(),
        "base_page_social_images": BasePageSocialImages.objects.all(),
        "base_page_footer": BasePageFooter.objects.first(),
        "base_page_notification": BasePageNotification.objects.first(),
        "base_page_add_order_service_modal": BasePageAddOrderServiceModal.objects.all(),
    }