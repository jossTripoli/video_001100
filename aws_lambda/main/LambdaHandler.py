import json
from boto3 import Session

folder = "challenge/"

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
    filename = "narration/" + folder + filename
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
    filename = "narration/" + folder + filename
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
    filename = "narration/" + folder + filename
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
    filename = "narration/" + folder + filename
    stream = response["AudioStream"]
    bucket.put_object(Key=filename, Body=stream.read())

def lambda_handler(event, context):

    avatars = ["intrepid", "daring", "valiant"]
    voice_ids = ["Ruth", "Danielle", "Matthew"]

    for avatar, myVoiceId in zip(avatars, voice_ids):
        # Challenge Intro
        # generateAudioUsingSSML('<speak>Let\'s begin the identity theft challenge. It will take around 5 minutes to complete.<break time="1000ms"/>Find out your Identity Theft Resilience Score!<break time="500ms"/>DART HQ has gathered a variety of suspicious messages. Your task? Differentiate between what’s genuine and what\'s a scam. Take this to assess your current knowledge and earn your first badge!<break time="500ms"/>Click the \'Next\' button below to start the challenge.</speak>', f'intro_{avatar}.mp3', myVoiceId)

        # generateSpeechMarksUsingSSML('<speak>Let\'s begin the identity theft challenge. It will take around 5 minutes to complete.<break time="1000ms"/>Find out your Identity Theft Resilience Score!<break time="500ms"/>DART HQ has gathered a variety of suspicious messages. Your task? Differentiate between what’s genuine and what\'s a scam. Take this to assess your current knowledge and earn your first badge!<break time="500ms"/>Click the \'Next\' button below to start the challenge.</speak>', f'intro_{avatar}.json', myVoiceId)
        
        # # Challenge quiz 
        # text_source = """
        #     Quiz question 1. Suppose you’ve been experiencing issues with your Apple laptop and have been in contact with Apple. In this scenario, would you consider the following email a scam?

        #     Hover over or click the sender to view email details.

        #     The email’s subject is "Customer Support Follow-up". Its sender is Apple Support.

        #     Thank you for contacting Apple Customer Service. We understand that you're facing some issues, and we're here to help!

        #     Could you please provide us with more details about the problem you're experiencing? This will help us better understand the situation and provide you with the appropriate solution.

        #     Thank you,

        #     Sarah (she/her)

        #     iTunes Store Customer Support

        #     Select "yes" if you think this email is a scam or "no" if you think it isn't a scam. Then click the blue "Next Question" button to continue.
        #     """
        
        # Challenge quiz-2
        # text_source = """
        #     Question 2. If you received the following email, would you consider it a scam?

        #     The email’s subject is: Your account on the verge of closure! Its sender is PayPal Support.

        #     Dear Client,

        #     Recently, your account was reviewed and flagged because of a potential connection to some fraudulent transactions. To avoid an eventual restriction to your account, please verify your informations by logging in to our Litigations Manager.

        #     At the end of the email there is a large button that says "check my account".
        #     """
        
        # generateAudioUsingText(text_source, f'quiz-2_{avatar}.mp3', myVoiceId)
        # generateSpeechMarksUsingText(text_source, f'quiz-2_{avatar}.json', myVoiceId)
        
        
        # # Challenge quiz-3
        # text_source = """
        #     Question 3.  If you received the following message, would you consider it a scam?

        #     ATM/CHECK-card is SUSPENDED! Please
        #     Continue www.bofa.com/support.bofa.com.htm
        #     """
        
        # generateAudioUsingText(text_source, f'quiz-3_{avatar}.mp3', myVoiceId)
        # generateSpeechMarksUsingText(text_source, f'quiz-3_{avatar}.json', myVoiceId)
        
        
        # # Challenge quiz-4
        # text_source = """
        #     Question 4. Assuming you are trying to log into Venmo following the instruction for the Venmo App, then you received the message below. In that case, would you consider this message a scam?

        #     Venmo here! NEVER share your code via call/text. ONLY YOU should enter this code. BEWARE: if someone asks for the code, it's a scam. Code: 5-6-8-6-0-1.
        #     """
        
        # generateAudioUsingText(text_source, f'quiz-4_{avatar}.mp3', myVoiceId)
        # generateSpeechMarksUsingText(text_source, f'quiz-4_{avatar}.json', myVoiceId)


        # Challenge quiz-5
        text_source = """
            Question 5. What could occur if your identity is stolen? Select all that apply.
            
            A: Loss of money.
            B: Loss of tax refund.
            C: Be charged as a criminal.
            D: Denial of loans.
            E: Getting a discount on online shopping.
            """
        
        generateAudioUsingText(text_source, f'quiz-5_{avatar}.mp3', myVoiceId)
        generateSpeechMarksUsingText(text_source, f'quiz-5_{avatar}.json', myVoiceId)


        # Challenge badge
        text_source = """
            Congratulations!
            You've completed the Challenge and earned a bronze badge!
            
            You have an Identity Theft Resilience score shown here.
            
            To build your resilience and earn more badges, continue to the next section.
            """
        
        generateAudioUsingText(text_source, f'badge_{avatar}.mp3', myVoiceId)
        generateSpeechMarksUsingText(text_source, f'badge_{avatar}.json', myVoiceId)

        
    return {
        'statusCode': 200,
        'body': json.dumps('Successful Generation using AWS Polly! Your audio files are so good, even Beyoncé is taking notes.')
    }
