import random
#Pictures
from PIL import Image, ImageDraw, ImageFont,ImageOps
import io,qrcode
import numpy as np

from PIL import Image
from io import BytesIO


def qrAdder(img_bg):

	qr = qrcode.QRCode(box_size=4,border=1)
	qr.add_data(
    
    random.choice([
      'https://github.com/8chanjikwatkinsQQQQQEdwardArthurKane/8kun_8coon'+str(random.randint(1, 1111)),
      'https://www.offenderradar.com/offender-details/edward-arthur-kane-of-idaho-523009'+str(random.randint(1, 1111)),
      ])
    )
	qr.make()
	img_qr = qr.make_image()


	adder=int(img_qr.size[0]/25)#how much background do you want?
	greenborder = Image.new('RGB', ((img_qr.size[0])+adder, (img_qr.size[1])+adder), (0,255,0))
	old_size = img_qr.size
	new_size = greenborder.size
	posQR = (int((new_size[0]-old_size[0])/2),int((new_size[1]-old_size[1])/2))

	greenborder.paste(img_qr, posQR)#greenborder
	img_qr = greenborder#give it a green border

	minus_QrSize = img_qr.size[0]#QR code size
	#print(minus_QrSize)
	###############################
	#X,Y
	x_qr = img_bg.size[0]
	y_qr = img_bg.size[1]

	if (minus_QrSize >= x_qr):
		raise Exception('ImageTooSmall (The image is smaller in x-y length then the QR)')
	else:
		max_value_x = x_qr-minus_QrSize
	#-----------------------------
	if (minus_QrSize >= y_qr):
		raise Exception('ImageTooSmall (The image is smaller in x-y length then the QR)')
	else:
		max_value_y = y_qr-minus_QrSize
	#-----------------------------
	for index in range(1):
		rando_x = random.randint(int(1),max_value_x)#x_qr/6 up to hald of x_qr
		rando_y = random.randint(int(1),max_value_y)
		pos = (rando_x, rando_y)

		img_bg.paste(img_qr, pos)
	return img_bg



    # Function to change the image size

def changeImageSize(maxWidth,
                    maxHeight,
                    image):

  widthRatio  = maxWidth/image.size[0]
  heightRatio = maxHeight/image.size[1]

  newWidth    = int(widthRatio*image.size[0])
  newHeight   = int(heightRatio*image.size[1])

  newImage    = image.resize((newWidth, newHeight))
  return newImage

def CounterANTISPAM(image2):
  width, height = image2.size

  # Make the images of uniform size
  image4 = changeImageSize(width, height, image2)

  # Make sure images got an alpha channel
  image6 = image4.convert("RGB")

  # Create's random pixel picture
  arr = np.random.randint(0,255,(250,250,3))

  im = Image.fromarray(arr,'RGB')
  image7 = im.convert("RGB")

  image7 = changeImageSize(width, height, image7)


  alphaBlended2 = Image.blend(image6, image7, alpha=.10)

  #alphaBlended2.show()
  return alphaBlended2

def randomize_image(selected_image):
  picture_1 = Image.open(selected_image)

  ##### CounterANTISPAM
  picture_1 = CounterANTISPAM(picture_1)
  #####

  length, width = picture_1.size

  resized_picture_1 = picture_1.resize((length + random.randint(1, 250), width+ random.randint(1, 250)), Image.NEAREST)
  length, width = picture_1.size#recheck size

  #cpu intensive dont use pointless
  # data = list(resized_picture_1.getdata())
  # image_without_exif = Image.new(resized_picture_1.mode, resized_picture_1.size)
  # image_without_exif.putdata(data)
  # resized_picture_1=image_without_exif#setting Var_resized_picture_1 to exifless

  # resized_picture_1.show()

  ###
  qr=True
  if qr:
    for x in range(2):
      resized_picture_1 = qrAdder(resized_picture_1)

  image_bytes = io.BytesIO()
  resized_picture_1.save(image_bytes, 'jpeg'
    ,quality=30,optimize=True
  )############JPEG
  # resized_picture_1.show()


  #image_bytes.seek(0)
  return image_bytes
# randomize_image("bot research meme.png")