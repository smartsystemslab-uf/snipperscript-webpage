# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib.request, json
from urllib.parse import quote




def read_json_file(filename):
    
    with open(filename, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
        return data


def read_json_file_online(url_filename):

    with urllib.request.urlopen(url_filename) as url:
        data = json.loads(url.read().decode())
        return data
    

def write_str_to_file(str_data, filename):    
    with open(filename, "w") as text_file:
        text_file.write(str_data)


def build_html_str(json_dblp_list):
    res_hits = sorted(json_dblp_list, key=lambda x : x["info"]["year"], reverse=True)
    
    print("Total number of papers: ", len(res_hits))
    lastest_year = None
    
    books_html_str = '<h2>BOOKS & BOOK CHAPTERS</h2>\n <ol>'
    journal_html_str = '<h2>JOURNAL</h2>\n <ol>'
    papers_html_str = '<h2>CONFERENCE & WORKSHOP</h2>\n <ol>'
    
    for idx, elt in enumerate(res_hits):
        
        authors_name = ""
        
        if isinstance(elt["info"]["authors"]["author"],dict):
            authors_name = "<strong>" + str(elt["info"]["authors"]["author"]["text"]) + "</strong>"
        else:
            authors_name = []
            for author in elt["info"]["authors"]["author"]:
                if "christophe" in str(author).lower():
                    authors_name.append("<strong>" + str(author["text"]) + "</strong>")
                else:
                    authors_name.append(str(author["text"]))
            authors_name = ", ".join(authors_name)
        
        publication_year = elt["info"]["year"]
        paper_title = elt["info"]["title"]
        paper_type = elt["info"]["type"] # Journal or Conference
        paper_venue = None #
        paper_volume = None #
        paper_doi = None #
        paper_url_ee = None #
        if "venue" in elt["info"]:
            paper_venue = elt["info"]["venue"]

            
        if "volume" in elt["info"]:
            paper_volume = elt["info"]["volume"]

           
        if "doi" in elt["info"]:
            paper_doi = elt["info"]["doi"]

           
        if "ee" in elt["info"]:
            paper_url_ee = elt["info"]["ee"]
        elif "url" in elt["info"]:
            paper_url_ee = elt["info"]["url"]
            # print("No EE URL - url:", elt["info"]["url"])
           
        
        # print("idx:", idx, ", publication year:", publication_year, ", paper_type:", paper_type)

        html_item_str = "<li>" + authors_name +", " + str(paper_title) + ", " + str(paper_type) + " (" + str(paper_venue) + "), Vol. " +  str(paper_volume) + ", " + str(publication_year) + ", " + str(paper_doi) + ". [<a href=\"" + str(paper_url_ee) + "\"><b>link</b></a>]</li>\n"
        
        if "book" in paper_type.lower():
            books_html_str = books_html_str + html_item_str
        elif "journal" in paper_type.lower():
            journal_html_str = journal_html_str + html_item_str
        else:
            
            if lastest_year != publication_year: 
                lastest_year = publication_year
                
                papers_html_str = papers_html_str + "<h3>" + publication_year + "</h3>\n" + html_item_str
            else:
                papers_html_str = papers_html_str + html_item_str
    
    books_html_str = books_html_str + "</ol>"
    journal_html_str = journal_html_str + "</ol>"
    papers_html_str = papers_html_str + "</ol>"
    
    final_html_str = books_html_str + '\n' + journal_html_str + '\n' + papers_html_str + '\n'
    return final_html_str
    
    

if __name__ == '__main__':
    # json filename
    filename = 'D:/DATA/Downloads/zoom-data/dr_bobda_publication.json'
    main_author_name = "Christophe Bobda"
    search_link = "https://dblp.org/search/publ/api?q=" + quote(main_author_name) + "&h=1000&format=json"
    print("URL: ", search_link)
    output_file = 'D:/DATA/Downloads/zoom-data/dr_bobda_publication.html'
    
    
    # read json file with all publications
    # jdata = read_json_file(filename)
    jdata = read_json_file_online(search_link)
    
    # Print Json String of data
    # jstr = json.dumps(jdata, ensure_ascii=False, indent=4)
    jstr = json.dumps(jdata['result']['hits']['hit'][2], ensure_ascii=False, indent=4)
    print(jstr)
    
    res_hits = jdata['result']['hits']['hit']
    
    # Generate the html string from the json array list
    final_html_str = build_html_str(res_hits)

    # Write html result file
    write_str_to_file(final_html_str, output_file)



