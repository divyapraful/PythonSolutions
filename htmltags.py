
PracticePythonRegex and ParsingDetect HTML Tags, Attributes and Attribute Values
Detect HTML Tags, Attributes and Attribute Values

5 more points to get your next star!
Rank: 354010|Points: 105/110
Python
Problem
Submissions
Leaderboard
Discussions
Editorial
You are given an HTML code snippet of  lines.
Your task is to detect and print all the HTML tags, attributes and attribute values.

Print the detected items in the following format:

Tag1
Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Tag3
-> Attribute3[0] > Attribute_value3[0]


The -> symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value.
The > symbol acts as a separator of attributes and attribute values.

If an HTML tag has no attribute then simply print the name of the tag.

Note: Do not detect any HTML tag, attribute or attribute value inside the HTML comment tags (<!-- Comments -->). Comments can be multiline.
All attributes have an attribute value.

Input Format

The first line contains an integer , the number of lines in the HTML code snippet.
The next  lines contain HTML code.

Constraints


Output Format

Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the snippet.

Format your answers as explained in the problem statement.

Sample Input

9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
Sample Output

head
title
object
-> type > application/x-flash
-> data > your-file.swf
-> width > 0
-> height > 0
param
-> name > quality
-> value > high
Explanation

head tag: Print the head tag only because it has no attribute.

title tag: Print the title tag only because it has no attribute.

object tag: Print the object tag. In the next  lines, print the attributes type, data, width and                     height along with their respective values.

<!-- Comment --> tag: Don't detect anything inside it.

param tag: Print the param tag. In the next  lines, print the attributes name along with                     their respective values.
Python 3



123456789101112131415171618
# Enter your code here. Read input from STDIN. Print output to STDOUT


from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        self.print_attrs(attrs)
    def handle_startendtag(self, tag, attrs):
        print(tag)
        self.print_attrs(attrs)
    def print_attrs(self, attrs):
        for elem in attrs:
            print("-> {:} > {:}".format(elem[0],elem[1]))
if __name__ == "__main__":
    parser = MyHTMLParser()
    for _ in range (int(input())):
        parser.feed(input())


Line: 18 Col: 29
Submit CodeRun Code
Upload Code as File
Test against custom input
Congratulations!

You have passed the sample test cases. Click the submit button to run your code against all the test cases.

Sample Test case 0
Input (stdin)
Download
9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash"
  data="your-file.swf"
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
Your Output (stdout)
head
title
object
-> type > application/x-flash
-> data > your-file.swf
-> width > 0
-> height > 0
param
-> name > quality
-> value > high
Expected Output
Download
head
title
object
-> type > application/x-flash
-> data > your-file.swf
-> width > 0
-> height > 0
param
-> name > quality
-> value > high
Author[deleted]
DifficultyEasy
Max Score30
Submitted By12019
NEED HELP?
View discussions
View editorial
View top submissions
RATE THIS CHALLENGE

MORE DETAILS
Download problem statement
Download sample test cases
Suggest Edits
Share on FacebookShare on TwitterShare on LinkedIn
Contest CalendarBlogScoringEnvironmentFAQAbout UsSupportCareersTerms Of ServicePrivacy PolicyRequest a Feature
input
