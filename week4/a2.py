def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count = 0
    for char in dna:
      if char in nucleotide:
        count = count + 1
    return count


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def 𝚒𝚜_𝚟𝚊𝚕𝚒𝚍_𝚜𝚎𝚚𝚞𝚎𝚗𝚌𝚎(dna):
    for char in dna:
      if not char in 'ATCG':
          return False
    return True

def 𝚒𝚗𝚜𝚎𝚛𝚝_𝚜𝚎𝚚𝚞𝚎𝚗𝚌𝚎(dna1, dna2, index):
    return dna1[:index] + dna2 + dna1[index:]
