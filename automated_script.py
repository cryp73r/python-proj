from PIL import Image
import requests

unit = 'unit3'

image_data = []
url = 'http://d3q0zgweec1uok.cloudfront.net/notes/COA_aktu_kiet_notes_' + unit + '_2_pipelining-0001.jpg'
temp = Image.open(requests.get(url, stream=True).raw)
start = temp.convert('RGB')
print('Getting Image Data...\n')
for i in range(2, 1000):
    try:
        if i<10:
            url = 'http://d3q0zgweec1uok.cloudfront.net/notes/COA_aktu_kiet_notes_' + unit + '_2_pipelining-000' + str(i) + '.jpg'
            temp = Image.open(requests.get(url, stream=True).raw)
        elif i>=10 and i<100:
            url = 'http://d3q0zgweec1uok.cloudfront.net/notes/COA_aktu_kiet_notes_' + unit + '_2_pipelining-00' + str(i) + '.jpg'
            temp = Image.open(requests.get(url, stream=True).raw)
        else:
            url = 'http://d3q0zgweec1uok.cloudfront.net/notes/COA_aktu_kiet_notes_' + unit + '_2_pipelining-0' + str(i) + '.jpg'
            temp = Image.open(requests.get(url, stream=True).raw)
        temp_conv = temp.convert('RGB')
        image_data.append(temp_conv)
        print('\rImage: ' + str(i), end='')
    except:
        break

print('\n\nConverting to PDF...')
start.save(r'C:/Users/Priyanshu Singh/Desktop/New folder/COA Unit-3b Notes.pdf', save_all=True, append_images=image_data)

