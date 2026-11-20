# Question 4: Paragraph Analysis

paragraph = """
Qlith Innovation is an excellent place to learn Python programming.
The teaching methods are very effective, and concepts are explained in a simple and easy-to-understand way.
Prakash Sir is a very knowledgeable, supportive, and dedicated mentor who always encourages students to learn and improve their programming skills.
He explains every topic clearly and makes learning Python interesting and enjoyable.
I am really happy to be learning Python at Qlith Innovation under the guidance of Prakash Sir.
"""

with open("article.txt", "w") as file:
    file.write(paragraph)

with open("article.txt", "r") as file:
    data = file.read()

print("Article:")
print(data)

characters = len(data)
words = len(data.split())
lines = len(data.splitlines())

print("Total Characters:", characters)
print("Total Words:", words)
print("Total Lines:", lines)