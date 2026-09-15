import re
text = "Hello world. This is a test."
result = re.split(r'(\s)', text)
result2 = re.split(r'([,.]|\s)', text)
print(result)
print(result2)