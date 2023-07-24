#Wavelet Universal Shrinkage
The "universal" term means the universal threshold method proposed by D.L. Donoho et al[1]. 
This project is a simple de-noise method with the help of PyWavelets package.
##manual
The wavelet_universal_shrinkage function returns a denoised array with the same dimension as your input data.
###Input
data: the time series you wants to de-noise, 1-D data ONLY(if you wants to process higher dimension data, plz contact the author).

name_of_wavelet: To specify which type of mother wavelet you would want to adopt. The list of options can be access through "pywt.wavelist()".

decomposition_level: The level of wavelet decomposition in this process. The maximum level available for your input can be calculated as log2(data_length/(filter_length-1)) or "pywt.dwt_max_level()".

shrinkage_method: {‘soft’, ‘hard’, ‘garrote’, ‘greater’, ‘less’} Mathematical representation not provided.

##references
[1] Donoho, D. L., Johnstone, I. M., Kerkyacharian, G., & Picard, D. (1997). Universal near Minimaxity of Wavelet Shrinkage. Festschrift for Lucien Le Cam, 183–218. https://doi.org/10.1007/978-1-4612-1880-7_12 

