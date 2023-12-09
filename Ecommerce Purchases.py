import pandas as pd

data = pd.read_csv(r'Ecommerce Purchases')
data


# # 1. Display top 10 rows of the dataset
data.head(10)

# # 2. Check last 10 rows of the dataset
data.tail(10)


# # 3. Check datatype of each column
data.dtypes


# # 4. Check null values in the dataset
data.isnull().sum()


# # 5. How many rows and columns are there in our dataset
len(data.columns)

len(data)

data.info()


# # 6. Highest and lowest purchase prices
data.columns

data['Purchase Price'].max()

data['Purchase Price'].min()


# # 7. Average purchase price
data['Purchase Price'].mean()


# # 8. How many people have French 'fr' as their language?
data.columns


data[data['Language'] == 'fr']


len(data[data['Language'] == 'fr'])


data[data['Language'] == 'fr'].count()


# # 9. Job title contains Engineer
data.columns


data['Job'].str.contains('engineer')


len(data[data['Job'].str.contains('engineer',case=False)])


# # 10. Find email of the person with the following ip address: 132.207.160.22
data.columns


data[data['IP Address'] == "132.207.160.22"]['Email']


# # 11. How many people have mastercard as their credit card provider and made a purchase above 50?
data.columns


len(data[(data['CC Provider']=='Mastercard') & (data['Purchase Price'] > 50)])


# # 12. Find the email of the person with the following credit card number: 4664825258997302
data.columns


data[data['Credit Card'] == 4664825258997302]['Email']


# # 13. How many people purchase during AM and How many people purchase during PM?
data.columns


data['AM or PM'].value_counts()


# # 14. How many people have a credit card that expires in 2020?
data.columns


data['CC Exp Date']


def fun():
    count = 0
    for date in data['CC Exp Date']:
        if date.split('/')[1]=='20':
            count=count+1
    print(count)


fun()
# #### so, 988 people's credit card will expire in 2020

data.columns


len(data[data['CC Exp Date'].apply(lambda x:x[3:]=='20')])


# # 15. Top 5 most popular email providers
list1 = []
for email in data['Email']:
    list1.append(email.split('@')[1])


data['temp'] = list1


data.head(1)


data['temp'].value_counts().head()

