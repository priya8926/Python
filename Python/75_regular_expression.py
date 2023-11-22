import re

# pattern = "Software"
pattern = r"[A-Z]oftware"
text = '''Wayfair Software Engineering Internship Challenge – 2024*
Dear Campus Representative, 

The Wayfair Software Engineering Internship Challenge 2024 is here. It's a 6-month opportunity for B.Tech students, starting in January 2024. Here are the key details:

*Company:* Wayfair TDC *Location: Bengaluru (On-Site)* Doftware

*Stipend:* INR 75,000 per month

*Eligibility:* 2024 graduating batch in Computer Science or related field

*Registration Link:* https://www.firstnaukri.com/contests/wt-6530ec1f6efc8b758e5eba9f?utm_source=campusnet&utm_medium=Whatsapp&utm_campaign=wayfair&utm_id=wayfair

*Registration Deadline:* 3rd Nov 2024 (7:00 PM)
 Poftware voftware
*Test Date:* 3rd Nov 2024 (7:00 PM - 8:00 PM)

Share opportunity with eligible & interested campus students.

'''

# match = re.search(pattern , text)
# print(match)

matches = re.finditer(pattern , text)

for match in matches:
    print(match)