from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from accounts.models import Account


class Testimonial(models.Model):
    client = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='Client')
    message = RichTextUploadingField(_('Message'))
    submission_date = models.DateTimeField(_('Submission Date'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        db_table = 'testimonials'

    def __str__(self):
        return self.client.first_name
