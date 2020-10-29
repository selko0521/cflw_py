from selenium import webdriver	#selenium
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities	#selenium
class C火狐(webdriver.Firefox):
	c连接特性 = 0x0002
	def __init__(self):
		v能力 = webdriver.DesiredCapabilities.FIREFOX.copy()
		v能力['acceptInsecureCerts'] = True
		v档案 = webdriver.FirefoxProfile()
		v档案.accept_untrusted_certs = True
		v档案.set_preference("browser.download.folderList", 0)	#设置成0表示下载到默认路径
		v档案.set_preference("browser.download.manager.showWhenStarting", False)	#是否显示开始
		v档案.set_preference("browser.download.manager.useWindow", False)
		v档案.set_preference("browser.download.manager.alertonEXEopen", False)
		v档案.set_preference("browser.download.manager.showAlertonComplete", False)
		v档案.set_preference("browser.download.manager.closeWhenDone", False)
		v档案.set_preference('browser.helperApps.alwaysAsk.force', False)
		v档案.set_preference("browser.helperApps.neverAsk.saveToDisk", "binary/octet-stream,application/octet-stream,application/zip,text/plain")	#不询问下载路径的文件类型
		webdriver.Firefox.__init__(self, capabilities = v能力, firefox_profile = v档案)
	def f打开(self, a地址):
		self.get(a地址)
	def fs下载路径(self, a路径):
		self.firefox_profile.set_preference("browser.download.folderList", 2)	#设置成2则可以保存到指定目录
		self.firefox_profile.set_preference("browser.download.dir", a路径)	#下载到指定目录
