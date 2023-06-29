"""
Encode and Decode Strings

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).

"""

class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        """
        Solution use delimiter chr(257) in between words 
        """
        if len(strs) == 0: 
            return chr(258)
        
        # encode here is a workaround to fix BE CodecDriver error
        return chr(257).join(x for x in strs)
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        if s == chr(258): 
            return []
        return s.split(chr(257))



class Codec:
    def len_to_str(self, x):
        """
        Encodes length of string to bytes string
        abc de ccc
        0003abc0002de0003ccc

        each chunk is preceded by its 4 byte size

        1. encode length of x into 4 bytes 8bits, 8bits, 8bits, 8bits

        0xff -> 11111111

        x = 0
        bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]
        if x = 0 bytes -> ['\x00', '\x00', '\x00', '\x00'] 0 0 0 0
        if x = 12 byes -> ['\x0c', '\x00', '\x00', '\x00'] 1 0 0 0
        """
        x = len(x)
        bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]
        bytes.reverse()
        bytes_str = ''.join(bytes)
        return bytes_str
    
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        # encode here is a workaround to fix BE CodecDriver error
        return ''.join(self.len_to_str(x) + x for x in strs)
        
    def str_to_int(self, bytes_str):
        """
        Decodes bytes string to integer.
        """
        result = 0
        for ch in bytes_str:
            result = result * 256 + ord(ch)
        return result
    
    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        i, n = 0, len(s)
        output = []
        while i < n:
            length = self.str_to_int(s[i: i + 4])
            i += 4
            output.append(s[i: i + length])
            i += length
        return output