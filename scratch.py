'''
a=['https://ieltsfever.org/wp-content/uploads/2016/05/ieltsfever-academic-reading-practice-test-26-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/01/ieltsfever-academic-reading-practice-test-27-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2016/11/ieltsfever-academic-reading-practice-test-28-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/01/ieltsfever-academic-reading-practice-test-29-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/01/ieltsfever-academic-reading-practice-test-30-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/01/ieltsfever-academic-reading-practice-test-31-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/11/ieltsfever-academic-reading-practice-test-32-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/11/ieltsfever-academic-reading-practice-test-33-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/11/ieltsfever-academic-reading-practice-test-34-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/01/ieltsfever-academic-reading-practice-test-35-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/10/ieltsfever-academic-reading-practice-test-36-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/10/ieltsfever-academic-reading-practice-test-37-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/10/ieltsfever-academic-reading-practice-test-38-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/10/ieltsfever-academic-reading-practice-test-39-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/10/ieltsfever-academic-reading-practice-test-40-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/10/ieltsfever-academic-reading-practice-test-41-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/11/ieltsfever-academic-reading-practice-test-42-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/11/IELTSFEVER-ACADEMIC-READING-PRACTCIE-TEST-43-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/11/IELTSFEVER-ACADEMIC-READING-PRACTCIE-TEST-44-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/11/IELTSFEVER-ACADEMIC-READING-PRACTCIE-TEST-45-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/11/IELTSFEVER-ACADEMIC-READING-PRACTCIE-TEST-46-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/11/IELTSFEVER-ACADEMIC-READING-PRACTCIE-TEST-47-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/11/IELTSFEVER-ACADEMIC-READING-PRACTCIE-TEST-48-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/11/IELTSFEVER-ACADEMIC-READING-PRACTCIE-TEST-49-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/11/IELTSFEVER-ACADEMIC-READING-PRACTCIE-TEST-50-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/11/ieltsfever-academic-reading-practice-test-51-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/11/ieltsfever-academic-reading-practice-test-52-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/11/ieltsfever-academic-reading-practice-test-53-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/11/ieltsfever-academic-reading-practice-test-54-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/11/ieltsfever-academic-reading-practice-test-55-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2017/11/ieltsfever-academic-reading-practice-test-56-pdf.pdf',
'https://ieltsfever.org/wp-content/uploads/2018/10/Academic-reading-practice-test-57-PDF.pdf',
'https://ieltsfever.org/wp-content/uploads/2018/10/IELTSFEVER-AACADEMIC-READING-TEST-58.pdf',
'https://ieltsfever.org/wp-content/uploads/2018/11/academic-reading-test-59.pdf',
'https://ieltsfever.org/wp-content/uploads/2018/11/academic-reading-test-60.pdf',
'https://ieltsfever.org/wp-content/uploads/2018/11/academic-reading-test-61.pdf',
'https://ieltsfever.org/wp-content/uploads/2018/12/academic-reading-test-62.pdf',
'https://ieltsfever.org/wp-content/uploads/2019/01/academic-reading-test-63.pdf',
'https://ieltsfever.org/wp-content/uploads/2019/01/academic-reading-test-64.pdf',
'https://ieltsfever.org/wp-content/uploads/2019/02/academic-reading-test-65.pdf',
'https://ieltsfever.org/wp-content/uploads/2019/02/academic-reading-test-66.pdf',
'https://ieltsfever.org/wp-content/uploads/2019/03/ACADEMIC-READING-67.pdf',
'https://ieltsfever.org/wp-content/uploads/2019/04/Academic-Reading-68.pdf',
'https://ieltsfever.org/wp-content/uploads/2019/04/Academic-Reading-69.pdf',
'https://ieltsfever.org/wp-content/uploads/2019/05/academic-reading-70.pdf',
'https://ieltsfever.org/wp-content/uploads/2021/06/Reading-Test-71.pdf',
'https://ieltsfever.org/wp-content/uploads/2019/06/academic-reading-72.pdf,'
'https://ieltsfever.org/wp-content/uploads/2019/06/academic-reading-73.pdf,'
'https://ieltsfever.org/wp-content/uploads/2019/06/academic-reading-74.pdf,'
'https://ieltsfever.org/wp-content/uploads/2019/07/academic-reading-75.pdf']



# Import libraries
import requests
from bs4 import BeautifulSoup

# URL from which pdfs to be downloaded
url = 'https://ieltsfever.org/wp-content/uploads/2018/11/academic-reading-test-59.pdf'

# Requests URL and get response object
response = requests.get(url)

# Parse text obtained
soup = BeautifulSoup(response.text, 'html.parser')

# Find all hyperlinks present on webpage
links = soup.find_all('a')

i = 0

# From all links check for pdf link and
# if present download file
for link in links:
	if ('.pdf' in link.get('href', [])):
		i += 1
		print("Downloading file: ", i)

		# Get response object for link
		response = requests.get(link.get('href'))

		# Write content in pdf file
		pdf = open("pdf"+str(i)+".pdf", 'wb')
		pdf.write(response.content)
		pdf.close()
		print("File ", i, " downloaded")

print("All PDF files downloaded")


import urllib.request

pdf_path = 'https://ieltsfever.org/wp-content/uploads/2018/11/academic-reading-test-59.pdf'
download_url=''

def download_file(download_url, filename):
	response = urllib.request.urlopen(download_url)
	file = open(filename + ".pdf", 'wb')
	file.write(response.read())
	file.close()


download_file(pdf_path, "Test")
'''

import os
import requests

urls=["https://ieltsfever.org/wp-content/uploads/2019/08/academic-reading-76.pdf",
"https://ieltsfever.org/wp-content/uploads/2019/08/academic-reading-77.pdf",
"https://ieltsfever.org/wp-content/uploads/2019/09/academic-reading-78.pdf",
"https://ieltsfever.org/wp-content/uploads/2021/06/Academic-Reading-79.pdf",
"https://ieltsfever.org/wp-content/uploads/2021/06/IELTS-Reading-Test-80.pdf",
"https://ieltsfever.org/wp-content/uploads/2021/06/Academic-IELTS-Reading-Test-81.pdf",
"https://ieltsfever.org/wp-content/uploads/2021/06/Academic-IELTS-Reading-Test-82.pdf",
"https://ieltsfever.org/wp-content/uploads/2021/06/Acdemic-IELTS-Reading-Test-83.pdf",
"https://ieltsfever.org/wp-content/uploads/2021/06/Acdemic-IELTS-Reading-Test-84.pdf",
"https://ieltsfever.org/wp-content/uploads/2021/06/Acdemic-IELTS-Reading-Test-85.pdf",
"https://ieltsfever.org/wp-content/uploads/2021/06/Acdemic-IELTS-Reading-Test-86.pdf",
"https://ieltsfever.org/wp-content/uploads/2021/06/Acdemic-IELTS-Reading-Test-87.pdf",
"https://ieltsfever.org/wp-content/uploads/2021/06/Acdemic-IELTS-Reading-Test-88.pdf",
"https://ieltsfever.org/wp-content/uploads/2021/06/Acdemic-IELTS-Reading-Test-89.pdf",
"https://ieltsfever.org/wp-content/uploads/2021/06/Acdemic-IELTS-Reading-Test-90.pdf",
"https://ieltsfever.org/wp-content/uploads/2021/06/Academic-IELTS-Reading-Test-91.pdf",
"https://ieltsfever.org/wp-content/uploads/2021/06/Academic-IELTS-Reading-Test-92.pdf",
"https://ieltsfever.org/wp-content/uploads/2021/06/Academic-IELTS-Reading-Test-93.pdf",
"https://ieltsfever.org/wp-content/uploads/2021/06/Academic-IELTS-Reading-Test-94.pdf",
"https://ieltsfever.org/wp-content/uploads/2021/06/Academic-IELTS-Reading-Test-95.pdf",
"https://ieltsfever.org/wp-content/uploads/2021/06/Academic-IELTS-Reading-Test-96.pdf",
"https://ieltsfever.org/wp-content/uploads/2021/06/Academic-IELTS-Reading-Test-97.pdf",
"https://ieltsfever.org/wp-content/uploads/2021/06/Academic-IELTS-Reading-Test-99.pdf",
"https://ieltsfever.org/wp-content/uploads/2021/06/Academic-IELTS-Reading-Test-100.pdf"]
print(len(urls))
output_dir='E:\paf_tyest1'

for url in urls:
	res =requests.get(url)
	if res.status_code == 200:
		file_path =os.path.join(output_dir,os.path.basename(url))
		with open(file_path,'wb') as f:
			f.write(res.content)



