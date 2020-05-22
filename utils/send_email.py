def send_email(account_id, account_alias, mail_enabled, ses, sender, recipients, subject, charset, ec2_running):
    if not ec2_running:
        print('No running instances')
    elif int(mail_enabled) == 1:
        print('Sending email to: {}'.format(', '.join(recipients)))
        body = 'AWS Resources Patrol\instance\n Running EC2 Instances {ec2}'.format(ec2=len(ec2_running))
        header = """
            <html>
                <head>
                    <style>
                        table, th, td {
                            border: 2px solid blue;
                            border-collapse: collapse;
                        }
                    </style>
                </head>
                <body>
                    <h1>AWS Resources Patrol</h1>
                    <p>AWS Account ID: """ + account_id + """ - """ + account_alias + """</p>"""

        if ec2_running:
            ec2_table = """
                <h3>Running EC2 Instance(s):</h3>
                <table cellpadding="4" cellspacing="4">
                <tr><td><strong>Name</strong></td><td><strong>Instance ID</strong></td><td><strong>Instance 
                Type</strong></td><td><strong>State</strong></td><td><strong>Region</strong></td><td><strong>Launch 
                Time</strong></td></tr>
                """ + \
                        "\n".join([f"<tr><td>{instance['name']}</td><td>{instance['id']}</td><td>"
                                   f"{instance['type']}</td><td>" f"{instance['state']}</td><td>"
                                   f"{instance['region']}</td><td>{instance['launch_time']}</td></tr>"
                                   for instance in ec2_running]) \
                        + """
                    </table>
                    <p>Total number of running EC2 instance(s): """ + str(len(ec2_running)) + """"""
        else:
            ec2_table = """"""

        html_body = header + ec2_table

        ses.send_email(
            Destination={
                'ToAddresses': recipients,
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': charset,
                        'Data': html_body,
                    },
                    'Text': {
                        'Charset': charset,
                        'Data': body,
                    },
                },
                'Subject': {
                    'Charset': charset,
                    'Data': subject + account_id,
                },
            },
            Source=sender,
        )
        print('Email sent!')
    else:
        print('Email notification disabled')
