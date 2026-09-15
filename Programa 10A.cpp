#include <iostream>
#include <string>
#include <vector>

struct agenda{
    std::string nomes;
    std::string enderecos;
    std::string telefones;
};


std::vector<agenda> cadastro(){
    std::vector<agenda> cadastros;

    agenda registro;
    for(int i = 0; i < 10; ++i){
        std::cout << "Digite o nome: "; std::getline(std::cin, registro.nomes); 
        std::cout << "Digite o endereço: "; std::getline(std::cin, registro.enderecos);
        std::cout << "Digite o telefone: "; std::getline(std::cin, registro.telefones);
        cadastros.push_back(registro);
    }

    return cadastros;
}

std::vector<agenda> pesquisar(std::vector<agenda> cadastros){
    std::string resp = "sim";
    std::string pesq;
    bool acha;
    int i = 0;

    while(resp == "sim"){
        std::cout << "Digite sua pesquisa: "; std::getline(std::cin, pesq);
        acha = false;
        for(i = 0; i < cadastros.size(); ++i){
            if(pesq == cadastros[i].nomes){
                acha = true;
                break;
            }
        }
        if(acha == true){
            std::cout << pesq << " Foi encontrado na posicao " << i << std::endl;
        } else {
            std::cout << pesq << " Nao foi encontrado" << std::endl;
        }
        std::cout << "Deseja continuar a pesquisar: "; std::cin >> resp;
        std::cin.ignore(1000, '\n');
    }
    return cadastros;
}

std::vector<agenda> classificar(std::vector<agenda> cadastros){
    if(cadastros.empty()){
        std::cout << "Não ha dados para classificar" << std::endl;
        return cadastros;
    }
    
    for(int i = 0; i < cadastros.size(); ++i){
        for(int j = i + 1; j < cadastros.size(); ++j){
            if(cadastros[i].nomes > cadastros[j].nomes){
                agenda x = cadastros[j];
                cadastros[j] = cadastros[i];
                cadastros[i] = x;
            }
        }
    }

    return cadastros;
}

std::vector<agenda> apresentar(std::vector<agenda> cadastros){
    for(int i = 0; i < cadastros.size(); i++){
        std::cout << "Nome cadastrado: " << cadastros[i].nomes << std::endl;
        std::cout << "Endereco cadastrado: " << cadastros[i].enderecos << std::endl;
        std::cout << "Telefone cadastrado: " << cadastros[i].telefones << std::endl;
    }

    return cadastros;
}

int main(void){
    std::vector<agenda> cadastros;
    std::vector<agenda> pesquisas;
    std::vector<agenda> classificacoes;
    std::vector<agenda> apresenta;
    int opcao = 0;

    while(opcao != 5){
        std::cout << "Bem-vindo a Agenda" << std::endl;
        std::cout << "Digite 1 para cadastrar" << std::endl;
        std::cout << "Digite 2 para pesquisar" << std::endl;
        std::cout << "Digite 3 para classificar" << std::endl;
        std::cout << "Digite 4 para apresentar" << std::endl;
        std::cout << "Digite 5 para sair" << std::endl;

        std::cout << "Sua opcao e: "; std::cin >> opcao;

        if(opcao == 1){
            std::cin.ignore(1000, '\n');
            cadastros = cadastro();
        }

        if(opcao == 2){
            std::cin.ignore(1000, '\n');
            pesquisas = pesquisar(cadastros);
        }

        if(opcao == 3){
            std::cin.ignore(1000, '\n');
            cadastros = classificar(cadastros);
        }

        if(opcao == 4){
            std::cin.ignore(1000, '\n');
            apresenta = apresentar(cadastros);
        }

        if(opcao <= 0 || opcao > 5){
            std::cout << "Por favor escolha uma opcao valida" << std::endl;
        }
    }

    std::cin.ignore(80, '\n');
    std::cout << "Tecle <Enter> para encerrar...";
    std::cin.get();

    return 0;

}
