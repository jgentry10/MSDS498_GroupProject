from wtforms import Form, StringField, TextAreaField, validators

# This class will be used in the webapp as the main input form
class SubmissionForm(Form):
    title = StringField('Title', [validators.Length(min=2, max=30)])
    category = StringField('Category', [validators.Length(min=0, max=30)])
    text = TextAreaField('Text', [validators.Length(min=1, max=1000)])
	#PAY_AMT1,BILL_AMT1,LIMIT_BAL,SEX,EDUCATION,MARRIAGE,AGE,PAY_0,PAY_2,PAY_3,PAY_4,PAY_5,PAY_6,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6
	