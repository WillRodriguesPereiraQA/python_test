from Selenium2Library import Selenium2Library
from SeleniumLibrary.base import keyword
from random import randint
import time

class CustomLib(Selenium2Library):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    @keyword
    def console_log(self, texto):
        print(texto)

    @keyword
    def select_multiple_random_from_list_by_index(self, select, limit):
        selectValueList = self.get_list_items(select)
        for x in range(limit):
            index = randint(0, len(selectValueList) - 1)
            self.select_from_list_by_index(select, str(index))
    
    @keyword
    def select_from_list_random(self, select):
        i = 0
        selectValueList = self.get_list_items(select)
        while len(selectValueList) <= 1:
            time.sleep(0.5)
            selectValueList = self.get_list_items(select)
            if i == 5:
                self.failure_occurred()
                break
            i = i + 1
        index = randint(1, len(selectValueList) - 1)
        self.select_from_list_by_index(select, str(index))

    @keyword
    def search_component_in_component_list_by_title_name(self, name):
        i = 0
        componentList = self.get_webelements("css:#list-table tr")
        while len(componentList) < 2:
            time.sleep(0.5)
            componentList = self.get_webelements("css:#list-table tr")
            if i == 5:
                self.failure_occurred()
                break
            else:
                i = i + 1
        for element in componentList:
            if (len(element.find_elements_by_css_selector("p.text")) > 0):
                if (self.get_text(element.find_element_by_css_selector("p.text")) == name):
                    return element
        self.failure_occurred()

    @keyword
    def return_child_element_from_parent(self, element, query):
        if(str(query).__contains__("css:")):
            query = str(query).replace("css:", "")
            print(query)
        return element.find_element_by_css_selector(query)

    @keyword
    def input_filter_description(self):
        cond = "input"
        while len(self.get_webelements("css:input[name='chose-opt']")) == 0:
            if len(self.get_webelements("css:select[name='chose-opt']")) > 0:
                cond = "select"
                break
            time.sleep(0.5)
        if (cond.__eq__("input")):
            self.input_text('css:.make-filter input[name="chose-opt"]', "Filter description")
        else:
            self.select_from_list_random('css:.make-filter select[name="chose-opt"]')

    @keyword
    def wait_until_element_loses_attribute(self, locator, attribute):
        i = 0
        while str(self.get_element_attribute(locator, attribute)).__eq__("true"):
            time.sleep(0.5)
            if i == 5:
                self.failure_occurred()
                break
            i = i + 1
    
    @keyword
    def say_no_to_register_highlight_to_a_page(self):
        if(str(self.get_location()).__contains__("carousel-form")):
            self.wait_until_element_is_visible("css:#modalReplaceHl")
            self.click_element("css:.no-replace")
    
    @keyword
    def return_random_element_with_selector_from_list(self, selector):
        i = 0
        elementList = self.get_webelements(selector)
        while len(elementList) <= 1:
            time.sleep(0.5)
            elementList = self.get_webelements(selector)
            if i == 5:
                self.failure_occurred()
                break
            i = i + 1
        index = randint(1, len(elementList) - 1)
        return elementList[index]
    
    @keyword
    def return_element_with_selector_from_list_by_index(self, selector, index):
        i = 0
        elementList = self.get_webelements(selector)
        while len(elementList) <= 1:
            time.sleep(0.5)
            elementList = self.get_webelements(selector)
            if i == 5:
                self.failure_occurred()
                break
            i = i + 1
        return elementList[int(index)]
    
    @keyword
    def element_list_should_be_equals_or_higher_then_length(self, selector, length):
        elementList = self.get_webelements(selector)
        if(len(elementList) >= int(length)):
            print("validation passed: list length equals or higher then sended length")
        else:
            self.failure_occurred()

    @keyword
    def return_highlight_carousel_from_page_creation_page(self):
        i = 0
        while len(self.get_webelements("css:#source-carousel tr")) < 0:
            time.sleep(0.5)
            if i == 5:
                self.failure_occurred()
                break
            i = i + 1
        carouselsList = self.get_webelements("css:#source-carousel tr")
        for carousel in carouselsList:
            if(self.get_text(carousel.find_element_by_css_selector("span.type")).__contains__("Hero")):
                print("achei highlight")
                return carousel
        print("nao achei highlight")
        self.failure_occurred()
    
    @keyword
    def drag_comom_carousel_into_phone_viewer(self, carouselCont):
        i = 0
        while len(self.get_webelements("css:#source-carousel tr")) < 0:
            time.sleep(0.5)
            if i == 5:
                self.failure_occurred()
                break
            i = i + 1
        carouselsList = self.get_webelements("css:#source-carousel tr")
        for carousel in carouselsList:
            if(self.get_text(carousel.find_element_by_css_selector("span.type")).__contains__("Hero")):
                carouselsList.remove(carousel)
        i = 0
        while i < int(carouselCont):
            index = randint(0, len(carouselsList) - 1)
            self.drag_and_drop(carouselsList[index], "css:tfoot .area-new-carrossel")
            carouselsList.remove(carouselsList[index])
            i = i + 1
            time.sleep(0.2)
        
    @keyword
    def return_parent_element_from_child(self, selector):
        self.wait_until_page_contains_element(selector)
        return self.get_webelement(selector).find_element_by_xpath('parent::*')
    
    @keyword
    def select_content_by_number(self, contentCont):
        i = 1
        lim = 0
        contentList = self.get_webelements("css:.filme-item .ck-mark")
        while len(self.get_webelements("css:.filme-item .ck-mark")) <= 1:
            time.sleep(0.5)
            lim = lim + 1
            if lim == 5:
                self.failure_occurred()
                break
        contentList = self.get_webelements("css:.filme-item .ck-mark")
        for content in contentList:
            self.click_element(content)
            if(int(contentCont) == i):
                break
            else:
                i = i + 1
            
    @keyword
    def return_content_in_catalog_by_title(self, title):
        i = 0
        while len(self.get_webelements("css:.filme-item")) < 1:
            time.sleep(0.5)
            i = i + 1
            if i == 5:
                self.failure_occurred()
                break
        contentList =  self.get_webelements("css:.filme-item")
        for content in contentList:
            contentTitle = self.get_text(content.find_element_by_css_selector("h4"))
            if title.__eq__(contentTitle):
                return content
        
    @keyword
    def list_should_contain(self, listValues, param):
        if not(listValues.__contains__(param)):
            self.failure_occurred()
    
    @keyword
    def return_all_values_from_select(self, select):
        element = self.get_webelement(select)
        listValues = []
        listOptions = element.find_elements_by_css_selector("option")
        for value in listOptions:
            listValues.append(self.get_element_attribute(value, "value"))
        return listValues
    
    @keyword
    def return_random_element_With_list_from_list(self, sendedList):
        index = randint(0, (len(sendedList) - 1))
        return sendedList[index]
    
    @keyword
    def return_carousel_type_from_settings_page(self, element):
        text = self.get_text(element)
        textList = str(text).split(str(";"))
        carouselType = textList[1].strip()
        return carouselType
