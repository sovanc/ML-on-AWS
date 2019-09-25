import boto3
import json 

if __name__ == "__main__":
    imageFile = 'Star-Trek.jpg'
    client = boto3.client('rekognition')
    
    with open(imageFile, 'rb') as image:
        response = client.recognize_celebrities(Image = {'Bytes': image.read()})
    
    print('Detected faces for ' + imageFile)
    for celebrity in response['CelebrityFaces']:
        print('Name: ' + celebrity['Name'])
        print('Id: ' + celebrity['Id'])
        print('Position: ')
        print('     Left: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Height']))
        print('     Top: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Top']))
        print('Info')
        
        for url in celebrity['Urls']:
            print(' ' + url)
        
        print()
        
    print('...\n')
    print('What do you think, heh?')