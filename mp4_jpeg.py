import cv2
vidcap = cv2.VideoCapture(r'C:\Users\alex_\OneDrive\Desktop\Matsuev_Video_Flat_Curve\C0006_rotated.MP4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite(r"C:\Users\alex_\OneDrive\Desktop\Matsuev_Video_Flat_Curve\jpegs\frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1