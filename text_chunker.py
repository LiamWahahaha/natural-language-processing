from nltk.corpus import brown


def chunker(input_data, N):
    '''
    :param input_data: text documents
    :param N: every chunk consists of at most N words
    :return:
    '''
    input_words = input_data.split(' ')
    output = []

    cur_chunk = []
    count = 0
    for word in input_words:
        cur_chunk.append(word)
        count += 1
        if count == N:
            output.append(' '.join(cur_chunk))
            cur_chunk = []
            count = 0

    output.append(' '.join(cur_chunk))

    return output


if __name__ == '__main__':
    input_data = ' '.join(brown.words()[:12000])

    chunk_size = 700

    chunks = chunker(input_data, chunk_size)

    print('\nNumber of text chunks = ', len(chunks), '\n')

    for i, chunk in enumerate(chunks):
        print('Chunk', i+1, '==>', chunk[:50])