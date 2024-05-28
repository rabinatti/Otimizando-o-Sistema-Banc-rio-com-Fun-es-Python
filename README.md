# Bootcamp da [DIO](https://web.dio.me/)

Projeto realizado como desafio no Bootcamp da [DIO](https://web.dio.me/), [Python AI Backend Developer](https://web.dio.me/track/coding-future-vivo-python-ai-backend-developer). 

**Desafio:** Otimizando o Sistema Bancário com Funções Python

## Linguagem utilizada:
* Python

## Descrição e regras do desafio:
Neste desafio, você terá a oportunidade de otimizar o Sistema Bancário previamente desenvolvido com o uso de funções Python. O objetivo é aprimorar a estrutura e a eficiência do sistema, implementando as operações de depósito, saque e extrato em funções específicas. Você terá a chance de refatorar o código existente, dividindo-o em funções reutilizáveis, facilitando a manutenção e o entendimento do sistema como um todo. Prepare-se para aplicar conceitos avançados de programação e demonstrar sua habilidade em criar soluções mais elegantes e eficientes utilizando Python.

## Objetivo Geral:
Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.

## Desafio:
Precisamos deixar nosso código mais modularizado, para isso, vamos criar funções para as operações existentes: sacar, depositar e vizualizar extrato. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário).

## Separação em Funções:
Devemos criar funções para todas as operações do sistema. Para axercitar tudo o que aprendemos neste módulo, cada função vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida por você da forma que achar melhor.

### Saque
A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: **saldo, valor, extrato, limite, numero_saques, limite_saques.** Sugestão de retorno: **saldo e extrato.**

### Depósito
A função depósito deve receber os argumetnos apenas por posição (positional only). Sugestão de argumentos: **saldo, valor, extrato.** Sugestão de retorno: **saldo e extrato.**

### Extrato
A função extrato deve receber os argumetnos por posição e nome (positional only e keyword only). Argumentos posicionais: **saldo**, agmentos nomeadors: **extrato**.

### Novas Funções
Precisamos criar duas novas funções: **criar usuário** e **criar conta corrente**. Fique a vontade para adicionar mais funções, exemplo: **listar contas**.

### Criar usuário(Cliente)
O programa deve armazenar os usuários em uma lista, um usuário é composto por: **nome, data de nascimento, cpf** e **endereço**. O ebdereço é uma string com o formato: **logadouto, número - bairro - cidade/sigla estado**. Deve ser armazenado somente os números do CPF(como string). Não podemos cadastrar 2 usuários com o mesmo CPF.

### Criar Conta Corrente
O programa devew armazenar contas em uma lista, uma conta é composta por agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.