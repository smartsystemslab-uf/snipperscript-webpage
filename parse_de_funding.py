# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 22:19:44 2020

@author: Erman Nghonda
"""


import urllib.request, json
from urllib.parse import quote
import pandas as pd
import datetime

from urllib.parse import urlparse


def read_excel_file(url_filename):

    with pd.ExcelFile(url_filename) as xls:
        sheetX = xls.parse(0) #Parse the first sheet (or specify the sheeet number)
        return sheetX


def url_ok(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

    

    

def write_str_to_file(str_data, filename):    
    with open(filename, "w") as text_file:
        text_file.write(str_data)


def build_html_str(json_dblp_list):
    
    return final_html_str
    
    

if __name__ == '__main__':
    # json filename
    filename = 'D:/DATA/Downloads/zoom-data/De-Funding Opportunities.xlsx'
    output_file = 'D:/DATA/Downloads/zoom-data/de_funding_table.html'
    
    sheetX = read_excel_file(filename)
    
    print(sheetX["Description"][3])
    
    table_str = '''
<table style="width: 100%;">
<tbody>
<tr>
<th>Opportunity</th>
<th>Agency</th>
<th>Description</th>
<th>CE-Relevance</th>
<th>Deadline</th>
<th>Links</th>
</tr>'''

    
    for line in range(sheetX["Links"].size):

        if str(sheetX["Opportunity"][line]) == 'nan':
            continue
        
        line_tr_html = "<tr>\n"
        
        m_date = sheetX["Deadline"][line]
        if isinstance(m_date, datetime.date):
            m_date = m_date.strftime("%B %d, %Y")
            
        m_url = str(sheetX["Links"][line])
        if url_ok(m_url):
            m_url = "<td><a href=\"" + str(sheetX["Links"][line]) + "\"><b>Program Webpage</b></a></td>\n"
        else:
            m_url = "<td><b>Not defined</b></td>\n"
            
            
        
        Opportunity = "<td>" + str(sheetX["Opportunity"][line]) + "</td>\n"
        Agency = "<td>" + str(sheetX["Agency"][line]) + "</td>\n"
        Description = "<td>" + str(sheetX["Description"][line]) + "</td>\n"
        CE_Relevance = "<td>" + str(sheetX["CE-Relevance"][line]) + "</td>\n"
        Deadline = "<td>" + str(m_date) + "</td>\n"
        Links = m_url
    
        
        line_tr_html += (Opportunity + Agency + Description + CE_Relevance + Deadline + Links)
        line_tr_html += "</tr>\n"
    
        table_str += line_tr_html
    
    
        print(line_tr_html)
    
    table_str += '''
</tbody>
</table>'''

     # Write html result file
    write_str_to_file(table_str, output_file)
    
    
    
    
    
