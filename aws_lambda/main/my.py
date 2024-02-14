import json
from boto3 import Session

def generateAudioUsingText(plainText, filename):
    # Generate audio using Text
    session = Session(region_name="us-east-1")
    polly = session.client("polly")

    # Use "json" as the output format to support SpeechMarks
    response = polly.synthesize_speech(
        Text=plainText,
        Engine="neural",
        TextType="text",
        OutputFormat="mp3",  # Change this to "mp3"
        VoiceId="Danielle"
    )

    # Extract SpeechMarks from the response
    speech_marks = polly.get_speech_marks(
        OutputFormat="json",
        Text=plainText,
        SpeechMarkTypes=["sentence", "word"],
        VoiceId="Danielle"
    )

    s3 = session.resource('s3')
    bucket_name = "dart-store"

    # Save SpeechMarks to a file
    speech_marks_filename = "narration/concepts/" + filename.replace('.mp3', '-speechmarks.json')
    bucket = s3.Bucket(bucket_name)
    bucket.put_object(Key=speech_marks_filename, Body=json.dumps(speech_marks))

    # Save MP3 file to S3
    filename = "narration/concepts/" + filename
    stream = response["AudioStream"]
    bucket.put_object(Key=filename, Body=stream.read())

# Rest of the code remains unchanged

def generateAudioUsingSSML(ssmlText, filename):
    # Generate audio using Text
    session = Session(region_name="us-east-1")
    polly = session.client("polly")

    # Use "json" as the output format to support SpeechMarks
    response = polly.synthesize_speech(
        Text=ssmlText,
        Engine="neural",
        TextType="ssml",
        OutputFormat="mp3",  # Change this to "mp3"
        VoiceId="Danielle"
    )

    # Extract SpeechMarks from the response
    speech_marks = polly.get_speech_marks(
        OutputFormat="json",
        Text=ssmlText,
        SpeechMarkTypes=["sentence", "word"],
        VoiceId="Danielle"
    )

    s3 = session.resource('s3')
    bucket_name = "dart-store"

    # Save SpeechMarks to a file
    speech_marks_filename = "narration/concepts/" + filename.replace('.mp3', '-speechmarks.json')
    bucket = s3.Bucket(bucket_name)
    bucket.put_object(Key=speech_marks_filename, Body=json.dumps(speech_marks))

    # Save MP3 file to S3
    filename = "narration/concepts/" + filename
    stream = response["AudioStream"]
    bucket.put_object(Key=filename, Body=stream.read())

def lambda_handler(event, context):
    # Generate audio using Text
    generateAudioUsingText('Leave it better than you found it', 'marks-demo.mp3')

    # Generate audio using SSML
    generateAudioUsingSSML('<speak>If everyone does a little bit <break time="1000ms"/> it adds up to a lot</speak>', 'ssml-marks-demo.mp3')

    return {
        'statusCode': 200,
        'body': json.dumps('Successful Generation of Audio File(s) using AWS Polly')
    }
