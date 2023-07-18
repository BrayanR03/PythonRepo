from PIL import Image,ImageOps,ImageEnhance,ImageChops
seguir=True
while seguir:
    print '<<NECIOSUP BOLANOS BRAYAN RAFAEL>>'
    print '<< PROCESAMIENTO DE IMAGENES EN PYTHON >>'
    print '<< IMAGENES: tigre / dragon >>'
    img=raw_input('ELIGE UNA IMAGEN: \n')
    img_formato=img+'.jpg'
    imagen_nueva=''

    try:
        img_formato=Image.open(img_formato)
        #img_formato.show()
        print 'MENU PROCESAMIENTO\n'
        print '1. INVERTIR IMAGEN\n2. ESCALA GRISES\n3. RESALTADO IMAGEN\n4. CONTRASTAR IMAGEN'
        print '5. MODO ESPEJO IMAGEN\n6. DISMINUIR NITIDEZ\n7. CAMBIAR TAMANIO IMAGEN\n8. RANGE IMAGEN\n'
        opcion =int(raw_input('ELIGE UNA OPCION: \n'))
        if opcion==1:
            imagen_nueva=ImageChops.invert(img_formato)
            imagen_nueva.save(img+'_imagen_invertida.jpg')
            imagen_nueva.show()
        elif opcion==2:
            imagen_nueva=ImageOps.grayscale(img_formato)
            imagen_nueva.save(img+'_imagen_gris.jpg')
            imagen_nueva.show()
        elif opcion==3:
            imagen_nueva=ImageEnhance.Brightness(img_formato).enhance(3)
            imagen_nueva.save(img+'_imagen_resaltada.jpg')
            imagen_nueva.show()
        elif opcion==4:
            imagen_nueva=ImageEnhance.Contrast(img_formato).enhance(4)
            imagen_nueva.save(img+'_imagen_contraste.jpg')
            imagen_nueva.show()
        elif opcion==5:
            imagen_nueva=ImageOps.mirror(img_formato)
            imagen_nueva.save(img+'_imagen_espejo.jpg')
            imagen_nueva.show()
        elif opcion==6:
            imagen_nueva=ImageEnhance.Sharpness(img_formato).enhance(-100)
            imagen_nueva.save(img+'_imagen_nitidez.jpg')
            imagen_nueva.show()
        elif opcion==7:
            ancho=int(raw_input('INGRESA EL ANCHO: \n'))
            alto=int(raw_input('INGRESA ALTURA: \n'))
            imagen_nueva=img_formato.resize((ancho,alto))
            imagen_nueva.save(img+'_tamanio_imagen_modificado.jpg')
            imagen_nueva.show()
        elif opcion==8:
            imagen_nueva=img_formato.convert('L')
            ancho,alto=imagen_nueva.size
            print 'EL ANCHO ES: ',ancho,'\n','EL ALTO ES: ',alto
        else:
            print 'ESTA OPCION NO EXISTE'

    except:
        print 'Error, la imagen no existe'
    eleccion=raw_input('ELEGIR OTRA IMAGEN? SI-NO\n')
    if eleccion.upper()==('SI'):
        seguir
    else:
        seguir=False
    
print 'FIN PROGRAMA'
