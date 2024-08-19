reStructuredText（RST、ReST或reST）是一種用於文字資料的檔案格式，主要用於Python 程式語言社群的技術文件。 reStructuredText. reStructuredText logo. 副檔名 .rst.

## Sphinx
Sphinx是一個功能強大的文件產生器，具有許多用於編寫技術文件的強大功能，包括：產生網頁，可列印的PDF，電子閱讀器的文檔（ePub），以及更多來自相同來源的文檔。可以使用reStructuredText或Markdown 編寫文檔。


## 安裝相依套件
使用pip安裝軟體包

```
pip install sphinx sphinx_rtd_theme
```

## 建立專案
```
mkdir wiki
cd wiki
sphinx-quickstart
```

![](https://images.ukx.cn/abcdocker/cluswqb0yfgcxwwzs73ay1fy/image_1d5ble14g12i35jd15mv6ja1hbr2i.png)

## 編譯

```
make clean
make html
```


### markdown語法編寫

```
pip install myst_parser
```
Then in your conf.py:
```
extensions = ['myst_parser']
```

### 輸出PDF
參考
- [使用rst2pdf轉PDF](https://chwang12341.medium.com/coding%E8%B5%B7%E4%BE%86-python%E5%B7%A5%E5%85%B7-sphinx%E6%93%8D%E4%BD%9C%E6%95%99%E5%AD%B8-%E4%BA%8C-%E5%A6%82%E4%BD%95%E5%B0%87restructured-text-rst-%E6%96%87%E4%BB%B6%E8%BD%89%E6%8F%9B%E6%88%90pdf-latex%E8%88%87rst2pdf%E6%96%B9%E6%B3%95%E6%95%99%E5%AD%B8-6408bd4d3a3e)



## Reference
- [Sphinx操作教學介紹](https://chwang12341.medium.com/coding%E8%B5%B7%E4%BE%86-python%E5%B7%A5%E5%85%B7-sphinx%E6%93%8D%E4%BD%9C%E6%95%99%E5%AD%B8-%E4%BA%8C-%E5%A6%82%E4%BD%95%E5%B0%87restructured-text-rst-%E6%96%87%E4%BB%B6%E8%BD%89%E6%8F%9B%E6%88%90pdf%E6%96%87%E4%BB%B6-latex%E8%88%87rst2pdf%E6%96%B9%E6%B3%95%E6%95%99%E5%AD%B8-4f017bf857a4)
- [Markdown with Sphinx Quick Start](https://cerodell.github.io/sphinx-quickstart-guide/build/html/markdown.html)
- [Sphinx建立部落格](https://i4t.com/3587.html)
- [Sphinx + MyST + Markdown for Static HTML Pages](https://www.lucasshen.com/notes/sphinx-md2html/sphinx-md2html)

reStructuredText（RST、ReST或reST）是一種用於文字資料的檔案格式，主要用於Python 程式語言社群的技術文件。 reStructuredText. reStructuredText logo. 副檔名 .rst.

## Sphinx
Sphinx是一個功能強大的文件產生器，具有許多用於編寫技術文件的強大功能，包括：產生網頁，可列印的PDF，電子閱讀器的文檔（ePub），以及更多來自相同來源的文檔。可以使用reStructuredText或Markdown 編寫文檔。


## 安裝相依套件
使用pip安裝軟體包

```
pip install sphinx sphinx - autobuild sphinx_rtd_theme
```

## 建立專案
```
mkdir wiki
cd wiki
sphinx-quickstart
```

![](https://images.ukx.cn/abcdocker/cluswqb0yfgcxwwzs73ay1fy/image_1d5ble14g12i35jd15mv6ja1hbr2i.png)

## 編譯

```
make clean
make html
```


### markdown語法編寫

```
pip install myst_parser
```
Then in your conf.py:
```
extensions = ['myst_parser']
```

### 輸出PDF
參考
- [使用rst2pdf轉PDF](https://chwang12341.medium.com/coding%E8%B5%B7%E4%BE%86-python%E5%B7%A5%E5%85%B7-sphinx%E6%93%8D%E4%BD%9C%E6%95%99%E5%AD%B8-%E4%BA%8C-%E5%A6%82%E4%BD%95%E5%B0%87restructured-text-rst-%E6%96%87%E4%BB%B6%E8%BD%89%E6%8F%9B%E6%88%90pdf-latex%E8%88%87rst2pdf%E6%96%B9%E6%B3%95%E6%95%99%E5%AD%B8-6408bd4d3a3e)



## Reference
- [Sphinx操作教學介紹](https://chwang12341.medium.com/coding%E8%B5%B7%E4%BE%86-python%E5%B7%A5%E5%85%B7-sphinx%E6%93%8D%E4%BD%9C%E6%95%99%E5%AD%B8-%E4%BA%8C-%E5%A6%82%E4%BD%95%E5%B0%87restructured-text-rst-%E6%96%87%E4%BB%B6%E8%BD%89%E6%8F%9B%E6%88%90pdf%E6%96%87%E4%BB%B6-latex%E8%88%87rst2pdf%E6%96%B9%E6%B3%95%E6%95%99%E5%AD%B8-4f017bf857a4)
- [Markdown with Sphinx Quick Start](https://cerodell.github.io/sphinx-quickstart-guide/build/html/markdown.html)
- [Sphinx建立部落格](https://i4t.com/3587.html)
- [Sphinx + MyST + Markdown for Static HTML Pages](https://www.lucasshen.com/notes/sphinx-md2html/sphinx-md2html)
- [Host your documentation on ReadTheDocs : Step-by-step guide](https://www.youtube.com/watch?v=PO4Zd-6a6fAhttps://www.youtube.com/watch?v=PO4Zd-6a6fA)# sphinx-tutorial
