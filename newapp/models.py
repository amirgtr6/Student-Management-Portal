from django.db import models

# Create your models here.


  




class newapp(models.Model):
  dars= models.CharField(max_length=255 ,null=True ,blank = True , verbose_name = "درس")
  akharin_nomre  = models.CharField(max_length=255 ,default='' ,blank=True , verbose_name = "آخرين نمره")
  code_standard= models.CharField(max_length=255 ,default='' ,blank=True , verbose_name = "کد استاندارد")
  noe_dars= models.CharField(max_length=255 ,null=True , blank = True , verbose_name = "نوع درس")
  vahed_teori= models.CharField(max_length=255 ,default='' ,blank=True , verbose_name = "واحد تئوري")
  vahed_amali = models.CharField(max_length=255 ,default='' ,blank=True , verbose_name = "واحد عملي")
  saat_teori=  models.CharField(max_length=255 ,default='' ,blank=True , verbose_name = "ساعت تئوري")
  saat_amali=  models.CharField(max_length=255 ,default='' ,blank=True , verbose_name = "ساعت عملي")
  pish_niaz= models.CharField(max_length=255 , null=True , blank = True , verbose_name = "پيش نيازها")
  code_pish_niaz=    models.CharField(max_length=255 ,default='' ,blank=True , verbose_name = "کد پيش نيازها")
 


class daneshjo(models.Model):
  shomare_daneshjoi = models.CharField(max_length=255 ,default='' ,blank=True , verbose_name = "شماره دانشجويي")
  #newapp = models.ForeignKey(newapp , blank = True , null = True , on_delete=models.CASCADE)
  code_meli = models.CharField(max_length=255 ,default='' ,blank=True , verbose_name = "کد ملي")
  name = models.CharField(max_length=255 ,null=True ,blank = True , verbose_name = "نام")
  daneshkade =  models.CharField(max_length=255 ,null=True ,blank = True , verbose_name = "دانشکده")
  reshte =  models.CharField(max_length=255 ,null=True ,blank = True , verbose_name = "رشته")
  maqta =  models.CharField(max_length=255 ,null=True ,blank = True , verbose_name = "مقطع")
  nobat_paziresh =  models.CharField(max_length=255 ,null=True ,blank = True , verbose_name = "نوبت پذيرش")
  term_vorood = models.CharField(max_length=255 ,default='' ,blank=True , verbose_name = "ترم ورود")
  nam_pedar =  models.CharField(max_length=255 ,null=True ,blank = True , verbose_name = "نام پدر")
  tarikh_tavalod = models.CharField(max_length=255 ,null=True ,blank = True , verbose_name = "تاريخ تولد")

  

class info_dars(models.Model):
  
  dars= models.CharField(max_length=255 ,null=True ,blank = True , verbose_name = "درس")
  dars_info= models.CharField(max_length=255 ,null=True ,blank = True , verbose_name = "اطلاعات درس")
