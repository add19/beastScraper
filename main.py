import urllib3	
from bs4 import BeautifulSoup
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_score(score):
	http = urllib3.PoolManager()

	urlRes = http.request('GET', 'http://www.cricbuzz.com/live-cricket-scores/')
	soup = BeautifulSoup(urlRes.data,"lxml")

	# score = soup.find_all('div', attrs = {'class':'cb-lv-scrs-col text-black'})
	data = []
	score = soup.find_all("div", attrs={"class":"cb-lv-scrs-col text-black"})
	result = soup.find_all("div", attrs={"class":"cb-lv-scrs-col cb-text-live"})
	over = soup.find_all("div", attrs={"class": "cb-lv-scrs-col cb-text-complete"})

	for i in score:
		print(i.getText() + '\n')


	print('\n\nLive Results: ' + '\n')
	for j in result:
		print(j.getText() + '\n')

	print('\n\nJust Happened: ' + '\n')
	for k in over:
		print(k.getText() + '\n')

if __name__ == "__main__":
	score = ''
	while (True):
		get_score(score)
		print('\n\n')
		time.sleep(60)

# <div class="cb-mtch-lst cb-col cb-col-100 cb-tms-itm"><div class="cb-col-100 cb-col cb-schdl"><h3 class="cb-lv-scr-mtch-hdr inline-block"><a class="text-hvr-underline text-bold" href="/live-cricket-scores/20183/zim-vs-pak-4th-odi-pakistan-tour-of-zimbabwe-2018" title="Zimbabwe vs Pakistan">Zimbabwe vs Pakistan,</a></h3><span class="text-gray">&nbsp;4th ODI</span><div class="text-gray"><span class="schedule-date ng-isolate-scope" timestamp="1532070900000" format="MMM dd'">Jul 20</span><span>&nbsp;•&nbsp;</span><span ng-bind="1532070900000 |date:'h:mm a'" class="ng-binding">12:45 PM</span><span class="text-gray"> at Queens Sports Club, Bulawayo</span></div></div><div class="cb-col-100 cb-col cb-schdl"><a class="cb-lv-scrs-well cb-lv-scrs-well-complete" href="/live-cricket-scores/20183/zim-vs-pak-4th-odi-pakistan-tour-of-zimbabwe-2018" title="Zimbabwe vs Pakistan 4th ODI"> <div class="cb-col"> <div class="cb-scr-wll-chvrn"> <div class="cb-lv-scrs-col text-black"><span class="text-bold">ZIM</span> 155-all out (42.4 Ovs) <span class="cb-series-sch-dot">&nbsp;•&nbsp;</span> <span class="text-bold">PAK</span> 399/1 (50.0 Ovs)</div> <div class="cb-lv-scrs-col cb-text-complete">Pakistan won by 244 runs</div> </div> <div class="cb-scr-wll-chvrn"> <div class="cb-ico cb-lv-scr-chvrn-bg"></div> </div> </div> </a></div><nav class="cb-col-100 cb-col padt5"><a href="/live-cricket-scores/20183/zim-vs-pak-4th-odi-pakistan-tour-of-zimbabwe-2018" class="cb-text-link cb-mtch-lnks">Live Score</a><a href="/live-cricket-scorecard/20183/zim-vs-pak-4th-odi-pakistan-tour-of-zimbabwe-2018" class="cb-text-link cb-mtch-lnks">Scorecard</a><a href="/cricket-full-commentary/20183/zim-vs-pak-4th-odi-pakistan-tour-of-zimbabwe-2018" class="cb-text-link cb-mtch-lnks">Full Commentary</a><a href="/cricket-match-news/20183/zim-vs-pak-4th-odi-pakistan-tour-of-zimbabwe-2018" class="cb-text-link cb-mtch-lnks">News</a></nav></div>
# <div class="cb-mtch-lst cb-col cb-col-100 cb-tms-itm"><div class="cb-col-100 cb-col cb-schdl"><h3 class="cb-lv-scr-mtch-hdr inline-block"><a class="text-hvr-underline text-bold" href="/live-cricket-scores/20165/sl-vs-rsa-2nd-test-south-africa-tour-of-sri-lanka-2018" title="Sri Lanka vs South Africa">Sri Lanka vs South Africa,</a></h3><span class="text-gray">&nbsp;2nd Test</span><div class="text-gray"><span class="schedule-date ng-isolate-scope" timestamp="1532061000000" format="MMM dd'">Jul 20</span><span> - </span><span class="schedule-date ng-isolate-scope" timestamp="1532390400000" format="MMM dd'">Jul 24</span><span>&nbsp;•&nbsp;</span><span ng-bind="1532061000000 |date:'h:mm a'" class="ng-binding">10:00 AM</span><span class="text-gray"> at Sinhalese Sports Club, Colombo</span></div></div><div class="cb-col-100 cb-col cb-schdl"><a class="cb-lv-scrs-well cb-lv-scrs-well-live" href="/live-cricket-scores/20165/sl-vs-rsa-2nd-test-south-africa-tour-of-sri-lanka-2018" title="Sri Lanka vs South Africa 2nd Test"> <div class="cb-col"> <div class="cb-scr-wll-chvrn"> <div class="cb-lv-scrs-col text-black"><span class="text-bold">SL</span> 277/9 (86.0 Ovs) <span class="cb-series-sch-dot">&nbsp;•&nbsp;</span> <span class="text-bold">RSA</span> </div> <div class="cb-lv-scrs-col cb-text-live">Day 1: Stumps</div> </div> <div class="cb-scr-wll-chvrn"> <div class="cb-ico cb-lv-scr-chvrn-bg"></div> </div> </div> </a></div><nav class="cb-col-100 cb-col padt5"><a href="/live-cricket-scores/20165/sl-vs-rsa-2nd-test-south-africa-tour-of-sri-lanka-2018" class="cb-text-link cb-mtch-lnks">Live Score</a><a href="/live-cricket-scorecard/20165/sl-vs-rsa-2nd-test-south-africa-tour-of-sri-lanka-2018" class="cb-text-link cb-mtch-lnks">Scorecard</a><a href="/cricket-full-commentary/20165/sl-vs-rsa-2nd-test-south-africa-tour-of-sri-lanka-2018" class="cb-text-link cb-mtch-lnks">Full Commentary</a><a href="/cricket-match-news/20165/sl-vs-rsa-2nd-test-south-africa-tour-of-sri-lanka-2018" class="cb-text-link cb-mtch-lnks">News</a></nav></div>

# <div class="cb-col"> <div class="cb-scr-wll-chvrn"> <div class="cb-lv-scrs-col text-black"><span class="text-bold">SL</span> 277/9 (86.0 Ovs) <span class="cb-series-sch-dot">&nbsp;•&nbsp;</span> <span class="text-bold">RSA</span> </div> <div class="cb-lv-scrs-col cb-text-live">Day 1: Stumps</div> </div> <div class="cb-scr-wll-chvrn"> <div class="cb-ico cb-lv-scr-chvrn-bg"></div> </div> </div>
# <div class="cb-col"> <div class="cb-scr-wll-chvrn"> <div class="cb-lv-scrs-col text-black"><span class="text-bold">ZIM</span> 155-all out (42.4 Ovs) <span class="cb-series-sch-dot">&nbsp;•&nbsp;</span> <span class="text-bold">PAK</span> 399/1 (50.0 Ovs)</div> <div class="cb-lv-scrs-col cb-text-complete">Pakistan won by 244 runs</div> </div> <div class="cb-scr-wll-chvrn"> <div class="cb-ico cb-lv-scr-chvrn-bg"></div> </div> </div>