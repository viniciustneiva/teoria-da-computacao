maquina = '000101110110111011001101011010110011011011011011001101110111011101001110110111101010011101011111011010011111010111110110100111110110111111010100111111010111111111010100111111011011111111101101001111110111011111110111011001111111010111111110111011000'
entrada = 'B101B'
m_transitions = list(filter(None,list(filter(None,maquina.split('000')))[0].split('00')))

def getItemToUnary(str):
    if(str == '0'):
        return "1"
    elif(str == '1'):
        return "11"
    elif(str == 'B'):
        return "111"

    return "erro"

def getUnaryToItem(str):
    if(str == '1'):
        return '0'
    if(str == '11'):
        return '1'
    if(str == '111'):
        return 'B'

def getNextTransition(total_transitions, actual_state, symbol):
    for c_transition in total_transitions:
        if c_transition[0] == actual_state and c_transition[1] == symbol:
            return c_transition;

    return -1;       
     
def universal_machine(m_transitions, input):
    transitions_tape = []
    state_tape = '1'
    rw_head = 0
    output_tape = ([*input])

    for x in range(len(output_tape)):
        output_tape[x] = getItemToUnary(output_tape[x]);

    for c_transition in m_transitions:
        transitions_tape.append(list(filter(None,c_transition.split('0'))))

    print("FITA 1:", transitions_tape)
    print("FITA 2:", state_tape)
    clone_list = []
    for i in range(len(output_tape)):
        if(i == rw_head and i == 0):
            clone_list = getUnaryToItem(output_tape[i])+'\u0332'
        else:
            clone_list += getUnaryToItem(output_tape[i]);
    print("FITA 3:", ''.join(clone_list))

    move = getNextTransition(transitions_tape, state_tape, output_tape[rw_head])

    while move != -1:
        if move[0] != state_tape and move[1] != output_tape[rw_head]:
            return "ERRO!"
        else:
            state_tape = move[2] # recebe o novo estado
            output_tape[rw_head] = move[3] # faz a troca da palavra

            if move[4] == '11':
                rw_head = rw_head + 1 # move para direita
            else:
                if(rw_head >= 1):
                    rw_head = rw_head - 1 # move para esquerda

            print("FITA 1:", transitions_tape)
            print("FITA 2:", state_tape)
            clone_list = []
            for i in range(len(output_tape)):
                if(i == rw_head):
                    clone_list += getUnaryToItem(output_tape[rw_head])+'\u0332'
                else:
                    clone_list += getUnaryToItem(output_tape[i]);
            print("FITA 3:", ''.join(clone_list))
        move = getNextTransition(transitions_tape, state_tape, output_tape[rw_head]) # movimenta a fita para a proxima transicao


universal_machine(m_transitions, entrada)
