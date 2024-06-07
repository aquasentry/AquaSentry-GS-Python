# AquaSentry: Contribuindo Para Um Futuro Mais Azul

## Introdução
O AquaSentry é uma empresa dedicada ao desenvolvimento sustentável marinho e decidiu fazer uma campanha para arrecadar fundos. Este sistema permite que usuários se cadastrem, façam login, doem para diferentes causas ambientais, especificamente voltadas para monitoramento e pesquisa sobre mudanças climáticas, proteção dos recifes de corais e restauração de manguezais e ecossistemas costeiros. Além disso, os usuários podem deixar comentários para compartilhar suas opiniões e experiências.

## Funcionalidades
- **Cadastro de Usuários**: Permite que novos usuários se cadastrem fornecendo um nome de usuário e senha.
- **Login de Usuários**: Usuários cadastrados podem fazer login para acessar as funcionalidades do sistema.
- **Página de Arrecadação de Fundos**: Oferece aos usuários a oportunidade de doar para diferentes causas ambientais, com opções para escolher a causa e o valor da doação.
- **Página de Comentários**: Permite aos usuários deixarem comentários sobre o projeto, compartilhando suas opiniões e feedbacks.
- **Logout**: Permite que os usuários saiam de suas contas.

## Estrutura do Código
### Variáveis Globais
- `usuarios`: Lista que armazena os nomes de usuários cadastrados.
- `senhas`: Lista que armazena as senhas dos usuários.
- `saldo_1`, `saldo_2`, `saldo_3`: Variáveis que armazenam os saldos de doações para cada uma das três causas.

### Funções
1. `boas_vindas()`: Exibe uma mensagem de boas-vindas ao usuário.
2. `pagina_cadastro()`: Responsável pelo cadastro e login de usuários.
3. `pagina_inicial()`: Exibe o menu principal após o login bem-sucedido.
4. `pagina_arrecadacao()`: Gerencia as doações para as três causas ambientais.
5. `pagina_comentarios()`: Gerencia os comentários dos usuários.

## Fluxo do Programa
1. **Boas-vindas**: Exibe uma mensagem inicial.
2. **Página de Cadastro/Login**: Oferece opções para cadastro e login.
3. **Página Inicial**: Oferece acesso às páginas de arrecadação, comentários e a opção de logout.
4. **Arrecadação de Fundos**: Gerencia as doações para as três causas ambientais.
5. **Comentários**: Permite deixar e visualizar comentários.

## Exemplo de Uso
Ao iniciar o programa, o usuário é recebido com uma mensagem de boas-vindas e então direcionado para a página de cadastro/login. Após fazer login, o usuário acessa o menu principal, onde pode optar por fazer doações, deixar comentários ou fazer logout. Na página de arrecadação, o usuário pode escolher uma causa e doar uma quantia específica, confirmando a doação. Na página de comentários, o usuário pode deixar feedbacks ou visualizar os existentes.

## Instalação e Execução
Para executar o AquaSentry localmente, siga estas etapas:
1. Clone o repositório para sua máquina local.
2. Certifique-se de ter Python instalado em seu sistema.
3. Navegue até o diretório do projeto e execute o arquivo `main.py` com o Python.

## Considerações Finais
Este sistema básico de arrecadação de fundos e login pode ser expandido com funcionalidades adicionais, como envio de emails de confirmação, integração com sistemas de pagamento, e melhorias na interface de usuário. O AquaSentry visa promover a participação ativa na proteção ambiental, tornando mais fácil para as pessoas contribuírem para um futuro mais sustentável.

## Link do Repositório no GitHub
https://github.com/aquasentry/AquaSentry-GS-Python
