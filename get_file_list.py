def get_file_list(path,file_type = 'csv',include_keyword = None,exclude_word = None,size = 0):
  l = []
  for root,subdirs,files in os.walk(path):
    if os.path.join(root,fn).endswith(file_type):
      l.append(os.path.join(root,fn))
  ret = [x for x in l if os.path.isfile(x)]
  if include_keyword is not None:
    ret = [x for x in ret if include_keyword in os.path.basename(x)]
  if exclude_keyword is not None:
    ret = [x for x in ret if exclude_keyword not in os.path.basename(x)]
    
  if size>0:
    ret = [x for x in ret if os.path.getsize(x) >= size]
    
  return ret
