import face_recognition
import utils
import cv2

# image1 = face_recognition.load_image_file("images/alia1.jfif")
# image2 = face_recognition.load_image_file("images/kiara2.jfif")

# results= utils.compare(image1, image2)

# print(results) 

full_image = cv2.imread("images/full_image_random2.jpeg")
#print(full_image)
faces = utils.extract_face(full_image)
cv2.imwrite("test_output/output_face.jpg", faces[0])