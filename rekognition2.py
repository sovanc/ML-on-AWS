import boto3
import json 

if __name__ == "__main__":
    imageFile = 'Star-Trek.jpg'
    client = boto3.client('rekognition')
    
    with open(imageFile, 'rb') as image:
        response = client.detect_faces(Image = {'Bytes': image.read()})
    
    print('Detected faces for ' + imageFile)
    for faceDetail in response['FaceDetails']:
        print('Here are the attributes:')
        print(json.dumps(faceDetail, indent=4, sort_keys=True))
    
    print('...\n')
    print('What do you think, heh?')