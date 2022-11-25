import json
from newMaster import masterList
import re

# newMaster = {}
# for courseCode, info in masterList.items():
#   newCode = courseCode.replace(" ", "").lower()[:-2]
#   newMaster[newCode] = info

# with open("newMaster.json", "w") as outfile:
#   json.dump(newMaster, outfile, indent=2)

reviewDic = {}
with open("./reviews.json", "r") as infile:
  reviewDic = json.load(infile)


reviews = {}
for code, course in masterList.items():
  courseReviews = []
  profs = set()
  for time in course["times"]:
    if time["professorName"] not in profs and time["professorName"] in reviewDic:
      courseReviews += reviewDic["professorName"]
  
  reviews[course["masterCourseCode"]] = courseReviews

with open("MatchedReviews.json", "w") as outfile:
    json.dump(reviews, outfile, indent=2)
  
# matchedClasses = {}
# unMatchedClasses = {}

# for courseCode, reviews in reviewDic.items():
#   if courseCode.lower() in masterList:
#     realCourseCode = masterList[courseCode.lower()]["masterCourseCode"]
#     matchedClasses[realCourseCode] = reviews
#   else:
#     unMatchedClasses[courseCode] = reviews

# print("len matched classes", len(matchedClasses))
# print("len unmacthed", len(unMatchedClasses))

# with open("MatchedReviews.json", "w") as outfile:
#     json.dump(matchedClasses, outfile, indent=2)

# with open("UnmatchedReviews.json", "w") as outfile:
#     json.dump(unMatchedClasses, outfile, indent=2)