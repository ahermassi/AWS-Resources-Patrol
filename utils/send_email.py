def send_email(account_id, account_alias, mail_enabled, ses, sender, recipients, subject, charset, ec2_running,
               rds_running, redshift_running, elasticsearch_running):
    if not ec2_running and not rds_running and not redshift_running and not elasticsearch_running:
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
                    <p>Number of running EC2 instances: """ + str(len(ec2_running)) + """"""
        else:
            ec2_table = """"""

        if rds_running:
            rds_table = """
                <h3>Running RDS Instance(s):</h3>
                <table cellpadding="4" cellspacing="4">
                <tr><td><strong>Name</strong></td><td><strong>Engine</strong></td><td><strong>Status</strong></td>
                <td><strong>Type</strong></td><td><strong>Storage</strong></td><td><strong>Region</strong></td>
                <td><strong>Creation Time</strong></td></tr>
                """ + \
                        "\n".join([f"<tr><td>{instance['identifier']}</td><td>{instance['engine']}</td><td>"
                                   f"{instance['status']}</td><td>" f"{instance['type']}</td><td>"
                                   f"{instance['storage']}</td><td>{instance['region']}</td>"
                                   f"<td>{instance['creation_time']}</td>" f"</tr>"
                                   for instance in rds_running]) \
                        + """
                    </table>
                    <p>Number of running RDS instances: """ + str(len(rds_running)) + """"""
        else:
            rds_table = """"""

        if redshift_running:
            redshift_table = """
                <h3>Running Redshift Instance(s):</h3>
                <table cellpadding="4" cellspacing="4">
                <tr><td><strong>Name</strong></td><td><strong>Status</strong></td><td><strong>Type</strong></td>
                <td><strong>Number of Nodes</strong></td><td><strong>Region</strong></td>
                <td><strong>Creation Time</strong></td></tr>
                """ + \
                        "\n".join([f"<tr><td>{instance['identifier']}</td><td>" f"{instance['status']}</td>"
                                   f"<td>" f"{instance['type']}</td><td>{instance['nodes']}</td><td>{instance['region']}</td>"
                                   f"<td>{instance['creation_time']}</td>" f"</tr>"
                                   for instance in redshift_running]) \
                        + """
                    </table>
                    <p>Number of running Redshift instances: """ + str(len(redshift_running)) + """"""
        else:
            redshift_table = """"""

        if elasticsearch_running:
            elasticsearch_table = """
                <h3>Created Elasticsearch Domain(s):</h3>
                <table cellpadding="4" cellspacing="4">
                <tr><td><strong>Domain Name</strong></td><td><strong>Domain ID</strong></td><td><strong>Created</strong></td>
                <td><strong>Instance Type</strong></td><td><strong>Instance Count</strong></td>
                <td><strong>Endpoints</strong></td></tr>
                """ + \
                        "\n".join([f"<tr><td>{domain['name']}</td><td>" f"{domain['id']}</td>"
                                   f"<td>" f"{domain['created']}</td><td>{domain['instance_type']}</td>"
                                   f"<td>{domain['instance_count']}</td><td>{domain['endpoints']}</td></tr>"
                                   for domain in elasticsearch_running]) \
                        + """
                    </table>
                    <p>Number of created Elasticsearch domains: """ + str(len(elasticsearch_running)) + """"""
        else:
            elasticsearch_table = """"""

        html_body = header + ec2_table + rds_table + redshift_table + elasticsearch_table

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
