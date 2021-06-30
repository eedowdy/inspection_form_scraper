# inspection_form_scraper
Simple TXT to CSV parser

### **Usage instructions:**
1. Convert folder of pdf files to TXT (plain text). Use https://pdftotext.com/. Upload all of your pdf files to the site and press download all. Place your converted txt files into a folder. The converted files may come in a zipped folder that you will need to extract. 
2. Open your script:
> **TO USE COLAB**: Open script from either a link or from Google Drive. Drag your folder of converted TXT files into the files area to the left ot your script. Give your folder a simple name that is easy to type. You will have to put your data into colab like this each time you open the application.
> 
>**TO USE IDLE**: Navigate to the IDLE Python GUI from the start menu or search bar. When you open IDLE you will be greeted with a shell application. This is where any output messages like error message will appear. Navigate to your script from File > Open and then look for pdf_scraper.py wherever you have it saved. 
3. Scroll to the last line of the script document. The line you are looking for should be defaulted to *load_all('/content/txts', 'output.csv')*
4. Replace the first parameter of *load_all*  with the full file path of your directory of TXT files. This should be a string, denoted in Python with apostrophes. 
5. Determine the file path for your output table file. Your filename should end with *.csv*. Replace the second parameter of *load_all* with this csv filename. Make sure you include the full intended path name. This should be a string, denoted in Python with apostrophes. 
6. Run the script:
> **IF ON IDLE**: save from File > Save, then run from Run > Run Module or by pressing F5.
>
> **IF ON COLAB**: navigate to Runtime > Run All. On a local machine you will need to save your changes to the script manually before running. 

7. **IF ON COLAB**: Find the output location of your csv file and double-click. A window should come up to the right of your code where you can preview the file. Right-click your file name back in the left window to download onto your local drive. 
8. Navigate to the local directory where you have saved your file and open it with Excel. If everything looks alright, this file can then be saved as a *.xls* file, or what ever other type of Excel workbook you wish to use.

### **Troubleshooting**
Common issues when parsing files:
1. **If the output csv file is not appearing**:  Most likely you have an issue with your file path. Make sure everything is spelled correctly and that you have given your output file a unique name. In colab, you can keep over writing a csv file as you work, but on a local machine it is likely that the system will request that you give each csv file you save a unique name. 
2. **Some data from form is not appearing in the csv**: Check and see if the pdf form format has changed from what this script was designed for. This code is *not* ment to be extensible, meaning that it will not work on any old pdf form. Some minor changes/additions to the form shouldn't be a problem as long as they follow the form 'Title: Entry'. The colon is how the code determines that something is a piece of data that should be entered in the table.
3. **File Not Found Error**: This will always be caused by an issue with your directory file path. On a local IDE like IDLE, file paths can be tricky. I've found that the best way to get an accurate path is by navigating to my file or folder in File Explorer and copying the full (absolute) path. You will likely have to edit the path that File Explorer gives you to have single forward slashes like '/' instead of double back slashes like ' \ \ '.

*Apologies for the overly long instructions. This program was designed to be able to be modified and run by people with zero coding experience.*
