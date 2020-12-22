def slices(series, length):
    series_len = len(series)
    if series_len <= 0 or series_len < length or length <= 0:
        raise ValueError('Invalid series length or chunk length.')
    else:
        results = [series[i:i+length] for i, s in enumerate(series) if i + length <= series_len] 
        return results
