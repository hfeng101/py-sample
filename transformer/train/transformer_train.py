import argparse
import pytorch.nn as nn

class Embedding(nn.Module):
    def __init__(self, inputX):
        print("Init Embedding!")
        self.w2v =

    def Word2Vec(self, input):
        print("Start Word2Vec")
        output=input

        return output

    def PositionEmbedding(self, input):
        print("Start PositionEmbedding")
        output = input

        return output

    def forword(self):

class MultiHeadAttention(nn.Module):
    def __init__(self):
        print("Start MultiHeadAttention")

    def Attention(self):
        print()



class PositionWiseFeedForwardNetwork(nn.Module):
    def __init__(self,d_mol, d_dff):
        print("Init PositionWiseFeedForwardNetwork!")

    def AddNorm(self, input):
        print()

    def MLP(self, input):
        print()


class Encoder(nn.Module):
    def __init__(self):
        print()

    def Forward(self):
        print()


class Decoder(nn.Module):
    def __init__(self):
        print()

    def Forward(self):
        print()


class Transformer():
    def __init__(self):
        print()

    def Forword(self):
        print()

def Train(dim=32, heads=4, encoder_lays=3, data_path="./data"):
    print(f"Start Training, dim is {dim}, heads is {heads}, encoder layers is {encoder_lays}")

    #加载数据
    dataset = utils.data()


if __name__ == "__main__":
    print()
    parser = argparse.ArgumentParser
    parser.add_argument("--dim", type=int, help="change the model dimension!")
    parser.add_argument("--heads", type=int, help="change the multi attention heads!")
    parser.add_argument("--encode_layers", type=int, help="change the numbers of layers in the model encoder&decoder")
    parser.add_argument("--dataset_path", type=str, help="root path of the dataset")

    args = parser.parse_args()

    args = dict(filter(lambda x:x[1],vars(args).items()))
    Train(**args)