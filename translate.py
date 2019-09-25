import boto3

translate = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)
t = "Hello, my name is Larry.  I'm the presenter today."
result = translate.translate_text(Text=t, SourceLanguageCode="en", TargetLanguageCode="es")
print(t)
print('Translated Text: ' + result.get('TranslatedText'))
print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))

