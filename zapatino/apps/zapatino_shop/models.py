from django.db import models
from django.contrib import admin

# Clase categoria IDNUMENTARIA/CALZADO
class categoria(models.Model):
    nombre = models.CharField(max_length=30)
    
    def __unicode__ (self):
        return self.nombre
# Clase para agregar filtros y busquedas en ADMIN DJANGO    
class categoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ('nombre',)
    search_fields = ('nombre',)
        
# Clase Marca
class marca(models.Model):
    nombre = models.CharField(max_length=30)
    
    def __unicode__ (self):
        return self.nombre


class tallenumero(models.Model):
    tallenumero_desc = models.CharField(max_length = 30)
    
    def __unicode__(self):
        return self.tallenumero_desc
    
# Clase Ciudad    
class ciudad(models.Model):
    nombre = models.CharField(max_length = 30)
    
    def __unicode__(self):
        return self.nombre
#Clase Provincia
class provincia(models.Model):    
    nombre = models.CharField(max_length = 30, primary_key = True)
    ciudad = models.ManyToManyField(ciudad)
  
    def __unicode__(self):
        return unicode(self.ciudad)  

              
    
# Clase Persona **DATOS COMUNES EN CLIENTE Y PROVEEDOR** CLASE PADRE DE CLIENTE/PROVEEDOR
class persona(models.Model):
    telefono = models.IntegerField(null = True)
    direccion = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    codigo_postal = models.IntegerField(null = True)    
  
#CLASE CLIENTE
class cliente(persona):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField(null = True)
    fecha_nacimiento = models.DateField(null = True)
   
    def __unicode__ (self):
        return self.nombre 


class clienteAdmin(admin.ModelAdmin):
    fields = ('nombre', 'apellido', 'dni', 'fecha_nacimiento', 'telefono', 'direccion', 'email', 'codigo_postal',)
    
    
    
    
# Clase Proveedor
class proveedor(persona):
    razon_social = models.CharField(max_length=30)
    marca = models.ForeignKey(marca)
    cuit = models.CharField(max_length=30)
    cbu = models.CharField(max_length=30)
    ncuenta = models.CharField(max_length=30)
    contacto = models.CharField(max_length = 50)
    
    def __unicode__ (self):
        return unicode(self.marca)
    
class proveedorAdmin(admin.ModelAdmin):
    fields = ('razon_social', 'marca', 'cuit', 'cbu', 'ncuenta', 'contacto', 'telefono', 'direccion', 'email', 'codigo_postal',)

# Clase Producto    
class producto(models.Model):
    codigo = models.CharField(max_length=30)
    categoria = models.ForeignKey(categoria, null = True)
    fecha_ingreso = models.DateField(null = True)
    precio_costo = models.FloatField(null = True)
    precio_publico = models.FloatField(null = True)
    proveedor = models.ForeignKey(proveedor, null = True)
    stock_minimo = models.IntegerField(null = True)
    stock_maximo = models.IntegerField(null = True)
    
    def __unicode__ (self):
        return self.codigo 
    

class detalle_producto(models.Model):
    producto = models.ForeignKey(producto, db_column='producto_id')
    tallenumero = models.ForeignKey(tallenumero, db_column='tallenumero_id')
    cantidad = models.IntegerField(null = True)
    descipcion = models.CharField(max_length=50, null = True)
    
    def __unicode__ (self):
        return unicode(self.cantidad)   
    

class detalle_productoInline(admin.TabularInline):
    model = detalle_producto
    


class productoAdmin(admin.ModelAdmin):
    inlines = (detalle_productoInline,)
    list_display = ('codigo','categoria','fecha_ingreso', 'precio_publico', 'proveedor',)
    list_filter = ('codigo', 'categoria',)
    search_fields = ('codigo', 'precio_publico','categoria__nombre','proveedor__marca__nombre',)       


    
admin.site.register(producto, productoAdmin)         
admin.site.register(categoria,categoriaAdmin)
admin.site.register(cliente, clienteAdmin)
admin.site.register(proveedor, proveedorAdmin)



