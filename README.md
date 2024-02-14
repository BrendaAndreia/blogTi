# Blog Django

Este é um projeto de blog desenvolvido em Django, que inclui diversas funcionalidades.
Banco de dados: Postgres
Bucket: google cloud. 

## Funcionalidades

1. **Login/Logout com Contas de Redes Sociais:**
   - Os usuários podem autenticar-se utilizando suas contas de redes sociais, como Google ou GitHub.
   - Utilizamos a biblioteca `django-allauth` para facilitar a integração.

2. **Contato:**
   - Os visitantes podem entrar em contato através de um formulário de contato.
   - As mensagens de contato são enviadas para um endereço de e-mail específico.

3. **Envio de Email usando SMTP Google:**
   - Configurações estão prontas para enviar emails usando o servidor SMTP do Google.
   - Certifique-se de configurar as variáveis de ambiente corretamente.

4. **Pequeno Quiz:**
   - Inclui um pequeno quiz para engajar os usuários.
   - Os resultados podem ser visualizados pelos visitantes.

5. **Posts:**
   - Os usuários podem criar, editar e excluir postagens.
   - A interface do administrador do Django é utilizada para gerenciar as postagens.
     
5. **Comentários:**
   - Os usuários podem criar, editar e excluir comentários.
   - Essa funcionalidade ainda está em andamento. (vocÊ provavelmente encontrará erros)
     
## Modelo de Entidade-Relacionamento (MER)

Diagrama de Modelo de Entidade-Relacionamento (MER) do projeto.
![Diagrama MER](https://github.com/BrendaAndreia/blogTi/blob/main/MER.jpg?raw=true)

## Pré-requisitos

Certifique-se de ter o Python e o Django instalados em sua máquina antes de começar.

```bash
pip install -r requirements.txt
```
## Configuração
Clone o repositório

Configure as variáveis de ambiente para as chaves secretas, informações de autenticação das redes sociais e configurações de e-mail.

Execute as migrações:
```bash
python manage.py migrate
```
Inicie o servidor:
```bash
python manage.py runserver
```
## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema, enviar um pull request, ou mesmo tirar uma dúvida. 
