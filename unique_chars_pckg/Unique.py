class Exam:

    def __init__(self):
        pass


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


