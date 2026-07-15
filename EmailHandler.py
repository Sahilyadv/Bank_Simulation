import gmail

def send_credentials(email, name, acn, pwd):
    con = gmail.GMail('sahilyad4567@gmail.com', 'uykv mwdd brrv jiza')

    body = f"""Hello {name},

Welcome to ABC Bank, here are your credentials:

Account No = {acn}
Password = {pwd}

Kindly change your password when you login first time.

ABC Bank
Sector-16, Noida
"""

    msg = gmail.Message(
        to=email,
        subject='Your Credentials for operating account',
        text=body
    )

    con.send(msg)
    
  
def send_otp(email, name, otp):
    con = gmail.GMail('sahilyad4567@gmail.com', 'uykv mwdd brrv jiza')

    body = f"""Hello {name},

Welcome to ABC Bank, here is your OTP to recover password:

OTP = {otp}

ABC Bank
Sector-16, Noida
"""

    msg = gmail.Message(
        to=email,
        subject='OTP for password recovery',
        text=body
    )

    con.send(msg)  
    
def send_otp_withdraw(email, name, otp,amt):
    con = gmail.GMail('sahilyad4567@gmail.com', 'uykv mwdd brrv jiza')

    body = f"""Hello {name},

Welcome to ABC Bank, here is your OTP to withdraw {amt} from your account:

OTP = {otp}

ABC Bank
Sector-16, Noida
"""

    msg = gmail.Message(
        to=email,
        subject='OTP for withdrawing amount',
        text=body
    )

    con.send(msg)        
    
def send_otp_transfer(email, name, otp,amt,to_acn):
    con = gmail.GMail('sahilyad4567@gmail.com', 'uykv mwdd brrv jiza')

    body = f"""Hello {name},

Welcome to ABC Bank, here is your OTP to transfer account {amt} to ACN : {to_acn}

OTP = {otp}

ABC Bank
Sector-16, Noida
"""

    msg = gmail.Message(
        to=email,
        subject='OTP for transferring amount',
        text=body
    )

    con.send(msg)            