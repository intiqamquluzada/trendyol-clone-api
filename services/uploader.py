class Uploader:

    @staticmethod
    def upload_photo_for_product(instance, filename):
        return f"product/{instance.slug}/{filename}"

    @staticmethod
    def upload_photo_for_shop(instance, filename):
        return f"shop/{instance.slug}/{filename}"

