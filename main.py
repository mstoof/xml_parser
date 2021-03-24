# These imports are required to parse through the xml file.
import xml.etree.ElementTree as ET
import sys

baseTag = "{http://schemas.microsoft.com/office/infopath/2003/myXSD/2019-03-01T06:37:18}"

# The location of the file from which the IP address should be parsed.
root = ET.parse('./IP_Subnet_VLAN_aanvraag_landelijk_datacenter_Aanvragen-2020-07-23T16_47_22.xml').getroot()

#Searching for the subnets
subNetVLAN = root.find(f"{baseTag}SubnetVlan")

if subNetVLAN is None:
    print("Tag my:SubnetVlan doesn't exists, killing script")
    sys.exit()

sVipHelpersGR = subNetVLAN.find(f"{baseTag}SVIPHelpersGr")

if sVipHelpersGR is None:
    print("Tag my:my:SVIPHelpersGr doesn't exists, killing script")
    sys.exit()

# A list of all the items with the following xml tag: my:SVIPHelper
sVipIps = {}

sVipBaseKey = "IP helper addr"

# A list of all the items with the following xml tag: my:SVIPHelper
# this is the section where the IP helper addresses are located.
for elem in sVipHelpersGR.findall(f"{baseTag}SVIPHelpers"):
    for subElem in elem.findall(f"{baseTag}SVIPHelper"):
        sVipIps[f"{sVipBaseKey} {len(sVipIps) + 1}"] = subElem.text

sVipSubnets = {}

sVipSubnetBaseKey = "Subnet"

# A variable with the value of my:SVIPSubnet this i
sVipSubnets[f"{sVipSubnetBaseKey}"] = subNetVLAN.find(f"{baseTag}SVIPSubnet").text

print(sVipIps)
print(sVipSubnets)

