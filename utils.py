import cv2
import numpy as np
import os
from azure.storage.blob import BlobServiceClient
import face_recognition

def extract_face(img):
    
    scale_factor = 1.1
    min_neighbors = 3
    min_size = (30, 30)

    cascade = cv2.CascadeClassifier("haarcascade_xmls/haarcascade_frontalface_alt.xml")
    print(cascade.empty())
    rects = cascade.detectMultiScale(img, scaleFactor=scale_factor, minNeighbors=min_neighbors,
                                          minSize=min_size)

    print("num of faces, ", len(rects))
    #if at least 1 face detected
    if len(rects) >= 0:
        
        # create the bounding box around the detected face
        
        blobs=[]
        for (x, y, w, h) in rects:
            #cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            extracted_face_blob = img[x:x+w, y:y+h]
            #cv2.imwrite('detected.jpg', img)
            blobs.append(extracted_face_blob)
        

        return blobs

    else:
        return None

def compare(image1, image2):
     
    width, height, depth= image1.shape
    try:
        encoding_image1 = face_recognition.face_encodings(image1) #, known_face_locations=[(0, width, height, 0)])
    except:
        return None
    encoding_image2 = face_recognition.face_encodings(image2)



    results = face_recognition.compare_faces([encoding_image1[0]], encoding_image2[0])
    
    return results

def detect_knife(image):
    return None 

constr = "DefaultEndpointsProtocol=https;AccountName=samplecctvfeed;AccountKey=VxWJUKjs9crSz3vGZPJeBNLeBAFtX14cAHyrHHEQdZBov0mhgydrhkHzmjZrr0wyoHoWG5ufdadC+AStARyhrA==;EndpointSuffix=core.windows.net"
container_name= "crimerepository"
service = BlobServiceClient.from_connection_string(conn_str=constr)

def fetch_imgs_from_azure_blob():
    # Download the blob to a local file
    # Add 'DOWNLOAD' before the .txt extension so you can see both files in the data directory
    
    container_client = service.get_container_client(container= container_name) 
    local_path = "criminal_images"

    blob_list = container_client.list_blobs()
    for blob in blob_list:
        download_file_path = os.path.join(local_path, blob.name)
        with open(file=download_file_path, mode="wb") as download_file:
            obj = container_client.download_blob(blob.name).readall()
            download_file.write(obj)

    return "Downloaded"

