import sublime
import sublime_plugin

def unescape_str(s:str)->str:
	return s.replace("\\n", "\n").replace("\\t", "\t").replace("\\r", "\r").replace("\\\\", "\\").replace("\\\"", "\"")

def escape_str(s:str)->str:
	return s.replace("\\", "\\\\").replace("\n", "\\n").replace("\t", "\\t").replace("\r", "\\r").replace("\"", "\\\"")


class UnescapeSelectionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				# 获取选中的文本
				text = self.view.substr(region)
				# 转换大小写
				toggled = unescape_str(text)
				# 替换文本
				self.view.replace(edit, region, toggled)

class EscapeSelectionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				# 获取选中的文本
				text = self.view.substr(region)
				# 转换大小写
				toggled = escape_str(text)
				# 替换文本
				self.view.replace(edit, region, toggled)
