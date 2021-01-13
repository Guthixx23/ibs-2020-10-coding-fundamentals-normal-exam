class Exam:
    #dummy init function
    def __init__(self):
        pass

    #function to determin unique characters in the string
    def unique_characters(self, str):

        dict = {}
        sol = []

        for i in range(len(str)):
            if str[i] in dict:
                dict[str[i]] += 1
            else:
                dict[str[i]] = 1

        for k,v in dict.items():
            if v == 1:
                sol.append(k)

        return sol


