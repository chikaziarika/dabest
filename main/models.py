from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.db import models
from django.contrib.auth.models import AbstractUser
from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from django.utils.translation import gettext as _


# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()
# drive = GoogleDrive(gauth)


# permission =  GoogleDriveFilePermission(
#    GoogleDrivePermissionRole.READER,
#    GoogleDrivePermissionType.USER,
#    "foo@mailinator.com"
# )

# gd_storage = GoogleDriveStorage(permissions=(permission, ))


DEPARTMENT = (
    (
        ('Research and Development', 'Research and Development'),
        ('Marketing & Communication', 'Marketing & Communication'),
        ('Project', 'Project'),
    )
)

EMPLOYEETYPE = (
    (
        ('REGULAR', 'REGULAR'),
        ('INTERNSHIP/ PART TIME', 'INTERNSHIP/ PART TIME'),
        ('BY PROJECT', 'BY PROJECT'),
    )
)

KATEGORI = (
    (
        ('Perencanaan Pesisir', 'Perencanaan Pesisir'),
        ('Pemanfaatan Sumber Daya Air', 'Pemanfaatan Sumber Daya Air'),
        ('Pengendalian Daya Rusak Air', 'Pengendalian Daya Rusak Air'),
        ('Konservasi Sumber Daya Air', 'Konservasi Sumber Daya Air'),
        ('Lain - Lain', 'Lain - Lain'),
    )
)

UNITIMPACT = (
    (
        ('Infrastruktur Pelabuhan', 'Infrastruktur Pelabuhan'),
        ('Jiwa Penduduk', 'Jiwa Penduduk'),
        ('Hektar Sawah', 'Hektar Sawah'),
        ('Hektar Permukiman yang terlindungi', 'Hektar Permukiman yang terlindungi'),
        ('Desain / Kajian', 'Desain / Kajian'),
        ('Hektar Lahan Konservasi', 'Hektar Lahan Konservasi'),
    )
)

LOCATION = (
    (
        ('Banda Aceh', ' Banda Aceh'),
        ('Langsa', ' Langsa'),
        ('Lhokseumawe', ' Lhokseumawe'),
        ('Sabang', ' Sabang'),
        ('Subulussalam', ' Subulussalam'),
        ('Denpasar', ' Denpasar'),
        ('Pangkalpinang', ' Pangkalpinang'),
        ('Cilegon', ' Cilegon'),
        ('Serang', ' Serang'),
        ('Tangerang Selatan', ' Tangerang Selatan'),
        ('Tangerang', ' Tangerang'),
        ('Bengkulu', ' Bengkulu'),
        ('Yogyakarta', ' Yogyakarta'),
        ('Gorontalo', ' Gorontalo'),
        ('Kota Administrasi Jakarta Barat', ' Kota Administrasi Jakarta Barat'),
        ('Kota Administrasi Jakarta Pusat', ' Kota Administrasi Jakarta Pusat'),
        ('Kota Administrasi Jakarta Selatan', ' Kota Administrasi Jakarta Selatan'),
        ('Kota Administrasi Jakarta Timur', ' Kota Administrasi Jakarta Timur'),
        ('Kota Administrasi Jakarta Utara', ' Kota Administrasi Jakarta Utara'),
        ('Sungai Penuh', ' Sungai Penuh'),
        ('Jambi', ' Jambi'),
        ('Bandung', ' Bandung'),
        ('Bekasi', ' Bekasi'),
        ('Bogor', ' Bogor'),
        ('Cimahi', ' Cimahi'),
        ('Cirebon', ' Cirebon'),
        ('Depok', ' Depok'),
        ('Sukabumi', ' Sukabumi'),
        ('Tasikmalaya', ' Tasikmalaya'),
        ('Banjar', ' Banjar'),
        ('Magelang', ' Magelang'),
        ('Pekalongan', ' Pekalongan'),
        ('Salatiga', ' Salatiga'),
        ('Semarang', ' Semarang'),
        ('Surakarta', ' Surakarta'),
        ('Tegal', ' Tegal'),
        ('Batu', ' Batu'),
        ('Blitar', ' Blitar'),
        ('Kediri', ' Kediri'),
        ('Madiun', ' Madiun'),
        ('Malang', ' Malang'),
        ('Mojokerto', ' Mojokerto'),
        ('Pasuruan', ' Pasuruan'),
        ('Probolinggo', ' Probolinggo'),
        ('Surabaya', ' Surabaya'),
        ('Pontianak', ' Pontianak'),
        ('Singkawang', ' Singkawang'),
        ('Banjarbaru', ' Banjarbaru'),
        ('Banjarmasin', ' Banjarmasin'),
        ('Palangka Raya', ' Palangka Raya'),
        ('Balikpapan', ' Balikpapan'),
        ('Bontang', ' Bontang'),
        ('Samarinda', ' Samarinda'),
        ('Nusantara', ' Nusantara'),
        ('Tarakan', ' Tarakan'),
        ('Batam', ' Batam'),
        ('Tanjungpinang', ' Tanjungpinang'),
        ('Bandar Lampung', ' Bandar Lampung'),
        ('Metro', ' Metro'),
        ('Ternate', ' Ternate'),
        ('Tidore Kepulauan', ' Tidore Kepulauan'),
        ('Ambon', ' Ambon'),
        ('Tual', ' Tual'),
        ('Bima', ' Bima'),
        ('Mataram', ' Mataram'),
        ('Kupang', ' Kupang'),
        ('Sorong', ' Sorong'),
        ('Jayapura', ' Jayapura'),
        ('Dumai', ' Dumai'),
        ('Pekanbaru', ' Pekanbaru'),
        ('Makassar', ' Makassar'),
        ('Palopo', ' Palopo'),
        ('Parepare', ' Parepare'),
        ('Palu', ' Palu'),
        ('Baubau', ' Baubau'),
        ('Kendari', ' Kendari'),
        ('Bitung', ' Bitung'),
        ('Kotamobagu', ' Kotamobagu'),
        ('Manado', ' Manado'),
        ('Tomohon', ' Tomohon'),
        ('Bukittinggi', ' Bukittinggi'),
        ('Padang', ' Padang'),
        ('Padang Panjang', ' Padang Panjang'),
        ('Pariaman', ' Pariaman'),
        ('Payakumbuh', ' Payakumbuh'),
        ('Sawahlunto', ' Sawahlunto'),
        ('Solok', ' Solok'),
        ('Lubuklinggau', ' Lubuklinggau'),
        ('Pagar Alam', ' Pagar Alam'),
        ('Palembang', ' Palembang'),
        ('Prabumulih', ' Prabumulih'),
        ('Binjai', ' Binjai'),
        ('Gunungsitoli', ' Gunungsitoli'),
        ('Medan', ' Medan'),
        ('Padangsidimpuan', ' Padangsidimpuan'),
        ('Pematangsiantar', ' Pematangsiantar'),
        ('Sibolga', ' Sibolga'),
        ('Tanjungbalai', ' Tanjungbalai'),
        ('Tebing Tinggi', ' Tebing Tinggi'),



    )
)

# class Map(models.Model):
#     id = models.AutoField( primary_key=True)
#     map_name = models.CharField(max_length=200)
#     map_data = models.FileField(upload_to='maps/', storage=gd_storage)

class DepartementList(models.Model):
    
    jobList = models.CharField(_("DEPARTEMENT"),max_length=200, unique=True)

    def __str__(self):
        return self.jobList

class EmployeeTypeList(models.Model):
    
    empType = models.CharField(_("EMPLOYEE TYPE"),max_length=200, unique=True)

    def __str__(self):
        return self.empType
    
    class Meta:
        verbose_name = _("Employee Type")


class Career(models.Model):
    position = models.CharField(max_length=200, unique=True)
    # department = models.CharField(max_length=200, choices=DEPARTMENT)
    department = models.ForeignKey(DepartementList, blank=True ,null=True, on_delete=models.PROTECT, db_constraint=False, related_name='department' , to_field='jobList' )
    # employeeType = models.CharField(max_length=200, choices=EMPLOYEETYPE)
    employeeType = models.ForeignKey(EmployeeTypeList, blank=True ,null=True, on_delete=models.PROTECT, db_constraint=False, related_name='employeeType' , to_field='empType' )
    location = models.CharField(max_length=200, choices=LOCATION)
    posting_date = models.DateTimeField(auto_now_add=True)
    jobDesk = CKEditor5Field('Text', config_name='extends')
    requirements = CKEditor5Field('Text', config_name='extends')
    

    class Meta:
        ordering = ['-posting_date']
        verbose_name = _("Career List")

    def __str__(self):
        return self.position

class User(AbstractUser):
    pass

class Project(models.Model):
    id_pekerjaan = models.AutoField(primary_key=True)
    namaPekerjaan = models.CharField(_("NAMA PEKERJAAN"),max_length=200)
    latCoor = models.DecimalField(_("LATITTUDE"),max_digits=9, decimal_places=6)
    longCoor = models.DecimalField(_("LONGITUDE"),max_digits=9, decimal_places=6)
    tahun = models.CharField(_("TAHUN PEKERJAAN"), max_length=4, null=True, blank=True)
    ktPekerjaan = models.CharField(_("KATEGORI PEKERJAAN"), max_length=100, null=True, blank=True, choices=KATEGORI)
    videoFile = models.FileField(_('VIDEO'), upload_to='media/%y', blank=True, null=True)
    impact = models.PositiveIntegerField(_("JUMLAH IMPACT"))
    unitImpact = models.CharField(_("UNIT IMPACT"), max_length=100, null=True, blank=True, choices=UNITIMPACT)

    def __str__(self):
        return self.namaPekerjaan
    
    class Meta:
        verbose_name = _("Project")
        
class Item(models.Model):
    title             = models.CharField(max_length=100)
    keywords          = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Tag(models.Model):
    nameTag = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nameTag    

class News(models.Model):
    id = models.AutoField(primary_key=True)
    # tags = models.CharField(_("TAGS"), max_length=100)
    headline = models.CharField(_("HEADER"), max_length=200)
    image = models.FileField(_("GAMBAR"), upload_to='images/%y', blank=True, null=True)
    textarea = CKEditor5Field('DESKRIPSI', config_name='extends')
    createAt = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='tags')

    class Meta:
        ordering = ['-createAt']
        verbose_name = _("Journal")

    def __str__(self):
        return self.headline
    
    def get_image_url(self):
        return self.image.url



class ActivityTag(models.Model):
    nameTag = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nameTag    

class Kegiatan(models.Model):
    ids = models.AutoField(primary_key=True)
    # tags = models.CharField(_("TAGS"), max_length=100)
    headline = models.CharField(_("HEADER"), max_length=200)
    image = models.FileField(_("GAMBAR"), upload_to='images/%y', blank=True, null=True)
    textarea = CKEditor5Field('DESKRIPSI', config_name='extends')
    createAt = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(ActivityTag, related_name='tags')

    class Meta:
        ordering = ['-createAt']
        verbose_name = _("DABEST Activities")

    def __str__(self):
        return self.headline
    
    def get_image_url(self):
        return self.image.url





GENDER = (
    (
        ('LAKI - LAKI', 'LAKI - LAKI'),
        ('PEREMPUAN', 'PEREMPUAN'),
        
    )
)

NATIONALITY = (
    (
        ('WNI', 'WNI'),
        ('WNA', 'WNA'),
        
    )
)

LICENSE = (
    (
        ('SIM A', 'SIM A'),
        ('SIM B', 'SIM B'),
        ('SIM C', 'SIM C'),
    )
)

STATUS = (
    (
        ('Pending', 'Pending'),
        ('Reject', 'Reject'),
        ('Approve', 'Approve'),
        ('On Review', 'On Review'),
    )
)

KLASIFIKASI = (
    (
        ('', '--Silahkan Pilih--'),
        ('Muda', 'Muda'),
        ('Madya', 'Madya'),
        ('Utama', 'Utama')
    )
)


from phone_field import PhoneField

class InputApplicant(models.Model):
    id = models.AutoField(primary_key=True)
    jobPosition = models.CharField(_("JOB APPLICANT FOR"),max_length=255, blank=True)
    FirstName = models.CharField(_("FIRST NAME"), max_length=200)
    LastName = models.CharField(_("LAST NAME"), max_length=200)
    Gender = models.CharField(_("JENIS KELAMIN"), max_length=20, choices=GENDER)
    DoB = models.DateField(_("TANGGAL LAHIR"), )
    PoB = models.CharField(_("TEMPAT LAHIR"), max_length=50)
    Nationality = models.CharField(_("WARGA NEGARA"), max_length=20, choices=NATIONALITY)
    personalEmail = models.EmailField(_("EMAIL"), max_length=254)
    personalMobile = PhoneField(_("NO. TELEPHONE"),blank=True)
    LicDrive = models.CharField(_("DRIVING LICENSE"), max_length=5, choices=LICENSE)
    linkedin = models.CharField(_("LINKEDIN ID"), max_length=254)
    address_1 = models.CharField(_("ADDRESS_1 "), max_length=254)
    address_2 = models.CharField(_("ADDRESS_2 "), max_length=254)
    expectedSalary = models.IntegerField(_('SALARY'))
    grossSalary = models.IntegerField(_('GROSS SALARY'))
    medicalHistory = models.TextField(_("MEDICAL HISTORY"))
    ReferensiInfo = models.CharField(_("Referensi Info"), max_length=152)
    referensiName = models.CharField(_("Referensi Name"), max_length=152) 
    referensiRelasi = models.CharField(_("Referensi Relasi"), max_length=152)
    submit_at = models.DateTimeField(auto_now_add=True)

class UploadApplicant(models.Model):
    id = models.AutoField(primary_key=True)
    document = models.FileField(null=True, blank=True,upload_to='files/%y')
    jobPosition = models.CharField(max_length=255, blank=True)
    ApplicantName = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    subklasifikasiSKA = models.CharField(max_length=255, null=True,  blank=True)
    klasifikasiSKA = models.CharField(max_length=5, null=True,  blank=True, choices=KLASIFIKASI)
    lampiranSKA = models.FileField(null=True, blank=True,upload_to='files/%y')
    status = models.CharField(_("Status"), max_length=20, choices=STATUS, default='Pending')

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = _("   Pending Applicant")

    def __str__(self):
        return self.ApplicantName

    
class ApprovedApplicant(UploadApplicant):
    class Meta:
        proxy = True
        verbose_name = _("  Approve Applicant")

class RejectApplicant(UploadApplicant):
    class Meta:
        proxy = True
        verbose_name = _(" Reject Applicant")

class ReviewApplicant(UploadApplicant):
    class Meta:
        proxy = True
        verbose_name = _(" Review Applicant")


from allauth.socialaccount.forms import SignupForm
class MyCustomSocialSignupForm(SignupForm):

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSocialSignupForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user