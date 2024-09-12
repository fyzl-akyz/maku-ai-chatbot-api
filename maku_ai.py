import requests,bs4,argparse
parser = argparse.ArgumentParser( description="Provides  a personal greeting.")

parser.add_argument(
    "-s", "--sorgu",metavar="sorgu",required=True,help="Yapay zekaya soru sormanıza yarayan komut"
)
parser.add_argument(
    "-hakkimda", "--hakkimda",metavar="sorgu",required=False,help="Bu konsolun sürecini açıklar"
)
args = parser.parse_args()
gelen_sorgu = args.sorgu
if gelen_sorgu =='hakkımda':
    print('\n Merhaba bu program tamamıyla test amacıyla yazıldı. Bu program kodları paylaşılmayacaktır ! \n Daha fazlası için  : \n https://www.linkedin.com/in/feyzullah-akyuz/ \n https://github.com/fyzl-akyz')
else:
    def check(gelen_sorgu):

        data = {
            "message" : gelen_sorgu
        }
        headers = {
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            "x-requested-with":"XMLHttpRequest"
        }
        client = requests.session()
        login_page = client.post("https://ddk.maku.edu.tr/bilen/maku")
        login_page_html = bs4.BeautifulSoup(login_page.text, 'html.parser')
        print('Kullanıcı verisi çekiliyor ⌛  ')

        login_page = client.post("https://ddk.maku.edu.tr/bilen/Bilen/setContract")
        login_page_html = bs4.BeautifulSoup(login_page.text, 'html.parser')
        if login_page_html.text == 'ok':
            print('Kullanıcı verisi geldi ⌛  \n🤖 : ')
        login_page = client.post("https://ddk.maku.edu.tr/bilen/Bilen/getresponse" , data=data,headers=headers)
        login_page_html = bs4.BeautifulSoup(login_page.text, 'html.parser')
        print(login_page_html)

    check(gelen_sorgu)