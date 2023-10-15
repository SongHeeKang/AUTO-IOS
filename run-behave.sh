#!/bin/sh
LOCAL_PATH=$(pwd)
echo $LOCAL_PATH/reports/allureReports
behave  -f  allure_behave.formatter:AllureFormatter -o $LOCAL_PATH/reports/allureReports
