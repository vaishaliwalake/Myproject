import xml.etree.cElementTree as ET

root = ET.Element("root")
doc = ET.SubElement(root, "doc")

ET.SubElement(doc, "field1", name="samplexml1").text = "some value1"
ET.SubElement(doc, "field2", name="samplexml2").text = "some vlaue2"

tree = ET.ElementTree(root)
tree.write("samplexml.xml")
