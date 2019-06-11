dc = [
    (86, "China"),
    (91, "India"),
    (1, "United States"),
    (62, "Indonesia"),
    (880, "Bangladesh"),
    (234, "Nigeria"),
    (7, "Russia"),
    (81, "Japan")
]
# 调换国家名country和区域编码code,并推导为字典
country_code = {country: code for code, country in dc}
print(country_code)

# 字典推导为字典,用区域编码code做key
result = {code: country.upper() for country, code in country_code.items() if code < 66 if code > 2}
print(result)

# 字典推导为列表,用国家名country
country_code1 = [ country for code, country in dc]
print(country_code1)

# 字典推导为列表,用国家名country,放弃区域编码code,在这里用下划线 _
country_code1 = [ country for _, country in dc]
print(country_code1)

country_code2 = [str(code) + "," + country for code, country in dc]
print(country_code2)

