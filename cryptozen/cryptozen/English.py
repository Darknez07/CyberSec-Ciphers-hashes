import sys
import os

sys.path.append("../")


class English:
    Letters = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower() + " \t\n"
    )
    words = []
    english_words = {}

    def get_english_words(self):
        words = open("dictionary.txt")
        for word in words:
            self.english_words[word.strip("\n")] = None
        words.close()
        # print('{} English words loaded from {}'.format(len(self.english_words),
        #                                                'dictionary.txt'))

    def check_letters(self, messages):
        self.get_english_words()
        counts = 0
        total = 0
        sym_count = 0
        if type(messages) != list:
            raise Exception("Pass the list of lines")
        else:
            if type(messages[0]) != str:
                raise Exception("Pass the list of strings")

        for message in messages:
            total += len(message)
            message = message.split(" ")
            for letter in message:
                count = 0
                for sym in letter:
                    if sym in self.Letters:
                        count += 1
                        sym_count += 1
                if count >= len(letter):
                    counts += count
                    self.words.append(letter.upper())
            if not self.words:
                return 0, 0
            if total == 0:
                return 0, 0
            if counts == 0:
                return 0, 0
                # print(self.words)
                # raise Exception("""The passed text does not have enough
                #                 symbols for alphabets and spaces""")

        return (float(counts / total), float(sym_count / total))

    def check_words(self, messages):
        res = self.check_letters(messages)
        if not self.words:
            return 0, 0
            # raise Exception("""The passed text does not have enough
            #                     symbols for alphabets and spaces""")
        count = 0
        for word in self.words:
            if word in self.english_words.keys():
                count += 1
        try:
            ans = float(count / len(self.words)), float(res[1])
            return ans
        except ZeroDivisionError:
            return 0, 0

    def get_from_files(self, filename):
        lines = []
        if os.path.exists(filename):
            if filename.endswith(".txt"):
                file = open(filename)
                for line in file:
                    lines.append(line.strip("\n"))
            else:
                raise Exception("File not text type")
        else:
            raise Exception("Could not find the file")
        file.close()
        return lines


def main(filename):
    eng = English()
    message = eng.get_from_files(filename)
    ans = eng.check_words(message)
    return ans[0] > 0.5 and ans[1] > 0.5
