from django.test import TestCase
from .models import Category,Location,Image

# Create your tests here.

class CategoryTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.Fashion= Category(category='Fashion')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.Fashion,Category))
        
    def tearDown(self):
        Category.objects.all().delete()
        
    def test_save_method(self):
        self.Fashion.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)
    
class LocationTestClass(TestCase):
    
    def setUp(self):
        self.Santorini=Location(location='Santorini')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.Santorini,Location))
        
    def tearDown(self):
        Location.objects.all().delete()
        
    def test_save_method(self):
        self.Santorini.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)
        
class ImageTestClass(TestCase):
    def setUp(self):
        self.test_category = Category(category=list('Fashion'))
        self.test_category.save_category()

        self.location = Location(location="Santorini")
        self.location.save_location()

        self.image = Image(id=1,image_name="Greece",image_description="Number one tourist destination",category=self.test_category,location=self.location,)
        self.image.save_image()

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()       