def to_query_string(data):
    lst = []
    for element in data:
        if isinstance(data[element], (str, int)):
            lst.append(f"{element}={data[element]}")
        else:
            for value in data[element]:
                lst.append(f"{element}={value}")
    return "&".join(lst)


print(to_query_string({"bar": [2, 3], "foo": 1}))
