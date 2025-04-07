from sell.models import Coaches, Reviews, Product

COURSE_CHOICES = {
    '1': 'Маркетинг',
    '2': 'Программирование',
    '3': '3D-Дизайн',
}

class CourseFilter:
    def __init__(self, max_price=None, min_price=None, category=None, with_reviews_only=False):
        self.max_price = max_price
        self.min_price = min_price
        self.category = category
        self.with_reviews_only = with_reviews_only
    def find(self):
        qs = Product.objects.all()

        if self.min_price is not None:
            qs = qs.filter(price__gte=self.min_price)

        if self.max_price is not None:
            qs = qs.filter(price__lte=self.max_price)

        if self.category:
            qs = qs.filter(category_id=self.category)

        if self.with_reviews_only:
            qs = qs.filter(Отзыв__isnull=False).distinct()
        return qs


def get_coaches():

    return Coaches.objects.all()

def get_reviews_list():

    return Reviews.objects.select_related('article', 'user').all()

def create_review(course_id, review_text, user=None):

    try:
        product = Product.objects.select_for_update().get(pk=course_id)
        review = Reviews.objects.create(product=product, text=review_text, user=user)
        return review

    except Product.DoesNotExist:

        raise ValueError(f"Курс с ID {course_id} не найден")

def get_courses():

    return Product.objects.all()
def get_reviews_list():

    return Reviews.objects.select_related('article', 'user').all()
