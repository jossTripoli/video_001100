import json
from boto3 import Session

def generateAudioUsingText(plainText, filename, myVoiceId):
    # Generate audio using Text
    session = Session(region_name="us-east-1")
    polly = session.client("polly")
    response = polly.synthesize_speech( Text=plainText,
                                        Engine = "neural",
                                        TextType = "text",
                                        OutputFormat="mp3",
                                        VoiceId=myVoiceId)
    s3 = session.resource('s3')
    bucket_name = "dart-store"
    bucket = s3.Bucket(bucket_name)
    filename = "narration/concepts/" + filename
    stream = response["AudioStream"]
    bucket.put_object(Key=filename, Body=stream.read())
    
    
def generateSpeechMarksUsingText(plainText, filename, myVoiceId):
    # Generate audio using Text
    session = Session(region_name="us-east-1")
    polly = session.client("polly")
    response = polly.synthesize_speech( Text=plainText,
                                        Engine = "neural",
                                        TextType = "text",
                                        OutputFormat="json",
                                        SpeechMarkTypes=["sentence","word"],
                                        VoiceId=myVoiceId)
    s3 = session.resource('s3')
    bucket_name = "dart-store"
    bucket = s3.Bucket(bucket_name)
    filename = "narration/concepts/" + filename
    stream = response["AudioStream"]
    bucket.put_object(Key=filename, Body=stream.read())
    
def generateAudioUsingSSML(ssmlText, filename, myVoiceId):
    # Generate audio using Text
    session = Session(region_name="us-east-1")
    polly = session.client("polly")
    response = polly.synthesize_speech( Text=ssmlText,
                                        Engine = "neural",
                                        TextType = "ssml",
                                        OutputFormat="mp3",
                                        VoiceId=myVoiceId)
    s3 = session.resource('s3')
    bucket_name = "dart-store"
    bucket = s3.Bucket(bucket_name)
    filename = "narration/concepts/" + filename
    stream = response["AudioStream"]
    bucket.put_object(Key=filename, Body=stream.read())

def generateSpeechMarksUsingSSML(ssmlText, filename, myVoiceId):
    # Generate audio using Text
    session = Session(region_name="us-east-1")
    polly = session.client("polly")
    response = polly.synthesize_speech( Text=ssmlText,
                                        Engine = "neural",
                                        TextType = "ssml",
                                        OutputFormat="json",
                                        SpeechMarkTypes=["sentence","word"],
                                        VoiceId=myVoiceId)
    s3 = session.resource('s3')
    bucket_name = "dart-store"
    bucket = s3.Bucket(bucket_name)
    filename = "narration/concepts/" + filename
    stream = response["AudioStream"]
    bucket.put_object(Key=filename, Body=stream.read())

def lambda_handler(event, context):

    avatars = ["intrepid", "daring", "valiant"]
    voice_ids = ["Ruth", "Danielle", "Matthew"]

    for avatar, myVoiceId in zip(avatars, voice_ids):
        # Challenge Intro
        generateAudioUsingSSML('<speak>Let\'s begin the identity theft challenge. It will take around 5 minutes to complete.<break time="1000ms"/>Find out your Identity Theft Resilience Score!<break time="500ms"/>DART HQ has gathered a variety of suspicious messages. Your task? Differentiate between what’s genuine and what\'s a scam. Take this to assess your current knowledge and earn your first badge!<break time="500ms"/>Click the \'Next\' button below to start the challenge.</speak>', f'intro_{avatar}.mp3', myVoiceId)

        generateSpeechMarksUsingSSML('<speak>Let\'s begin the identity theft challenge. It will take around 5 minutes to complete.<break time="1000ms"/>Find out your Identity Theft Resilience Score!<break time="500ms"/>DART HQ has gathered a variety of suspicious messages. Your task? Differentiate between what’s genuine and what\'s a scam. Take this to assess your current knowledge and earn your first badge!<break time="500ms"/>Click the \'Next\' button below to start the challenge.</speak>', f'intro_{avatar}.json', myVoiceId)

    return {
        'statusCode': 200,
        'body': json.dumps('Successful Generation using AWS Polly! Your audio files are so good, even Beyoncé is taking notes.')
    }
