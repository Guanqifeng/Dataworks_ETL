import docx
def dox_modle():
    table_of_list = [('商户注册名称*','拓展渠道','广西分公司')]
def read_docx(file_name):
    doc = docx.Document(file_name)
    return doc
def read_table_of_docx(doc,file_name):
    for table in doc.tables:  # 遍历所有表格
        print('----table------')
        hdr_cells = table.rows[4].cells
        hdr_cells[2].text = 'ggggg'
        print(hdr_cells[1].text)
        print(hdr_cells[2].text)
        print(hdr_cells[3].text)
        doc.save(file_name)
def main(file_name):
    getDoc = read_docx(file_name)
    read_table_of_docx(getDoc,file_name)
if __name__ == '__main__':
    file_name = 'C:\\Users\\Administrator\\Desktop\\通联支付网络服务股份有限公司当面付业务协议-模板_test.docx'
    main(file_name)