sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

min_dict=min(sample_dict, key=lambda k:sample_dict[k])

print (min_dict)