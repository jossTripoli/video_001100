import json
from boto3 import Session

def generateAudioUsingText(plainText,filename):
    # Generate audio using Text
    session = Session(region_name="us-east-1")
    polly = session.client("polly")
    response = polly.synthesize_speech( Text=plainText,
                                        Engine = "neural",
                                        TextType = "text",
                                        OutputFormat="mp3",
                                        SpeechMarkTypes=["sentence","word"],
                                        VoiceId="Danielle")
    s3 = session.resource('s3')
    bucket_name = "dart-store"
    bucket = s3.Bucket(bucket_name)
    filename = "narration/concepts/" + filename
    stream = response["AudioStream"]
    bucket.put_object(Key=filename, Body=stream.read())
    
def generateAudioUsingSSML(ssmlText,filename):
    # Generate audio using Text
    session = Session(region_name="us-east-1")
    polly = session.client("polly")
    response = polly.synthesize_speech( Text=ssmlText,
                                        Engine = "neural",
                                        TextType = "ssml",
                                        OutputFormat="mp3",
                                        SpeechMarkTypes=["sentence","word"],
                                        VoiceId="Danielle")
    s3 = session.resource('s3')
    bucket_name = "dart-store"
    bucket = s3.Bucket(bucket_name)
    filename = "narration/concepts/" + filename
    stream = response["AudioStream"]
    bucket.put_object(Key=filename, Body=stream.read())


def lambda_handler(event, context):

    # Generate audio using Text
    generateAudioUsingText('Leave it better than you found it','polly-text-demo.mp3')
    
    # Generate audio using SSML
    generateAudioUsingSSML('<speak>If everyone does a little bit <break time="1000ms"/> it adds up to alot</speak>','polly-ssml-demo.mp3')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successful Generation of Audio File(s) using AWS Polly')
    }
