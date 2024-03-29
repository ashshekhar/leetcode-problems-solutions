#
# @lc app=leetcode id=68 lang=python
#
# [68] Text Justification
#

# @lc code=start
class Solution:
  	# Why slots: https://docs.python.org/3/reference/datamodel.html#slots
    # TLDR: 1. faster attribute access. 2. space savings in memory.
    # For letcode problems this can save ~ 0.1MB of memory <insert is something meme>
    __slots__ = ()
	
    def fullJustify(self, words, maxWidth):
	    # Init return array in which, we'll store justified lines
        lines = []
		# current line width
        width = 0
		# current line words
        line = []
        
        for word in words:
			# Gather as many words that will fit under maxWidth restrictions.
			# Line length is a sum of:
			# 1) Current word length
			# 2) Sum of words already in the current line
			# 3) Number of spaces (each word needs to be separated by at least one space)
            if (len(word) + width + len(line)) <= maxWidth:
                width += len(word)
                line.append(word)
                continue
            
			# If the current line only contains one word, fill the remaining string with spaces.
            if len(line) == 1:
				# Use the format function to fill the remaining string with spaces easily and readable.
				# For letcode police, yes you could do something like:
                line = " ".join(line)
                line += " " * (maxWidth - len(line))
                lines.append(line)

            else:
			    # Else calculate how many common spaces and extra spaces are there for the current line.
				# Example:
                #  line = ['a', 'computer.', 'Art', 'is']
				# width left in line equals to: maxWidth - width: 20 - 15 = 5
				# len(line) - 1 because to the last word, we aren't adding any spaces
				# Now divmod will give us how many spaces are for all words and how many extra to distribute.
				# divmod(5, 3) = 1, 2
				# This means there should be one common space for each word, and for the first two, add one extra space.
                space, extra = divmod(maxWidth - width, len(line) - 1)
                
                i = 0
				# Distribute extra spaces first
				# There cannot be a case where extra spaces count is greater or equal to number words in the current line.
                while extra > 0:
                    line[i] += " "
                    extra -= 1
                    i += 1
                    
                # Distribute common spaces
				# Join line array into a string by common spaces, and append to justified lines.
                lines.append((" " * space).join(line))
            
			# Create new line array with the current word in iteration, and reset current line width as well.
            line = [word]
            width = len(word)
        
		# Last but not least format last line to be left-justified with no extra space inserted between words.
		# No matter the input, there always be the last line at the end of for loop, which makes things even easier considering the requirement.
        line = " ".join(line)
        line += " " * (maxWidth - len(line))
        lines.append(line)

        return lines
# @lc code=end

