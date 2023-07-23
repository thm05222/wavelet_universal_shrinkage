def wavelet_universal_shrinkage(data,name_of_wavelet = 'sym2',decomposition_level = 5,shrinkage_mode = 'soft'):
    coeffs = pywt.wavedec(data,name_of_wavelet,level=decomposition_level)
    mad = np.abs(np.abs(coeffs[-1])-np.abs(coeffs[-1]).mean()).mean()
    threshold = mad*np.sqrt(2*np.log(df.__len__()))/0.6745
    coeffs_thresholded = list()
    for item in coeffs:
        coeffs_thresholded.append(pywt.threshold(item,threshold,mode = shrinkage_mode))
    data_rec = pywt.waverec(coeffs_thresholded,name_of_wavelet)
    return data_rec