import random
import string
import time
import click


def generateWarehouseId():
    return "DXB3"

def generateReceiveType():
    return "EACH"

def generateAsin():
    return 'B' + ''.join(random.sample(list(string.ascii_uppercase + string.digits),9))

def generateFnSku(generatedAsin):
    return random.choice([generatedAsin,'X' + ''.join(random.sample(list(string.ascii_uppercase + string.digits),9))])

def generateFcSku(generatedFnSku):
    return random.choice([generatedFnSku,'Z'+''.join(random.sample(list(string.ascii_uppercase + string.digits),9))])

def generateQuantity():
     return random.randint(1,15)

def generateInboundShipmentDeliveryId():
    return ''.join(random.sample(list(string.digits),8))

def generateReceiveContainerId():
    return ''.join(random.sample(list(string.digits),6))

def generateReceiveContainerScannableId():
    return 'P-'+random.choice(list(string.digits))+'-'+''.join(random.sample(list(string.digits+string.ascii_uppercase),8))

def generateClientLogin():
    return "kumaranu"

def generateClientApplication():
    return "IRS"

def generatePriceFC():
    return round(random.uniform(0,15),2)

def generatePrice(priceFC):
    return priceFC;

def generateForeignCurrencyCode():
    return "AED"

def generateBaseCurrencyCode():
    return "AED"

def generateCost():
    return round(random.uniform(0,15),2)

def generateCostFC(cost):
    return cost;

def generateExchangeRate():
    return 1

def generateExchangeType():
    return 'C'

def generateExchangeDate():
    return int(time.time()-random.randint(100,200))

def generateOrderId():
    return ''.join(random.sample(list(string.ascii_uppercase + string.digits),7))

def generateGlProductGroup():
    return random.choice([14,15,20,21,22,23,27,44,50,53,60,63,65,74,75,79,86,107,111,114,121,123,125,129,136,147,153,158,160,171,180,193,194,195,196,197,198,199,200,201,219,226,228,229,234,236,241,246,251,256,258,259,260,261,262,263,264,265,266,267,279,293,297,298,304,307,309,311,313,316,318,325,327,328,334,336,340,349,350,351,353,354,355,356,360,362,364,366,367,370,392,394,395,396,397,400,402,405,406,407,408,409,410,411,412,414,416,417,420,421,422,424,425,426,437,438,439,441,442,443,444,446,447,448,449,450,451,460,462,465,467,468,469,470,473,475,484,485,487,489,493,494,496,497,500,503,504,510,515,517,540,541,542,543,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,570,582,590,591,592,594,596,597,598,609,610,611,613,616,618,620,624,626,628,632,633,634,637,639,640,641,644,645,649,650,653,655,657,663,667,670,673,675,679,682,685,686,689,693,694,697,698])

def generateInventoryOwnerGroupId():
    return random.randint(1,10)

def generateLegalEntityId():
    return random.randint(1,301)

def generateDistributorId():
    return ''.join(random.sample(list(string.ascii_uppercase + string.digits),5))

def generateInventoryFiscalOwnerId():
    return ''.join(random.sample(list(string.digits),6))

def generateOrderType():
    return random.randint(1,10)

def generateHandler():
    return "oe"

def generateConfirmationDate():
    return int(time.time()-random.randint(100,200))

@click.command()
@click.option("--numrecords", default=2, help="Number of records")
def generateData(numrecords):
    record_list = []
    for i in range(numrecords):
        asin=generateAsin()
        fnSku=generateFnSku(asin)
        fcSku=generateFcSku(fnSku)
        receiveContainerId=generateReceiveContainerId()
        receiveContainerScannableId=generateReceiveContainerScannableId()
        priceFC=generatePriceFC()
        price=generatePrice(priceFC)
        cost=generateCost()
        costFC=generateCostFC(cost)

        record = ','.join([str(receiveContainerId),generateWarehouseId(),
        generateReceiveType(),
        asin,
        fnSku,
        fcSku,
        str(generateQuantity()),
        str(generateInboundShipmentDeliveryId()),
        receiveContainerScannableId,
        generateClientLogin(),
        generateClientApplication(),
        generateForeignCurrencyCode(),
        generateBaseCurrencyCode(),
        str(priceFC),
        str(price),
        str(cost),
        str(costFC),
        str(generateExchangeRate()),
        generateExchangeType(),
        str(generateExchangeDate()),
        generateOrderId(),
        str(generateGlProductGroup()),
        str(generateInventoryOwnerGroupId()),
        str(generateLegalEntityId()),
        generateDistributorId(),
        str(generateInventoryFiscalOwnerId()),
        str(generateOrderType()),
        generateHandler(),
        str(generateConfirmationDate())])
        record_list.append(record)

    print(*record_list, sep = "\n")


if __name__ == '__main__':
    generateData()
