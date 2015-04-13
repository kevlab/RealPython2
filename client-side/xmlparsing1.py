from xml.etree import ElementTree as et

doc = et.parse("cars.xml")

print doc.find("CAR/MODEL").text
print doc.find("CAR[2]/MODEL").text
