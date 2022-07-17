from typing import List, Dict, Union, Optional
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = list()
carrinho: List[Dict[Produto, int]] = list()


def main() -> None:
    menu()


def menu() -> None:
    print('\033[1;97m-='*40)
    print("Bem-vindo(a)".center(80, '-'))
    print('-='*40)
    print("Geek Shop\033[m".center(80, '-'))

    print('Selecione uma opção abaixo:')
    print(
        '1 - Cadastrar produto\n2 - Listar produtos\n3 - Comprar produto',
        '\n4 - Visualizar carrinho\n5 - Fechar pedido\n6 - Sair do sistema'
    )

    opcao: str = input()

    def switch(op: str) -> None:
        sw = {
            '1': cadastrar_produto,
            '2': listar_produtos,
            '3': comprar_produto,
            '4': visualizar_carrinho,
            '5': fechar_pedido,
            '6': sair
        }
        try:
            return sw[op]()
        except KeyError:
            print('\033[31mOpção inválida!\033[m')
            menu()

    switch(opcao)


def cadastrar_produto() -> None:
    print('Cadastro de Produto'.center(20, '-'))
    print('-='*10)

    produto: Produto = Produto(
        input(
            'Informe o nome do produto: '
        ),
        float(
            input(
                'Informe o preço do produto: '
            )
        )
    )

    produtos.append(produto)
    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Listagem de produtos'.center(20, '-'))
        print('-='*10)

        for produto in produtos:
            print(produto)
            print('-='*10)
            sleep(0.50)
    else:
        print('\033[31mAinda não existem produtos cadastrados!\033[m')
    sleep(2)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print(
            'Informe o código do produto que deseja adicionar ao carrinho:'
            .center(20, '-')
        )
        print('-='*10)
        print('Produtos Disponíveis'.center(20, '='))
        for p in produtos:
            print(p)
            print('-='*10)
            sleep(0.50)
        codigo: int = int(input())
        produto: Optional[Produto] = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: Optional[int] = item.get(produto)
                    if quant:
                        item[produto] += 1
                        print(
                            f'O produto {produto.nome} agora possui {item[produto]} unidades no carrinho.'
                        )
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod: dict = {produto: 1}
                    carrinho.append(prod)
                    print(
                        f'O produto {produto.nome} foi adicionado ao carrinho.'
                    )
                    sleep(2)
                    menu()

            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'\033[31mO produto com código {codigo} não foi encontrado\033[m')
            sleep(2)
            menu()
    else:
        print('\033[31mAinda não existem produtos para vender \033[m')
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('\033[1;97mProdutos no carrinho\033[m'.center(20, '-'))
        print('-='*10)

        for item in carrinho:
            for dados in item.items():
                print(f'Produto: {dados[0]} - Quantidade: {dados[1]}')
                print('-='*10)
                sleep(0.50)
    else:
        print('\033[31mAinda não existem produtos no carrinho!\033[m')
    sleep(2)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do carrinho'.center(20, '-'))
        for item in carrinho:
            for dados in item.items():
                print(f'Produto: {dados[0]} - Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('-='*10)
                sleep(0.50)
        print(f'\033[1;97mSua fatura é {formata_float_str_moeda(valor_total)}\033[m')
        print('-='*10)
        cartao()
        print('-='*10)
        sleep(3)
        print('Volte sempre!')
        carrinho.clear()
    else:
        print('\033[31mAinda não existem produtos no carrinho!\033[m')
    sleep(2)
    menu()


def sair():
    print('Volte sempre!')
    sleep(2)
    exit(0)


def pega_produto_por_codigo(codigo: int) -> Union[Produto, None]:
    p: Union[Produto, None] = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto

    return p


def cartao() -> int:
    num: int = int(input('Digite o número do cartão: '))
    senha: int = int(input('Digite a senha do cartão: '))

    return num and senha


if __name__ == '__main__':
    main()
