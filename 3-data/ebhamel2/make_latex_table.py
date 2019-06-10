from enum import Enum


class MultiDimDictionary:
    dictionary = []

    def __init__(self):
        self.dictionary = []

    def __iter__(self):
        return self

    def is_key_in_dictionary(self, key):
        if len(self.dictionary) == 0:
            return False

        if len(self.dictionary) == 0 or len(self.dictionary[0][0]) != len(key):
            return False

        for entry in self.dictionary:
            if entry[0] == key:
                return True

        return False

    def update_key(self, key, replicate):
        if not self.is_key_in_dictionary(key):
            print("Key could not be found in dictionary")
            return

        for entry in self.dictionary:
            found_key = True
            for x in range(0, len(entry[0])):
                if (key[x] != entry[0][x]):
                    found_key = False

            if found_key:
                entry[1].append(replicate[0])

    def add_entry(self, entry):
        if len(self.dictionary) == 0:
            self.dictionary.append(entry)

        if len(entry[0]) != len(self.dictionary[0][0]):
            print("Can't add to dictionary")
            return

        else:
            self.dictionary.append(entry)

    def get_iterable(self):
        return self.dictionary

    def print(self):
        print(self.dictionary)

    def get_key_at_index(self, index):
        return self.dictionary[index][0]

    def get_entry_at_index(self, index):
        return self.dictionary[index][0]

    def get_length(self):
        return len(self.dictionary)



def make_latex_table(file_path):
    writer = open("/Users/emmahamel/Research/test/test" + ".tex", "w+")
    writer.write("\\begin{table}\n \t\\centering\n\t\\begin{tabular}{ccccccc} \\hline\n \t\t# of taxa &# of genes & Species Tree Height & Data Type & Method & Fraction of Replicates & Replicate Numbers \\\\\n\t\t\\hline")

    failure_dictionary = get_failure_stats_from_file(file_path)
    dictionary = failure_dictionary.get_iterable()
    for entry in dictionary:
        to_write_out = "\t"
        for data in entry[0]:
            to_write_out += str(data) 
            to_write_out += "&"

        percentage = float(entry[1][0])/20
        to_write_out += str(percentage)
        to_write_out += "&"
        to_write_out += process_reps(entry[1][1])
        to_write_out += "\\\\"
        writer.write(to_write_out)

    writer.write("\n\t\\end{tabular}")

def get_failure_stats_from_file(file_path):
    multi_key_dictionary = MultiDimDictionary()

    reader = open(file_path, "r+")
    for line in reader:
        line_split = line.split(",")

        if line_split[15] == "NA\n":
            key = [int(line_split[1]), int(line_split[2]), line_split[3], line_split[5], line_split[6]]
            values = [line_split[4]]

            if multi_key_dictionary.is_key_in_dictionary(key):
                multi_key_dictionary.update_key(key, values)

            else:
                new_entry = [key, values]
                multi_key_dictionary.add_entry(new_entry)

    return multi_key_dictionary


def process_reps(reps):
    if len(reps) == 4:
        to_return = ""
        for rep in reps:
            to_return += rep
            to_return += ", "
            return to_return

    else:
        to_return = "All but "
        num_of_reps = 20 - len(reps)
        to_return += str(num_of_reps) 
        to_return += " Failed"
        return to_return

ok = get_failure_stats_from_file("/Users/emmahamel/Research/Phylogeny/tutorials/data-species-trees.csv")
make_latex_table("/Users/emmahamel/Research/Phylogeny/tutorials/data-species-trees.csv")
print(ok.get_length())





