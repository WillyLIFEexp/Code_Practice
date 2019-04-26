import re
test_input =  ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

def check_email_wre(emails):
    tmp_list = set()
    match = r"(.*)\+.*(@.*)"
    for email in emails:
        matchs = re.search(match,email)
        host_name = ''.join(matchs.group(1).split('.'))
        tmp_list.append(host)
    return len(tmp_list)

def check_email_better_version(emails):
    tmp_list = set()
    for email in emails:
        email_list = email.split("@")
        host_name = "".join(email_list[0].split('+')[0].split('.'))
        real_email = host_name+'@'+email_list[1]
        tmp_list.add(real_email)
    return len(tmp_list)
