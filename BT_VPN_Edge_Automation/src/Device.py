import xlrd

class Device:
    def __init__(self,name):
        workbook = xlrd.open_workbook(r'../devices/device_list.xlsx')
        for sheet in workbook.sheets():
            for row in range(sheet.nrows):
                column = 0
                if sheet.cell(row, column).value == name:
                    self.ip = str(sheet.cell(row, 1).value)
                    self.username = str(sheet.cell(row, 2).value)
                    self.password = str(sheet.cell(row, 3).value)
                    self.enpassword = str(sheet.cell(row, 4).value)
                    self.ospf_id = str(sheet.cell(row, 5).value)
                    self.bgp_id = str(sheet.cell(row, 6).value)
                    print(self.ip, self.username, self.password, self.enpassword, self.ospf_id, self.bgp_id)
    #def SET_IP(self,given_ip):
        #self.ip= given_ip
        #return self
    def GET_IP(self):
        return self.ip
    def GET_USERNAME(self):
        return self.username
    def GET_PASSWORD(self):
        return self.password
    def GET_ENPASSWORD(self):
        return self.enpassword
    def GET_OSPF_ID(self):
        return self.ospf_id
    def GET_BGP_ID(self):
        return self.bgp_id




























