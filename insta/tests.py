from django.test import TestCase
from .models import Image,Comment,Profile

#create test for image class
class imageTestClass(TestCase):
    # set up method
    def setUp(self):
        self.image=Image(Image_Description = 'the beaty nature',
        Image_Name='travel')

        # testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

# testing save method for image
    def test_save_method(self):
        self.image.save_image()
        images= Image.objects.all()
        self.assertTrue(len(images)> 0)

# testing delete image
    def test_delete_image(self):
        self.image=Image(Image_Description = 'the beaty nature',
        Image_Name='travel')

        self.image.delete_image()
        images= Image.objects.all()
        self.assertTrue(len(images)< 1)

class profileTestClass(TestCase):   
    #testing save method for class profile
    def test_save_method(self):
        self.profile.save_category()
        images= Profile.objects.all()
        self.assertTrue(len(images)> 0)

class CommentTestClass(TestCase):   
    #testing save method for class profile
    def test_save_method(self):
        self.comment.save_location()
        comments= Comment.objects.all()
        self.assertTrue(len(comments)> 0)

