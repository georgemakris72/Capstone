from django.db import models
from django.db import models

#IMPORT post_save signal
from django.db.models.signals import pre_save, post_save

#Import Reversse Lookup resolver
from django.core.urlresolvers import reverse



#IMport Slugify
from django.utils.text import slugify
# Create your models here.

class Instrument(models.Model):
    title = models.CharField(max_length = 50)
    exchange = models.CharField(max_length = 150)
    symbol = models.CharField(max_length = 50)
    multiplier=models.IntegerField()
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('instrument_detail_slug', kwargs={'slug': self.slug})
        #self.slug refers to Product.slug

def instrument_pre_save_receiver(sender,instance,*args,**kwargs):
    print(sender) #sender =Product Class
    print(instance) #instance = Newly Created product of the database.


    if not instance.slug:
        instance.slug=slugify(instance.title)  # Product (i.e shoe doesn't have a slug, create one.)

pre_save.connect(instrument_pre_save_receiver,sender=Instrument)


class Variation(models.Model):
    instrument=models.ForeignKey(Instrument)
    title=models.CharField(max_length=50)
    active=models.BooleanField(default=True)
    symbol=models.CharField(max_length = 50)
    multiplier=models.IntegerField()

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        """This absolute url will receive the instruments slug value and only be available
        from the Variation class.  We will use the ForeignKey relationship from
        Instrument to access the slug value."""

        return self.instrument.get_absolute_url()

    def add_to_cart(self):
        return "{}/?item={}&qty=1".format(reverse("cart"),self.id)

    def remove_from_cart(self):
        """This function will remove one item from the cart when called upon"""
        return "{}/?item={}&qty=1&delete=True".format(reverse("cart"),self.id)


    def get_title(self):
        return "{}-{}".format(self.instrument.title,self.title)



def instrument_variation_post_save_receiver(sender,instance,created,*args,**kwargs):
    print(sender)#sender is the Variation
    print(instance)#instance is the newly created product Variation
    print(created)#This will print when a new product variation is created

    instrument=instance
    variations=instrument.variation_set.all()

    if variations.count() == 0:
        new_variation=Variation()
        new_variation.instrument=instrument#using the foreignkey relationship from Product
        new_variation.title="Liquid Contract"#Creating our default variation if nome exist
        new_variation.multiplier = instrument.multiplier
        new_variation.save() #Saving the variation to the database
        # variations = Variation.objects.order_by('instrument')
    print(created)#This will print when a new instrument variation is created

post_save.connect(instrument_variation_post_save_receiver, sender=Instrument)

# Create your models here.
