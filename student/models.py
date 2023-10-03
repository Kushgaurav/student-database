from django.db import models

# Create your models here.


class studentDetail(models.Model):
    fullName = models.CharField(max_length=100)
    collageId = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    mobileNumber = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    date = models.DateField()
    # filename = models.CharField(max_length=10)
    file = models.FileField(upload_to='documents/')
    # file = models.FileField(upload_to= get_image_path, null=True, verbose_name="Uploaded File")
    course = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.collageId + " " + self.fullName + " " + self.subject
