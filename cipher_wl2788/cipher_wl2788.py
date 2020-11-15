def cipher(text, shift, encrypt=True):
    """
    Function to encipher or decipher the string by using different shift number.
    
    Parameters
    ----------
    text : string
        A string that you wish to encipher or decipher.
    shift : integer
        An integer that you wish to shift.
    encrypt : boolean
        A boolean that you would like to encrypt string or not.
  
    Returns
    -------
    string
        The text after being encrypted or decrypted 
        
    Example
    -------
    >>> from cipher_wl2788 import cipher_wl2788
    >>> text = "happy"
    >>> shift = 1
    >>> cipher_wl2788.cipher(text, shift, encrypt = True)
    'ibqqz'
    
    """
       
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text