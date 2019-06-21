"""
Basic routines for manipulating sequences and alignments
Written by EKM (molloy.erin.k@gmail.com) in October 2016.
"""
import sys


def parse_text(text, skey, ekey):
    """Extract text between start key and end key
    Parameters
    ----------
    text : str
    skey : str
    ekey : str
    Returns
    -------
    Text between start and end keys
    """
    s = text.find(skey)
    if s == -1:
        return "NA"
    else:
        s = s + len(skey)
        e = s + text[s:].find(ekey)
        return text[s:e]


def concatenate(alns, fill_gaps=True):
    """Concatenate a list of alignments into single alignment
    Parameters
    ----------
    alns : list of dictionaries
        alignments
    Returns
    -------
    cat : dict
        concatenated alignment
    """
    if type(alns) is not list:
        raise Exception("Input alignments must be in a list!\n")

    if fill_gaps is False:
        nams = set(alns[0])
        for a in alns[1:]:
            nams = nams.intersection(set(a))
    else:
        nams = []
        for a in alns:
            nams = nams + list(a)
        nams = list(set(nams))

    cat = {}
    for n in nams:
        cat[n] = ''

    for a in alns:
        nch = len(a[list(a)[0]])
        for n in nams:
            cat[n] = cat[n] + a.get(n, '-' * nch)

    return cat


def constrain(seqs1, seqs2):
    """Constrain seqs1 to be on the same set of sequences as seqs2
    Parameters
    ----------
    seqs1 : dict
        sequence data
    seqs2 : dict
        sequence data
    Returns
    -------
    Nothing
    """
    nams = list(set(seqs1) - set(seqs2))
    for n in nams:
        try:
            del seqs1[n]
        except KeyError:
            sys.stdout.write("WARNING: Sequence %s does not exist!"
                             % n)


def get_names_from_fasta(ifil, istext=False):
    """Read the sequence names into a list
     Parameters
     ----------
     ifil: str
           file name
     Returns
     -------
     nams : list of str
    """
    nams = set()

    if istext:
        text = ifil
    else:
        with open(ifil, 'r') as f:
            text = f.read()

    lines = text.split('>')

    for x in text.split('>')[1:]:
        [n, d] = x.split('\n', 1)
        nams = nams.union(set([n]))

    return list(nams)


def guess_format(ifil, istext=False):
    """Guess the format of a file
    Parameters
    ----------
    ifil : str
        file name
    istext : boolean, option
        False, ifil is a file name
        True, ifil is the text from a file
    Returns
    -------
    format : 'fasta' | 'nexus' | 'phylip' | None
    """
    if istext:
        text = ifil
        line = text.split('\n')
    else:
        with open(ifil, 'r') as f:
            line = f.readline().rstrip()
    ws = line.split()

    if ws[0] == "#NEXUS":
        return "nexus"

    if ws[0][0] == ">":
        return "fasta"

    if len(ws) > 1:
        try:
            nsq = int(ws[0])
            nch = int(ws[1])
        except ValueError:
            return None
        return "phylip"

    return None


def keep(seqs, nams):
    """Remove sequences that are not in names
    Parameters
    ----------
    seqs : dict
        sequence data
    nams : list of str
        subset of sequences to keep
    Returns
    -------
    Nothing
    """
    nams = list(set(seqs) - set(nams))
    for n in nams:
        try:
            del seqs[n]
        except KeyError:
            sys.stdout.write("WARNING: Sequence %s does not exist!"
                             % n)


def mask_gaps(seqs, thresh=1.0):
    """Remove columns in an alignment when a certain fraction of sites
       are gaps
    Parameters
    ----------
    seqs : dict
        alignment
    thresh : float between 0 and 1, option
        fraction of gaps needed for column to be removed
    Returns
    -------
    algn : dict
        alignment with gapped columns removed
    """
    import numpy
    from numpy.core.defchararray import startswith

    nams = list(seqs)
    nseq = len(nams)

    data = []
    for n in nams:
        data.append(list(seqs[n]))
    data = numpy.array(data)

    perc = numpy.sum(startswith(data, '-'), axis=0) / float(nseq)
    cols = numpy.where(perc < thresh)[0]
    data = data[:, cols]

    algn = {}
    for i, n in enumerate(nams):
        algn[n] = ''.join(list(data[i, :]))

    return algn


def read(ifil, istext=False):
    """Read sequence data into a dict
    Parameters
    ----------
    ifil : str
    istext : boolean, option
        False, ifil is a file name
        True, ifil is the text from a file
    Returns
    -------
    seqs : dict
           sequence data
    """
    x = guess_format(ifil, istext=istext)
    if x == "fasta":
        seqs = read_fasta(ifil, istext=istext)
    elif x == "nexus":
        seqs = read_nexus(ifil, istext=istext)
    elif x == "phylip":
        seqs = read_phylip(ifil, istext=istext)
    else:
        raise Exception("Unable to recognize input file format!\n")
    return seqs


def read_fasta(ifil, istext=False):
    """Read a fasta file into a dictionary
    Parameters
    ----------
    ifil: str
    istext : boolean, option
        False, ifil is a file name
        True, ifil is the text from a file
    Returns
    -------
    seqs : dict
        sequence data
    """
    seqs = {}

    if istext:
        text = ifil
    else:
        with open(ifil, 'r') as f:
            text = f.read()

    lines = text.split('>')

    for x in text.split('>')[1:]:
        [n, d] = x.split('\n', 1)
        n = ''.join(n.split())
        d = d.replace('\n', '').replace(' ', '')

        if n in seqs:
            sys.stderr.write("WARNING: %s has already been found!\n" % n)

        seqs[n] = d
    return seqs


def read_nexus(ifil, istext=False):
    """Read a nexus file into a dictionary
    Parameters
    ----------
    ifil : str
    istext : boolean, option
        False, ifil is a file name
        True, ifil is the text from a file
    Returns
    -------
    seqs : dict
        sequence data
    """
    seqs = {}

    if istext:
        text = ifil
    else:
        with open(ifil, 'r') as f:
            text = f.read()

    nsq = int(parse_text(text, "ntax=", " "))
    nch = int(parse_text(text, "nchar=", ";"))
    mat = parse_text(text, "matrix", ";")
    if mat == "NA":
        mat = parse_text(text, "Matrix", ";")
    if mat == "NA":
        mat = parse_text(text, "MATRIX", ";")
    if mat == "NA":
        raise("Nexus file has no matrix block!\n")

    lines = mat.split('\n')

    for s in range(len(lines)):
        words = lines[s].split(' ', 1)

        if len(words) > 1:
            n = words[0]
            d = words[1].replace(' ', '').replace('\t', '')

            if n not in list(seqs):
                seqs[n] = ''
            seqs[n] = seqs[n] + d
    return seqs


def read_phylip(ifil, istext=False):
    """Read a phylip file into a dictionary
    Parameters
    ----------
    ifil : str
    istext : boolean, option
        False, ifil is a file name
        True, ifil is the text from a file
    Returns
    -------
    seqs : dict
        sequence data
    """
    seqs = {}

    if istext:
        text = ifil
    else:
        with open(ifil, 'r') as f:
            text = f.read()

    lines = text.split('\n')

    tmp = lines[0].split()
    nsq = int(tmp[0])
    nch = int(tmp[1])

    for s in range(1, len(lines)):
        words = lines[s].split(' ', 1)
        if len(words) > 1:
            n = words[0]
            d = words[1].replace(' ', '').replace('\t', '')
            # Important because of INDELible phylip files...
            if n != "":
                if n not in list(seqs):
                    seqs[n] = ''
                seqs[n] = seqs[n] + d
    return seqs


def remove(seqs, nams):
    """Remove a list of sequences from a dictionary
    Parameters
    ----------
    seqs : dict
        sequence data
    nams : list of str
        subset of sequence to be removed
    Returns
    -------
    Nothing
    """
    assert(type(nams) is list), "Input names must be in a list!"

    for n in nams:
        try:
            del seqs[n]
        except KeyError:
            warn("Sequence %s does not exist!" % n)


def restrict(seqs, s=None, e=None):
    """Restrict an sequence data to a substring specified by start
    and end indices
    Parameters
    ----------
    seqs : dict
        sequence data
    s : int
        start index
    e : int
        end index
    Returns
    -------
    Nothing
    """
    nam = list(seqs)
    nch = len(seqs[nam[0]])

    if s is None:
        s = 0

    if e is None:
        e = nch

    if s < 0:
        raise Exception("Start index is less than 0!\n")

    if s > e:
        raise Exception("Start index is greater than end index!\n")

    if e > nch:
        sys.stderr.write("End index is greater than sequence length!\n")

    for n in nam:
        seqs[n] = seqs[n][s:e]


def write_fasta(seqs, ofil):
    """Write sequence data to file with format fasta
    Parameters
    ----------
    seqs : dictonary
        sequence data
    ofil : str
        file name
    Returns
    -------
    Nothing
    """
    with open(ofil, 'w') as f:
        for n in list(seqs):
            f.write('>' + n + '\n' + seqs[n] + '\n')


def write_nexus(seqs, ofil):
    """Write sequence data to file with format fasta
    Parameters
    ----------
    seqs : dictonary
        sequence data
    ofil : str
        file name
    Return
    ------
    Nothing
    """
    nam = list(seqs)
    nam = sorted(nam, key=lambda n: int(n))  # Important for PAUP* SVDquartets
    nsq = len(nam)
    nch = len(seqs[nam[0]])

    with open(ofil, 'w') as f:
        f.write("#NEXUS\n\n")

        f.write("BEGIN TAXA;\n")
        f.write("    DIMENSIONS NTAX=%d;\n" % nsq)
        f.write("    TAXLABELS\n")
        for n in nam:
            f.write("        %s\n" % n)
        f.write("    ;\n")
        f.write("END;\n\n")

        f.write("BEGIN CHARACTERS;\n")
        f.write("    DIMENSIONS NCHAR=%d;\n" % nch)
        f.write("    FORMAT DATATYPE=DNA" + " GAP=-" +
                " MISSING=?;\n")
        f.write("    MATRIX\n")
        for n in nam:
            f.write("        %s    %s\n" % (n, seqs[n]))
        f.write("    ;\n")
        f.write("END;\n")


def write_phylip(seqs, ofil):
    """Write sequence data to file with format phylip
    Parameters
    ----------
    seqs : dictonary
        sequence data
    ofil : str
        file name
    Returns
    -------
    Nothing
    """
    nam = list(seqs)
    nsq = len(nam)
    nch = len(seqs[nam[0]])

    with open(ofil, 'w') as f:
        f.write("%d %d\n" % (nsq, nch))

        for n in nam:
            f.write(n + " " + seqs[n] + '\n')


def main(args):
    out = None

    alns = []
    for ifil in args.input:
        alns.append(read(ifil))

    if args.keep is not None:
        for aln in alns:
            keep(aln, args.keep)

    if args.restrict:
        for aln in alns:
            restrict(aln, s=args.start, e=args.end)

    if args.concatenate:
        if len(args.input) < 1:
            sys.stdout.write("Nothing to concatenate!")
            sys.exit(1)
        out = concatenate(alns)

    if out is None:
        out = alns[0]

    if args.output is not None:
        if args.format == "fasta":
            write_fasta(out, args.output)
        elif args.format == "nexus":
            write_nexus(out, args.output)
        else:
            write_phylip(out, args.output)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--concatenate",
                        help="Concatenate multiple alignment files",
                        action="store_true")
    parser.add_argument("-r", "--restrict",
                        help="Restrict alignment to substring",
                        action="store_true")

    parser.add_argument("-s", "--start", type=int,
                        help="Start position of substring")
    parser.add_argument("-e", "--end", type=int,
                        help="End position of substring")
    parser.add_argument("-f", "--format", type=str,
                        help="Output alignment format")

    parser.add_argument("-k", "--keep", type=str, nargs='+',
                        help="Sequence names to keep")

    parser.add_argument("-i", "--input", type=str, nargs='+',
                        help="Input alignment file(s)", required=True)
    parser.add_argument("-o", "--output", type=str,
                        help="Output alignment file")

    main(parser.parse_args())
