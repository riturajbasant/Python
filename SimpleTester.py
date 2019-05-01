#import
from dxclient.Query import *
from dxclient.DxOpenClient import DxOpenClient

# Create the DXOpenClient object with the URL of DX Open
client = DxOpenClient("https://msf.markit.com/DxOpen")

# Set the credentials of the user so that DX Open can assign the relevant permissions.
client.setCredentials("API_Test002", "sp0rtNik")

# Create a query object for SF data
query = DxlClientQuery()

# Set the source to be the client's market
query.setSource('Client.Market')

# Add a market identifier
query.addIdentifier('Market', 'S&P500')

# Add a field for which to fetch the data
query.addFields(['LendableValue'])

# Add a date for which the data is required
query.setFromDate('20180522') #('22 May 2018')
query.setToDate('20180522') #('22 May 2018')

# Perform the query
marketData = client.getClient(query).get_Market()

# Print the data retrieved from the API
print 'Date: '+ str(marketData[0].get_DataDate()[0].value.strftime('%d %b %Y'))
print 'Lendable Value: ' + '{0:15.6f}'.format(marketData[0].get_DataDate()[0].get_Inventory().LendableValue)

client.logout()