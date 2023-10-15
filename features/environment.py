import base64
import os
from appium import webdriver
import time

import utilities.CustomLogger as cl

logger = cl.custom_logger()
BASE_DIR = os.getcwd()
URL = 'http://192.168.2.36:4723/wd/hub'
apps = 'FaceSDKProSample.ipa' # for iOS
app = os.path.join(BASE_DIR, 'apps', apps)

print("baseDir = " + BASE_DIR)
print("app = " + app)

def before_feature(context, feature):
    capabilities = {
                "app": app,
                "platformName": "ios",
                "appium:platformVersion": "16.2",
                "appium:automationName": "XCUITest",
                "appium:udid": "00008110-001615203402401E",
                "appium:bundleId": "com.alcherainc.app.FaceSDKProSample",
                "appium:xcodeOrgId": "G476VT3T47",
                "autoAcceptAlerts": "true",
                "appium: xcodeSigningId": "iPhone Developer"
            }

    context.driver = webdriver.Remote(command_executor=URL, desired_capabilities=capabilities)
    start_recoding(context)

    context = Scenario("feature_file.feature", "Scenario: Launch app and perform some action")
    context._runner = Scenario.runner
    context._feature = Scenario.feature
    context.tags = tag
    context.run()

def after_feature(context,feature):
    stop_recoding(context)
    context.driver.quit()

def start_recoding(context):
    context.driver.start_recording_screen(videoType='h264', videoQuality='high')        
    logger.info("Recoding Start")

def stop_recoding(context):
    raw_video_data = context.driver.stop_recording_screen()
    video_file_name = f'{time.strftime("%Y%m%d_%H%M%S")}_.mp4'
    video_file_path = os.path.join(BASE_DIR+"/reports", "["+ "ios" + "]"+ "-" + video_file_name)
    with open(video_file_path, "wb") as fd:
      fd.write(base64.b64decode(raw_video_data))
    logger.info("Recoding Stop")
