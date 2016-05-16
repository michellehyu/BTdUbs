import os
# for sendgrid
EMAIL_USE_TLS= True
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER= os.environ['SENDGRID_USERNAME']
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
EMAIL_PORT = 587
