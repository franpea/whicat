from app import db, models
import datetime

k = models.Checklist(id=999, timestamp=datetime.datetime.utcnow())
db.session.add(k)
db.session.commit()

k = models.Checklist.query.get(999)

Q1 = models.Question(number=1, text="Are the aims of the website clear?", button1="Not clear", button2="Sort of clear", button3="Can't decide", button4="Mostly clear", button5="Very Clear", hint="<p>Does the website include a statement about:</p> <ul><li>what it is about</li><li>what topics it includes</li><li>who it is for?</li></ul><p>Does the website provide the information it aims to provide?</p>", example="<p>A good example is <a href='http://yfoundations.org.au/need-help/support-and-services/youth-health/' target='_blank'>yfoundations</a>. This website states that its aim is, 'to provide youth health sector support, through the Youth Health Council and by working with youth health practitioners across NSW.'</p>", set=k)
Q2 = models.Question(number=2, text="Is the website's domain name trustworthy?", button1="No", button2="Not really", button3="Can't decide", button4="Seems ok", button5="Yes", hint=" <p>Look at the website's URL (address), eg The University of Sydney is www.sydney.edu.au. The domain name follows the organisation's name. For example, in the University of Sydney's URL,  the organisation's name is 'sydney' and the domain name is 'edu'. 'au' means the organisation is in Australia.</p><p>A domain name tells you that there may be a conflict of interest, or potential bias, between the owner of the website and its content.</p>  <p>Common domain names are .gov, .org, .edu, .com and .net:</p><ul><li>.gov is for websites of hospitals, government organisations and non-profit organisations. These are normally trustworthy websites that help the public. They normally have little or no conflict of interest or bias.</li>  <li>.org is also for websites of hospitals, government organisations and non-profit organisations.   These are normally trustworthy websites that are for the public. They normally have little or no conflict of interest or bias.</li>  <li>.edu is for websites of universities, schools and other educational institutions. These are normally trustworthy sites that are for the public. They normally have little or no conflict of interest or bias.</li>  <li>.com is for websites of private, commercial companies that are usually for-profit. Some of these sites may have a conflict of interest or bias, but not necessarily.</li>  <li>.net is for companies involved in networking technologies. They are also a general purpose domain name for other websites. Some of these websites may have a conflict of interest or bias, but not necessarily.</li> </ul>", example="<ul><li>An example of a website with a <strong>.gov</strong> domain name is <a href='http://www.cdc.gov' target='_blank'>Centers for Disease Control and Prevention</a> (CDC). The CDC is a part of the United States of America's Department of Health and Human Services.</li> <li>An example of a website with a <strong>.org</strong> domain name is <a href='http://www.trapeze.org.au' target='_blank'>Trapeze</a>.</li> <li>An example of a website with a <strong>.edu</strong> domain name is <a href='http://www.sydney.edu.au' target='_blank'>Sydney University</a>.</li> <li>Examples of websites with a <strong>.com</strong> domain name include <a href='http://www.webmd.com' target='_blank'>WebMD</a> and <a href='http://www.reachout.com' target='_blank'>Reachout</a>.</li> <li>Examples of websites with a <strong>.net</strong> domain name include <a href='https://www.iinet.net.au' target='_blank'>iinet</a>, <a href='http://www.raisingchildren.net.au' target='_blank'>Raising Children</a> and the <a href='http://www.abc.net.au' target='_blank'>ABC</a>.</li> </ul>", set=k)
Q3 = models.Question(number=3, text="Are the authors qualified to give health information?", button1="Not qualified", button2="Partly qualified", button3="Can't decide", button4="Mostly qualified", button5="Well qualified", hint=" <p>Are they health professionals, such as doctors?</p> <p>Are they experienced? </p> <p> If an organisation is providing the information, is it a non-profit organisation? These organisations normally have little or no conflict of interest or bias.</p><p>Are the members of the organisation qualified health professionals?</p>", example=" <p>A good example is <a href='https://labtestsonline.org' target='_blank'>Lab tests online</a>. This website notes that, 'Laboratory and medical professionals, who are experts in the field, develop and review all content'.</p>", set=k)
Q4 = models.Question(number=4, text="Is it clear what sources of information were used to write the website's health information?", button1="Not clear", button2="Sort of clear", button3="Can't decide", button4="Mostly clear", button5="Very Clear", hint=" <p>Do the main statements include a reference to the sources of the information, eg research by many people or the opinions of more than one expert. </p> <p>If an expert's opinion is the source, can you see whether this person is qualified to give this information? Do they belong to a non-profit organisation with qualified health professionals?</p>", example="<p>A good example is the <a href='https://medlineplus.gov/woundsandinjuries.html' target='_blank'> US National Library of Medicine. </a>This is a government website providing information and results of research for consumers.</p>", set=k)
Q5 = models.Question(number=5, text="Is the information based on proven medical evidence?", button1="Not clear", button2="Sort of clear", button3="Can't decide", button4="Mostly clear", button5="Very Clear", hint="<p>Any medical or health claims must be based on proof. Proof can be</p><ul><li>Clinical guidelines from a relevant health department - these give directions to health professionals about how to treat patients</li><li>Journal articles about results from research - journal articles should be recent (preferably in the past 2 years and no more than 5 years) and journals should be high quality. Look for a journal with an Impact Factor that does not appear in a list of questionable journals such as Bealls List. </li></ul>", example="<p>A good example is the <a href='https://www.cdc.gov/about/organization/mission.html' target='_blank'>National Institute of Diabetes and Digestive and Kidney Diseases</a> (NIDDK) which states that the organisation bases 'all public health decisions on the highest quality scientific data that is derived openly and objectively'. It also states that it places 'the benefits to society above the benefits to our institution'.</p>", set=k)
Q6 = models.Question(number=6, text="Is the information up-to-date?", button1="Not clear", button2="Sort of clear", button3="Can't decide", button4="Mostly clear", button5="Very Clear", hint="<ul><li>Look at the dates of publication or copyright of the information. Also look at the dates of revisions.</li><li>Up-to-date information is less than five years old - the most up-to-date information is normally less than two years old.</li></ul>", example="<p>A good example is the <a href='https://www.kidney.org/atoz/content/know-your-kidney-numbers-two-simple-tests' target='_blank'> National Kidney Foundation</a> which provides revision dates.</p>", set=k)
Q7 = models.Question(number=7, text="Is the information balanced and unbiased? ", button1="Not clear", button2="Sort of clear", button3="Can't decide", button4="Mostly clear", button5="Very Clear", hint="<ul><li>Is the website neutral? Does it give information from an objective point of view, not a personal opinion?</li><li>Does the website support information with evidence?</li><li>Does the website write about a topic with more than one source of information, eg the research of many people or the opinions of more than one expert?</li><li>Does the website give the advantages and disadvantages of different types of treatment, not just one choice?</li><li>Is the information just and sensible, or is it emotional?</li></ul>", example="<p>A good example is the <a href='http://www.nhlbi.nih.gov/health/health-topics/topics/cf' target='_blank'>National Institutes of Health National Heart, Lung and Blood Institute</a> which is neutral and provides different types of treatment options.</p>", set=k)
Q8 = models.Question(number=8, text="Does the website's information match information from other sources?", button1="Not clear", button2="Sort of clear", button3="Can't decide", button4="Mostly clear", button5="Very Clear", hint="<ul><li>If possible, check the information with a website of a government or non-profit organisation.</li><li>Always ask for medical advice from a qualified health professional.</li></ul>", example="<p>A good example is the <a href='http://www.nhs.uk/conditions/depression/Pages/Introduction.aspx' target='_blank'>National Health Service's Choices website </a> which advises consumers to see their doctor if they think they have the condition described.</p>", set=k)
Q9 = models.Question(number=9, text="Does the website state who funds it?", button1="Not clear", button2="Sort of clear", button3="Can't decide", button4="Mostly clear", button5="Very Clear", hint="<ul><li>Websites from governments or non-profit organisations (eg public hospitals or universities) are for the public and are normally trustworthy.</li><li>Websites from private companies may give biased information.</li></ul>", example="<p>A good example is the <a href='http://www.healthday.com/purchase-health-news-articles.html' target='_blank'>HealthDay</a> which clearly states who pays for the website.</p>", set=k)
Q10 = models.Question(number=10, text="Is advertising clearly separate from website content?", button1="Not clear", button2="Sort of clear", button3="Can't decide", button4="Mostly clear", button5="Very Clear", hint="<ul><li>Advertising content is biased and not trustworthy.</li></ul>", example="<p>A good example is <a href='http://www.webmd.com/eye-health/default.html' target='_blank'>WebMD</a> which clearly labels advertisements.</p>", set=k)
Q11 = models.Question(number=11, text="Is there a seal of certification from a trusted organisation, such as <a href='https://www.hon.ch' target='_blank'>Health on the Net</a>?", button1="Not clear", button2="Sort of clear", button3="Can't decide", button4="Mostly clear", button5="Very Clear", hint="<ul><li>Seals of certification show that the website has up-to-date information that is supported by evidence. The website also states the sources of the information, who pays for the website and the authors' health qualifications, and separates website content from advertising.</li><li>Is the certification up-to-date?</li></ul>", example="<p>A good example is the <a href='http://www.mayoclinic.org' target='_blank'>Mayo Clinic</a> which has HON certification.</p>", set=k)
Q12 = models.Question(number=12, text="Based on the answers to all of these questions, do you think the website is trustworthy?", button1="Not clear", button2="Sort of clear", button3="Can't decide", button4="Mostly clear", button5="Very Clear", hint="", example="", set=k)

questions = (Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12)

						
for q in questions:
    db.session.add(q)
    db.session.commit()



W1 = models.Website(address="https://avn.org.au/independent-studies-on-vaccine-safety-in-general/", title="Independent studies on vaccine safety in general | Australian Vaccination-skeptics Network Inc.")
W2 = models.Website(address="http://healthinformationcompany.com/do-you-have-cravings-for-facebook", title="Do you have cravings for Facebook? | The Health Information Company")
W3 = models.Website(address="http://www.bodyandsoul.com.au/health/health-advice", title="Health Advice | Health Advice | body+soul")
W4 = models.Website(address="http://www.traveldoctor.com.au/Article/Alerts/Early-Rise-of-Dengue-in-Bangladesh", title="Early Rise of Dengue in Bangladesh")
W5 = models.Website(address="http://travelvaccines.com.au/travel-health-advice/insect-and-animal-bites", title="Tips for preventing insect and animal bites")
W6 = models.Website(address="http://www.healthline.com/health/working-too-much-health-effects", title="7 Health Effects of Working Too Much")
W7 = models.Website(address="http://www.govita.com.au/health/acne/", title="Acne - Go Vita Health Shops")
W8 = models.Website(address="https://www.dhsv.org.au/dental-advice/general-dental-advice/preschool-children", title="Dental advice for preschool children (3-5 years) - Dental Health Services Victoria")
W9 = models.Website(address="http://bendigoufs.com.au/the-flu-and-you/", title="The Flu and you | UFS Bendigo")
W10 = models.Website(address="http://healthinformationcompany.com/internet-games-and-body-image", title="Internet games and body image | The Health Information Company")
W11 = models.Website(address="http://www.webmd.com/women/features/women-top-health-tips#1", title="Top 10 Health Tips for Women")
W12 = models.Website(address="https://www.healthdirect.gov.au/", title="Trusted Health Advice | healthdirect")

websites = (W1,W2,W3,W4,W5,W6,W7,W8,W9,W10,W11,W12)

for w in websites:
	db.session.add(w)
	db.session.commit()

w = models.Website.query.get(1)

a = models.Assessment(answer1=2, answer2=2, answer3=1, answer4=2, answer5=4, answer6=2, answer7=3, answer8=3, answer9=2, answer10=3, answer11=3, answer12=4, url=w)
b = models.Assessment(answer1=1, answer2=1, answer3=1, answer4=1, answer5=1, answer6=1, answer7=1, answer8=1, answer9=1, answer10=1, answer11=1, answer12=1, url=w)
c = models.Assessment(answer1=2, answer2=2, answer3=2, answer4=2, answer5=2, answer6=2, answer7=2, answer8=2, answer9=2, answer10=2, answer11=2, answer12=2, url=w)
d = models.Assessment(answer1=2, answer2=2, answer3=1, answer4=2, answer5=4, answer6=2, answer7=3, answer8=3, answer9=2, answer10=3, answer11=3, answer12=4, url=w)
e = models.Assessment(answer1=1, answer2=1, answer3=1, answer4=1, answer5=1, answer6=1, answer7=1, answer8=1, answer9=1, answer10=1, answer11=1, answer12=1, url=w)
f = models.Assessment(answer1=2, answer2=2, answer3=2, answer4=2, answer5=2, answer6=2, answer7=2, answer8=2, answer9=2, answer10=2, answer11=2, answer12=2, url=w)
j = models.Assessment(answer1=2, answer2=2, answer3=2, answer4=2, answer5=2, answer6=2, answer7=2, answer8=2, answer9=2, answer10=2, answer11=2, answer12=2, url=w)
k = models.Assessment(answer1=4, answer2=4, answer3=5, answer4=5, answer5=5, answer6=4, answer7=2, answer8=5, answer9=4, answer10=3, answer11=4, answer12=5, url=w)
l = models.Assessment(answer1=2, answer2=1, answer3=3, answer4=2, answer5=1, answer6=3, answer7=5, answer8=3, answer9=2, answer10=1, answer11=2, answer12=2, url=w)
m = models.Assessment(answer1=1, answer2=2, answer3=1, answer4=3, answer5=2, answer6=1, answer7=2, answer8=3, answer9=1, answer10=1, answer11=2, answer12=1, url=w)
n = models.Assessment(answer1=2, answer2=3, answer3=2, answer4=1, answer5=2, answer6=2, answer7=2, answer8=3, answer9=2, answer10=1, answer11=2, answer12=2, url=w)
o = models.Assessment(answer1=2, answer2=2, answer3=1, answer4=2, answer5=4, answer6=2, answer7=3, answer8=3, answer9=2, answer10=3, answer11=3, answer12=4, url=w)
p = models.Assessment(answer1=1, answer2=1, answer3=1, answer4=1, answer5=1, answer6=1, answer7=1, answer8=1, answer9=1, answer10=1, answer11=1, answer12=1, url=w)
q = models.Assessment(answer1=2, answer2=2, answer3=2, answer4=2, answer5=2, answer6=2, answer7=2, answer8=2, answer9=2, answer10=2, answer11=2, answer12=2, url=w)

responses = (a,b,c,d,e,f,j,k,l,m,n,o,p,q)

for r in responses:
	db.session.add(r)
	db.session.commit()

w = models.Website.query.get(2)

d = models.Assessment(answer1=3, answer2=3, answer3=3, answer4=3, answer5=3, answer6=3, answer7=3, answer8=3, answer9=3, answer10=3, answer11=3, answer12=3, url=w)
e = models.Assessment(answer1=4, answer2=4, answer3=4, answer4=4, answer5=4, answer6=4, answer7=4, answer8=4, answer9=4, answer10=4, answer11=4, answer12=4, url=w)
f = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)
g = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)
h = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)
i = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)
j = models.Assessment(answer1=2, answer2=2, answer3=2, answer4=2, answer5=2, answer6=2, answer7=2, answer8=2, answer9=2, answer10=2, answer11=2, answer12=2, url=w)
k = models.Assessment(answer1=4, answer2=4, answer3=5, answer4=5, answer5=5, answer6=4, answer7=2, answer8=5, answer9=4, answer10=3, answer11=4, answer12=5, url=w)
l = models.Assessment(answer1=2, answer2=1, answer3=3, answer4=2, answer5=1, answer6=3, answer7=5, answer8=3, answer9=2, answer10=1, answer11=2, answer12=2, url=w)
m = models.Assessment(answer1=1, answer2=2, answer3=1, answer4=3, answer5=2, answer6=1, answer7=2, answer8=3, answer9=1, answer10=1, answer11=2, answer12=1, url=w)
n = models.Assessment(answer1=2, answer2=3, answer3=2, answer4=1, answer5=2, answer6=2, answer7=2, answer8=3, answer9=2, answer10=1, answer11=2, answer12=2, url=w)

responses = (d,e,f,g,h,i,j,k,l,m,n)

for r in responses:
	db.session.add(r)
	db.session.commit()

w = models.Website.query.get(3)

a = models.Assessment(answer1=2, answer2=2, answer3=1, answer4=2, answer5=4, answer6=2, answer7=3, answer8=3, answer9=2, answer10=3, answer11=3, answer12=4, url=w)
b = models.Assessment(answer1=1, answer2=1, answer3=1, answer4=1, answer5=1, answer6=1, answer7=1, answer8=1, answer9=1, answer10=1, answer11=1, answer12=1, url=w)
c = models.Assessment(answer1=2, answer2=2, answer3=2, answer4=2, answer5=2, answer6=2, answer7=2, answer8=2, answer9=2, answer10=2, answer11=2, answer12=2, url=w)
d = models.Assessment(answer1=3, answer2=3, answer3=3, answer4=3, answer5=3, answer6=3, answer7=3, answer8=3, answer9=3, answer10=3, answer11=3, answer12=3, url=w)
e = models.Assessment(answer1=4, answer2=4, answer3=4, answer4=4, answer5=4, answer6=4, answer7=4, answer8=4, answer9=4, answer10=4, answer11=4, answer12=4, url=w)
f = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)
g = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)
h = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)

responses = (a,b,c,d,e,f,g,h)

for r in responses:
	db.session.add(r)
	db.session.commit()

w = models.Website.query.get(4)

a = models.Assessment(answer1=2, answer2=2, answer3=1, answer4=2, answer5=4, answer6=2, answer7=3, answer8=3, answer9=2, answer10=3, answer11=3, answer12=4, url=w)
c = models.Assessment(answer1=2, answer2=2, answer3=2, answer4=2, answer5=2, answer6=2, answer7=2, answer8=2, answer9=2, answer10=2, answer11=2, answer12=2, url=w)
e = models.Assessment(answer1=4, answer2=4, answer3=4, answer4=4, answer5=4, answer6=4, answer7=4, answer8=4, answer9=4, answer10=4, answer11=4, answer12=4, url=w)
g = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)

responses = (a,c,e,g)

for r in responses:
	db.session.add(r)
	db.session.commit()

w = models.Website.query.get(5)

a = models.Assessment(answer1=2, answer2=2, answer3=1, answer4=2, answer5=4, answer6=2, answer7=3, answer8=3, answer9=2, answer10=3, answer11=3, answer12=4, url=w)
c = models.Assessment(answer1=2, answer2=2, answer3=2, answer4=2, answer5=2, answer6=2, answer7=2, answer8=2, answer9=2, answer10=2, answer11=2, answer12=2, url=w)
e = models.Assessment(answer1=4, answer2=4, answer3=4, answer4=4, answer5=4, answer6=4, answer7=4, answer8=4, answer9=4, answer10=4, answer11=4, answer12=4, url=w)
g = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)
n = models.Assessment(answer1=2, answer2=3, answer3=2, answer4=1, answer5=2, answer6=2, answer7=2, answer8=3, answer9=2, answer10=1, answer11=2, answer12=2, url=w)
o = models.Assessment(answer1=3, answer2=3, answer3=3, answer4=4, answer5=4, answer6=3, answer7=4, answer8=5, answer9=5, answer10=5, answer11=5, answer12=4, url=w)
p = models.Assessment(answer1=4, answer2=2, answer3=3, answer4=4, answer5=5, answer6=4, answer7=3, answer8=3, answer9=4, answer10=5, answer11=5, answer12=4, url=w)
q = models.Assessment(answer1=5, answer2=1, answer3=3, answer4=3, answer5=5, answer6=4, answer7=4, answer8=5, answer9=5, answer10=3, answer11=2, answer12=3, url=w)


responses = (a,c,e,g,n,o,p,q)

for r in responses:
	db.session.add(r)
	db.session.commit()

w = models.Website.query.get(6)

c = models.Assessment(answer1=2, answer2=2, answer3=2, answer4=2, answer5=2, answer6=2, answer7=2, answer8=2, answer9=2, answer10=2, answer11=2, answer12=2, url=w)
e = models.Assessment(answer1=4, answer2=4, answer3=4, answer4=4, answer5=4, answer6=4, answer7=4, answer8=4, answer9=4, answer10=4, answer11=4, answer12=4, url=w)
g = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)
n = models.Assessment(answer1=2, answer2=3, answer3=2, answer4=1, answer5=2, answer6=2, answer7=2, answer8=3, answer9=2, answer10=1, answer11=2, answer12=2, url=w)
q = models.Assessment(answer1=5, answer2=1, answer3=3, answer4=3, answer5=5, answer6=4, answer7=4, answer8=5, answer9=5, answer10=3, answer11=2, answer12=3, url=w)


responses = (c,e,g,n,q)

for r in responses:
	db.session.add(r)
	db.session.commit()

w = models.Website.query.get(7)

a = models.Assessment(answer1=2, answer2=2, answer3=1, answer4=2, answer5=4, answer6=2, answer7=3, answer8=3, answer9=2, answer10=3, answer11=3, answer12=4, url=w)
b = models.Assessment(answer1=1, answer2=1, answer3=1, answer4=1, answer5=1, answer6=1, answer7=1, answer8=1, answer9=1, answer10=1, answer11=1, answer12=1, url=w)
d = models.Assessment(answer1=3, answer2=3, answer3=3, answer4=3, answer5=3, answer6=3, answer7=3, answer8=3, answer9=3, answer10=3, answer11=3, answer12=3, url=w)
e = models.Assessment(answer1=4, answer2=4, answer3=4, answer4=4, answer5=4, answer6=4, answer7=4, answer8=4, answer9=4, answer10=4, answer11=4, answer12=4, url=w)
f = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)
g = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)

responses = (a,b,d,e,f,g)

for r in responses:
	db.session.add(r)
	db.session.commit()

w = models.Website.query.get(8)

a = models.Assessment(answer1=2, answer2=2, answer3=1, answer4=2, answer5=4, answer6=2, answer7=3, answer8=3, answer9=2, answer10=3, answer11=3, answer12=4, url=w)
b = models.Assessment(answer1=1, answer2=1, answer3=1, answer4=1, answer5=1, answer6=1, answer7=1, answer8=1, answer9=1, answer10=1, answer11=1, answer12=1, url=w)
d = models.Assessment(answer1=3, answer2=3, answer3=3, answer4=3, answer5=3, answer6=3, answer7=3, answer8=3, answer9=3, answer10=3, answer11=3, answer12=3, url=w)
e = models.Assessment(answer1=4, answer2=4, answer3=4, answer4=4, answer5=4, answer6=4, answer7=4, answer8=4, answer9=4, answer10=4, answer11=4, answer12=4, url=w)
f = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)
g = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)
i = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)
j = models.Assessment(answer1=2, answer2=2, answer3=2, answer4=2, answer5=2, answer6=2, answer7=2, answer8=2, answer9=2, answer10=2, answer11=2, answer12=2, url=w)
k = models.Assessment(answer1=4, answer2=4, answer3=5, answer4=5, answer5=5, answer6=4, answer7=2, answer8=5, answer9=4, answer10=3, answer11=4, answer12=5, url=w)
l = models.Assessment(answer1=2, answer2=1, answer3=3, answer4=2, answer5=1, answer6=3, answer7=5, answer8=3, answer9=2, answer10=1, answer11=2, answer12=2, url=w)


responses = (a,b,d,e,f,g,i,j,k,l)

for r in responses:
	db.session.add(r)
	db.session.commit()

w = models.Website.query.get(9)

a = models.Assessment(answer1=2, answer2=2, answer3=1, answer4=2, answer5=4, answer6=2, answer7=3, answer8=3, answer9=2, answer10=3, answer11=3, answer12=4, url=w)
b = models.Assessment(answer1=1, answer2=1, answer3=1, answer4=1, answer5=1, answer6=1, answer7=1, answer8=1, answer9=1, answer10=1, answer11=1, answer12=1, url=w)
c = models.Assessment(answer1=2, answer2=2, answer3=2, answer4=2, answer5=2, answer6=2, answer7=2, answer8=2, answer9=2, answer10=2, answer11=2, answer12=2, url=w)
d = models.Assessment(answer1=3, answer2=3, answer3=3, answer4=3, answer5=3, answer6=3, answer7=3, answer8=3, answer9=3, answer10=3, answer11=3, answer12=3, url=w)
e = models.Assessment(answer1=4, answer2=4, answer3=4, answer4=4, answer5=4, answer6=4, answer7=4, answer8=4, answer9=4, answer10=4, answer11=4, answer12=4, url=w)
f = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)
g = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)
h = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)
i = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)
j = models.Assessment(answer1=2, answer2=2, answer3=2, answer4=2, answer5=2, answer6=2, answer7=2, answer8=2, answer9=2, answer10=2, answer11=2, answer12=2, url=w)
k = models.Assessment(answer1=4, answer2=4, answer3=5, answer4=5, answer5=5, answer6=4, answer7=2, answer8=5, answer9=4, answer10=3, answer11=4, answer12=5, url=w)
l = models.Assessment(answer1=2, answer2=1, answer3=3, answer4=2, answer5=1, answer6=3, answer7=5, answer8=3, answer9=2, answer10=1, answer11=2, answer12=2, url=w)
m = models.Assessment(answer1=1, answer2=2, answer3=1, answer4=3, answer5=2, answer6=1, answer7=2, answer8=3, answer9=1, answer10=1, answer11=2, answer12=1, url=w)
n = models.Assessment(answer1=2, answer2=3, answer3=2, answer4=1, answer5=2, answer6=2, answer7=2, answer8=3, answer9=2, answer10=1, answer11=2, answer12=2, url=w)
o = models.Assessment(answer1=3, answer2=3, answer3=3, answer4=4, answer5=4, answer6=3, answer7=4, answer8=5, answer9=5, answer10=5, answer11=5, answer12=4, url=w)
p = models.Assessment(answer1=4, answer2=2, answer3=3, answer4=4, answer5=5, answer6=4, answer7=3, answer8=3, answer9=4, answer10=5, answer11=5, answer12=4, url=w)
q = models.Assessment(answer1=5, answer2=1, answer3=3, answer4=3, answer5=5, answer6=4, answer7=4, answer8=5, answer9=5, answer10=3, answer11=2, answer12=3, url=w)

responses = (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q)

for r in responses:
	db.session.add(r)
	db.session.commit()
w = models.Website.query.get(10)

d = models.Assessment(answer1=3, answer2=3, answer3=3, answer4=3, answer5=3, answer6=3, answer7=3, answer8=3, answer9=3, answer10=3, answer11=3, answer12=3, url=w)
e = models.Assessment(answer1=4, answer2=4, answer3=4, answer4=4, answer5=4, answer6=4, answer7=4, answer8=4, answer9=4, answer10=4, answer11=4, answer12=4, url=w)
f = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)
g = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)
i = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)
k = models.Assessment(answer1=4, answer2=4, answer3=5, answer4=5, answer5=5, answer6=4, answer7=2, answer8=5, answer9=4, answer10=3, answer11=4, answer12=5, url=w)
o = models.Assessment(answer1=3, answer2=3, answer3=3, answer4=4, answer5=4, answer6=3, answer7=4, answer8=5, answer9=5, answer10=5, answer11=5, answer12=4, url=w)
p = models.Assessment(answer1=4, answer2=2, answer3=3, answer4=4, answer5=5, answer6=4, answer7=3, answer8=3, answer9=4, answer10=5, answer11=5, answer12=4, url=w)
q = models.Assessment(answer1=5, answer2=1, answer3=3, answer4=3, answer5=5, answer6=4, answer7=4, answer8=5, answer9=5, answer10=3, answer11=2, answer12=3, url=w)

responses = (d,e,f,g,i,k,o,p,q)

for r in responses:
	db.session.add(r)
	db.session.commit()

w = models.Website.query.get(11)

a = models.Assessment(answer1=2, answer2=2, answer3=1, answer4=2, answer5=4, answer6=2, answer7=3, answer8=3, answer9=2, answer10=3, answer11=3, answer12=4, url=w)
b = models.Assessment(answer1=1, answer2=1, answer3=1, answer4=1, answer5=1, answer6=1, answer7=1, answer8=1, answer9=1, answer10=1, answer11=1, answer12=1, url=w)
c = models.Assessment(answer1=2, answer2=2, answer3=2, answer4=2, answer5=2, answer6=2, answer7=2, answer8=2, answer9=2, answer10=2, answer11=2, answer12=2, url=w)
d = models.Assessment(answer1=3, answer2=3, answer3=3, answer4=3, answer5=3, answer6=3, answer7=3, answer8=3, answer9=3, answer10=3, answer11=3, answer12=3, url=w)
e = models.Assessment(answer1=4, answer2=4, answer3=4, answer4=4, answer5=4, answer6=4, answer7=4, answer8=4, answer9=4, answer10=4, answer11=4, answer12=4, url=w)
f = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)
g = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)
i = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)
k = models.Assessment(answer1=4, answer2=4, answer3=5, answer4=5, answer5=5, answer6=4, answer7=2, answer8=5, answer9=4, answer10=3, answer11=4, answer12=5, url=w)
o = models.Assessment(answer1=3, answer2=3, answer3=3, answer4=4, answer5=4, answer6=3, answer7=4, answer8=5, answer9=5, answer10=5, answer11=5, answer12=4, url=w)
p = models.Assessment(answer1=4, answer2=2, answer3=3, answer4=4, answer5=5, answer6=4, answer7=3, answer8=3, answer9=4, answer10=5, answer11=5, answer12=4, url=w)
q = models.Assessment(answer1=5, answer2=1, answer3=3, answer4=3, answer5=5, answer6=4, answer7=4, answer8=5, answer9=5, answer10=3, answer11=2, answer12=3, url=w)

responses = (a,b,c,d,e,f,g,i,k,o,p,q)

for r in responses:
	db.session.add(r)
	db.session.commit()

w = models.Website.query.get(12)

a = models.Assessment(answer1=2, answer2=2, answer3=1, answer4=2, answer5=4, answer6=2, answer7=3, answer8=3, answer9=2, answer10=3, answer11=3, answer12=4, url=w)
b = models.Assessment(answer1=1, answer2=1, answer3=1, answer4=1, answer5=1, answer6=1, answer7=1, answer8=1, answer9=1, answer10=1, answer11=1, answer12=1, url=w)
c = models.Assessment(answer1=2, answer2=2, answer3=2, answer4=2, answer5=2, answer6=2, answer7=2, answer8=2, answer9=2, answer10=2, answer11=2, answer12=2, url=w)
d = models.Assessment(answer1=3, answer2=3, answer3=3, answer4=3, answer5=3, answer6=3, answer7=3, answer8=3, answer9=3, answer10=3, answer11=3, answer12=3, url=w)
g = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)
i = models.Assessment(answer1=5, answer2=5, answer3=5, answer4=5, answer5=5, answer6=5, answer7=5, answer8=5, answer9=5, answer10=5, answer11=5, answer12=5, url=w)
k = models.Assessment(answer1=4, answer2=4, answer3=5, answer4=5, answer5=5, answer6=4, answer7=2, answer8=5, answer9=4, answer10=3, answer11=4, answer12=5, url=w)
p = models.Assessment(answer1=4, answer2=2, answer3=3, answer4=4, answer5=5, answer6=4, answer7=3, answer8=3, answer9=4, answer10=5, answer11=5, answer12=4, url=w)
q = models.Assessment(answer1=5, answer2=1, answer3=3, answer4=3, answer5=5, answer6=4, answer7=4, answer8=5, answer9=5, answer10=3, answer11=2, answer12=3, url=w)

responses = (a,b,c,d,g,i,k,p,q)

for r in responses:
	db.session.add(r)
	db.session.commit()
