import pandas as pd

sal = pd.read_csv('Salaries.csv')

sal.head()

sal.info() # 148654 Entries

sal['BasePay'].mean()

sal['OvertimePay'].max()

sal[sal['EmployeeName']=='JOSEPH DRISCOLL']

sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']

sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']

sal['TotalPayBenefits'].max()

sal[sal['TotalPayBenefits']== sal['TotalPayBenefits'].max()] #['EmployeeName']
# or
# sal.loc[sal['TotalPayBenefits'].idxmax()]

sal.loc[sal['TotalPayBenefits'].idxmax()]

sal[sal['TotalPayBenefits']== sal['TotalPayBenefits'].min()] #['EmployeeName']
# or
# sal.loc[sal['TotalPayBenefits'].idxmax()]['EmployeeName']

## ITS NEGATIVE!! VERY STRANGE

sal.loc[sal['TotalPayBenefits'].idxmin()]['EmployeeName']

sal.loc[sal['TotalPayBenefits'].idxmin()]

sal.groupby('Year').mean()['BasePay']

sal['JobTitle'].nunique()

sal['JobTitle'].value_counts().head(5)

sal[sal['Year']==2013]['JobTitle'].value_counts()

sum(sal[sal['Year']==2013]['JobTitle'].value_counts() == 1) # pretty tricky way to do this...

def chief_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False

sal['JobTitle'].iloc[0]

chief_string('GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY')

sum(sal['JobTitle'].apply(lambda x: chief_string(x)))

sal['title_len'] = sal['JobTitle'].apply(len)
sal[['JobTitle', 'title_len']].head()

sal[['JobTitle', 'title_len']].corr()

sal[['title_len','TotalPayBenefits']].corr() # No correlation.