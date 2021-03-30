from bs4 import BeautifulSoup
import requests

# get the webpage
w  = requests.get("https://www.wired.com/story/geoengineering-is-the-only-solution-to-our-climate-calamities/")
n  = requests.get("https://www.nature.org/en-us/what-we-do/our-insights/perspectives/natural-solutions-to-climate-change/")
g  =  requests.get("https://www.theguardian.com/environment/climate-change")
l = requests.get("https://www.ladyscience.com/features/why-we-need-a-feminist-climate-science-and-how-we-might-get-it")

# get the HTML source from that page
html_doc_w = w.text
html_doc2_n = n.text
html_doc3_g = g.text
html_doc4_l = l.text

# turn the source into a bs4 "soup" object
soup_w = BeautifulSoup(html_doc_w, features="html.parser")
soup_n = BeautifulSoup(html_doc2_n, features="html.parser")
soup_g = BeautifulSoup(html_doc3_g, features="html.parser")
soup_l = BeautifulSoup(html_doc4_l, features="html.parser")

# narrow down to the block of html that contains our content
headline_w = soup_w.find("h1")
headline_n = soup_n.find("h1")
headline_g = soup_g.find("h1")
headline_l = soup_l.find("h2")

# get the span that has the actual headline
heading_text_w = headline_w.get_text()
heading_text_n = headline_n.get_text()
heading_text_g = headline_g.get_text()
heading_text_l = headline_l.get_text()

# remove any line breaks
heading_text_w = heading_text_w.replace('\n',' ')
heading_text_n = heading_text_n.replace('\n',' ')
heading_text_g = heading_text_g.replace('\n',' ')
heading_text_l = heading_text_l.replace('\n',' ')
# print(heading_text1)
# print(heading_text2)

# capitalize first letter of each word
heading_text_w_cap = heading_text_w.title()

#capitalize first letter of each word
heading_text_l_cap = heading_text_l.title()

# remove the date from ladyscience.com title
heading_text_l_cap = heading_text_l_cap[6:]

# select first climate change article from guardian.com
climate_change_article_1 = soup_g.find(class_="fc-item__container")

# select title
climate_change_article_1_title = climate_change_article_1.find(class_ = "js-headline-text")

# select article text
climate_change_article_1_text = climate_change_article_1_title.get_text()

# select content from ladyscience.com article
content_l = soup_l.find(class_="col sqs-col-12 span-12")

# select all paragraph from ladyscience.com article
all_paragraph_l = content_l.find(class_="sqs-block-content")

# select paragraph from ladyscience.com article
paragraph_l = all_paragraph_l("p")[3]

# select on the text from paragraph from ladyscience.com article
paragraph_l = paragraph_l.get_text()

# select all paragraphs from Wired.com article
all_paragraphs_w = soup_w.find(class_="article__chunks")

# select the fourth paragraph from Wired.com article
paragraph_w_4 = all_paragraphs_w("p")[3]

# select only the text from the fourth paragraph
paragraph_text_w_4 = paragraph_w_4.get_text()
# print(paragraph_text)

# remove any line breaks
paragraph_text_w_4 = paragraph_text_w_4.replace('\n',' ')

# image from Wired.com article
image_w = soup_w.find("picture", class_="lead-asset__media responsive-image")
image_src_w = image_w.find("img")["src"]
# print(image_src)

#image from Nature.org article
image_link_n = soup_n.find(class_ = "triggerModal")
image_n = image_link_n.find("picture")
image_src_n = image_n.find("img")["src"]
# print(image_src2)

# select all all paragraphs from Nature.org article
all_sections_n = soup_n.find(class_ = "template-body-container")

# select the first section from the Nature.org article
section_n_1 = all_sections_n(class_ = "rich-text-editor base-component")[0]

# select the second section from Nature.org article
section_n_2 = all_sections_n(class_ = "rich-text-editor base-component")[1]

# select all paragraphs from second section
all_paragraphs_n_2 = section_n_2 ("p")

# select all paragraphs from the first section
all_paragraphs_n_1 = section_n_1 ("p")

# select the first paragraph from the second section
paragraph_n_2_1 = all_paragraphs_n_2 [0]

# select the third paragraph from the first section
paragraph_n_1_3 = all_paragraphs_n_1 [2]

# select only the text from first paragraph
paragraph_text_n_2_1 = paragraph_n_2_1.get_text()

# select only the text from third paragraph
paragraph_text_n_1_3 = paragraph_n_1_3.get_text()

# break the third paragraph into sentences
all_sentences_n_1_3 = (paragraph_text_n_1_3.split(". "))

# select the first sentence from the third paragraph
sentence_n_1_3_1 = all_sentences_n_1_3 [0]

# first 100 charcters in the sentence
sentence_characters = sentence_n_1_3_1[8:103]

# capitalize first letter of each word
sentence_characters_cap = sentence_characters.title()

# Open and read the html template file
fo = open("template.html", "r")
html_template = fo.read();
fo.close()

# merge the html template with the scraped data
html_file = html_template.format(heading_text_w_cap, image_src_w, paragraph_text_w_4, sentence_characters_cap, image_src_n, paragraph_text_n_2_1, paragraph_text_n_1_3, heading_text_g, heading_text_l_cap, paragraph_l, climate_change_article_1_text)

# make the html look nice with indents, etc.
html_file = BeautifulSoup(html_file, features="html.parser").prettify(formatter="html")

# write out the html file
fo = open("climate_change.html", "w")
fo.write( html_file );
fo.close()
