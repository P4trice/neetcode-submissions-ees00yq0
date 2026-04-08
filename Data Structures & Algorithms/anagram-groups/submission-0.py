class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a dict per entry with (character, nums_of_appearances)
        # Sort the dict
        # compare to existing dicts for anagram group
        # append original string to that list
        output = []
        anagrams = []
        for s in strs:
            array = list(s)
            array.sort()
            if array in anagrams:
                output[anagrams.index(array)].append(s)
            else:
                anagrams.append(array)
                output.append([])
                output[anagrams.index(array)].append(s)

        return output