"""
271. Encode and Decode Strings

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

 Example 1:

Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
Example 2:

Input: dummy_input = [""]
Output: [""]
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] contains any possible characters out of 256 valid ASCII characters.
 

Follow up: Could you write a generalized algorithm to work on any possible set of characters?

"""


from base64 import encode


class Codec:
    
    def len_to_str(self, x: str) -> str:
        # integer is of 4 bytes meaning 00000000 00000000 00000000 00000000 
        # 0xff = 255 ie 2^8 -1 = 8 1's -> 11111111
        #eg: x= 3
        # bit representation: 00000000 00000000 00000000 00000011
        #1. do right shift to fetch the current 8 bits -> i=0 does no right shift
        # val = 00000000 00000000 00000000 00000011  && 11111111 => 00000011 = 3 bytes =[3]
        # i = 1 right shift will give 00000000 00000000 00000000 00000000 -> 00000000 & 11111111 = 00000000 = 0 
        # i = 2 right shift 16 bits 00000000 00000000 00000000 00000000 -> 0000000 & 11111111 = 00000000 = 0
        # i = 3 right shift 24 bits 00000000 00000000 00000000 00000000 -> 0000000 & 11111111 = 00000000 = 0
        # byte would be then [3, 0, 0, 0] reverse it -> [0,0,0,3] chr will make it = ['0','0','0','3]
        x = len(x)
        bytes = [chr((x >> (i*8)) & 0xff) for i in range(4)]
        bytes.reverse()
        bytes_str = ''.join(bytes)
        return bytes_str

    def encode(self, strs: [str]) -> str:
        return ''.join(self.len_to_str(x)+x for x in strs)


    def str_to_int(self, x:str) -> int:
        result = 0
        for ch in x:
            result = result * 256 + ord(ch)
        return result
    
    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        i, n = 0, len(s)
        output = []
        while i < n:
            length = self.str_to_int(s[i:i+4])
            i += 4
            output.append(s[i:i+length])
            i+= length
        return output
    

class Codec1:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if not strs:
            return chr(258)
        return chr(257).join(x for x in strs)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        if s == chr(258):
            return []
        return s.split(chr(257))
        

s = ["Hello","World"]
encoded_str = Codec().encode(s)
print(encoded_str)
decoded_str = Codec().decode(encoded_str)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))