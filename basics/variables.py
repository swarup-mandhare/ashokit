# num1 = 200      ...single
# num2 = 300      ...single
# num1, num2 = 200, 300  ... single line initialization
# num1 = num2 = 200      ... same line initialization
# add = num1 + num2
# print ("Addition", add)
# print (type(add))

# multi line string (""" """)
name = "AshokIT"
address = "Hyderabad"
course= 'AI'
msg = """
ML - Machine Learning
DL - Deep Learning
NLP - Natural Language Processing
Gen AI - Generative AI
Agents - Agentic AI
Fine Tuning
RAG
MCP
LLMS
"""
print(msg)


numbers = [100, 200, 300, 400]
print(numbers)
print(type(numbers))
print(numbers[0])
print(numbers[-2], numbers[3])   # negative and positive index accessing
print(numbers[0:3])              # slicing
print(numbers[-3:-1])            # negative slicing
print(numbers [:4])              # internally converts to [0:4]
