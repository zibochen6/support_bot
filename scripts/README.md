## 脚本介绍



`clean_md_export.py`清理爬取到的文档，并导出保存到新的文件夹

清理规则：

**specifications** 表格大量无用字符

图片链接无实际回答帮助







```bash
python build_database.py build --docs wiki_pages_cleaned --out faiss_store --model BAAI/bge-m3 --max-tokens 420 --overlap-tokens 60 --min-tokens 30 --batch-size 32


#query
python build_database.py build ^
  --docs wiki_pages_cleaned ^
  --out faiss_store ^
  --model BAAI/bge-m3 ^
  --max-tokens 420 ^
  --overlap-tokens 60 ^
  --min-tokens 30 ^
  --batch-size 32


```



