import json
def read_json(addr):
    with open(addr) as reader:
        f = json.load(reader)
    return f


if __name__ == "__main__":
    cuadv1_f = 'Data/full/CUADv1.json'
    test_f = 'Data/five/test.json'
    tsq_f = 'Data/full/train.json'

    # squad_train = 'data/train-v2.0.json'
    # squad_dev = 'data/dev-v2.0.json'
    # cuadv1_f = read_json(cuadv1_f)
    test_f = read_json(test_f)
    tsq_f = read_json(tsq_f)

    cuad_train_test = {'version':'v2.0', 'data':tsq_f['data'][0:50]}
    with open('Data/one/train.json', 'w') as writer:
        json.dump(cuad_train_test, writer)
    for i_d, data_one in enumerate(tsq_f['data']):
        for i_q, qa in enumerate(data_one['paragraphs'][0]['qas']):
            if len(qa['answers']) != 1:
                print(i_d, i_q)


    for i_d, data_one in enumerate(tsq_f['data']):
        for i_q, qas in enumerate(data_one['paragraphs'][0]['qas']):
            if len(qas['answers'])>0 and len(qas['answers'][0]['text'].split())>300:
                print(i_d, i_q,qas)

