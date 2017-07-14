#-*- coding:utf-8 -*-
from framework.base_page import BasePage
from framework.excelparser import ExcelParser
from framework.get_keycases import KeyCases



class HomePage(BasePage):
    

             
    #input_box = "id=>kw"
    #search_submit_btn = "xpath=>//*[@id='su']" 
    def type_clear(self):
        self.clear(self.input_box)
    def type_search(self, text): 
        self.type(self.input_box, text)
    def send_submit_btn(self):
        self.click(self.search_submit_btn)
    
          
    '''    
    #excel表内关键字列表 [('type', 'id=>kw', '输入搜索'), (), ()]
    action_list = KeyCases().key_case_list_all()

    def type_clear(self): 
        for i in range(len(self.action_list)):
            if self.action_list[i][0] == 'type':        
                self.clear(self.action_list[i][1])
 
    def type_search_list(self, action_list, text):
        self.action_list = action_list
        self.action_list
        
        pass
    
    def type_search(self, text):
    #执行excel表内type关键字用例
        for i in range(len(self.action_list)):
            if self.action_list[i][0] == 'type':
                
                self.type(self.action_list[i][1], text)
                print self.action_list[i][2]
                #return self.action_list[i][2]

    def send_submit_btn(self):
        #执行excel表内type关键字用例
            for i in range(len(self.action_list)):
                if self.action_list[i][0] == 'search':                   
                    self.click(self.action_list[i][1]) 
                    #return self.action_list[i][2]             
                    
                    
    '''                                                