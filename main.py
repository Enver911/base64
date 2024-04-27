from math import ceil, floor


class Base64:
    base64_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    base64_index_char = {index: char for index, char in enumerate(base64_letters)}
    base64_char_index = {char: index for index, char in enumerate(base64_letters)}
    
    @classmethod
    def decode(cls, base64: str):
        base64 = base64.rstrip("=") # deleting suffix
        base64_indexes = [cls.base64_char_index.get(char) for char in base64] # dec -> sixtets
        bin_list = [bin(index)[2:].rjust(6, "0") for index in base64_indexes] # sixtets list
        bin_string = "".join(bin_list) # sixtets string
        
        length = floor(len(bin_string) / 8) * 8 # new length for octets
        bin_string = bin_string[:length] # octets string
        
        bin_list = [bin_string[i: i + 8] for i in range(0, len(bin_string), 8)] # octets list
        
        string_unicode = [int(bin, 2) for bin in bin_list] # octets list -> unicode
        string = "".join(chr(code) for code in string_unicode)
        
        return string
        

    
    @classmethod
    def encode(cls, string: str):
        string_unicode = [ord(char) for char in string] # string -> unicode 
        
        bin_list = [str(bin(code))[2:].rjust(8, "0") for code in string_unicode] # unicode -> octets list
        bin_string = "".join(bin_list) # octets string
        suffix = {0: "", 1: "=", 2: "=="}[len(bin_string) % 3] # "" or "=" or "==" in the end 
        
        length = (ceil(len(bin_string) / 6)) * 6 # new length for sixtets
        bin_string = bin_string.ljust(length, "0") 
            
        bin_list = [bin_string[i: i + 6] for i in range(0, len(bin_string), 6)] #sixtets list
        base64_indexes = [int(bits, 2) for bits in bin_list] # sixtets -> dec
        
        base64 = "".join(cls.base64_index_char.get(index) for index in base64_indexes) + suffix # result
        
        return base64