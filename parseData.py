import json
from newMaster import masterList
import re

# newMaster = {}
# for courseCode, info in masterList.items():
#   newCode = courseCode.replace(" ", "").lower()[:-2]
#   newMaster[newCode] = info

# with open("newMaster.json", "w") as outfile:
#   json.dump(newMaster, outfile, indent=2)

def matchClasses(reviewDic):
  matchedClasses = {}
  unMatchedClasses = {}

  for courseCode, reviews in reviewDic.items():
    if courseCode.lower() in masterList:
      realCourseCode = masterList[courseCode.lower()]["masterCourseCode"]
      matchedClasses[realCourseCode] = reviews
    else:
      unMatchedClasses[courseCode] = reviews

  print("len matched classes", len(matchedClasses))
  print("len unmacthed", len(unMatchedClasses))

  with open("MatchedReviews.json", "w") as outfile:
      json.dump(matchedClasses, outfile, indent=2)

  with open("UnmatchedReviews.json", "w") as outfile:
      json.dump(unMatchedClasses, outfile, indent=2)

def mapReviewsToProf(reviewDic):
  reviews = {}

  for course in masterList.values():
    courseReviews = []
    checkedProfs = set()

    for time in course["times"]:
      if (
        "professorName" in time and
        time["professorName"] not in checkedProfs and 
        time["professorName"] in reviewDic
        ):
        courseReviews += reviewDic[time["professorName"]]
        checkedProfs.add(time["professorName"])
    
    if len(courseReviews) > 0:
      reviews[course["masterCourseCode"]] = courseReviews

  with open("MatchedReviews.json", "w") as outfile:
    json.dump(reviews, outfile, indent=2)

if __name__ == '__main__':
  reviewDic = {}
  with open("./reviews.json", "r") as infile:
    reviewDic = json.load(infile)

  mapReviewsToProf(reviewDic)
