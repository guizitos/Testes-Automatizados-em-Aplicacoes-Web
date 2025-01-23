# Testes-Automatizados-em-Aplicacoes-Web

Este repositório contém um script de **testes automatizados** desenvolvido em Python utilizando o framework **unittest** e o **Selenium WebDriver**. Os testes visam validar as principais funcionalidades do site de demonstração **Sauce Demo**, uma aplicação fictícia de e-commerce.

## Estrutura do Projeto

O código está organizado em uma classe chamada `TestSauceDemo`, que implementa os seguintes testes:

1. **Login bem-sucedido**:
   - Testa se é possível fazer login com credenciais válidas.
2. **Login inválido**:
   - Testa o comportamento do sistema ao tentar fazer login com credenciais incorretas.
3. **Adicionar produto ao carrinho**:
   - Testa se o produto selecionado é adicionado corretamente ao carrinho de compras.
4. **Remover produto do carrinho**:
   - Verifica se um item é removido do carrinho corretamente.
5. **Finalizar compra**:
   - Simula o processo de checkout, incluindo o preenchimento de informações do cliente e finalização do pedido.

---

## Requisitos

- Python 3.8+
- Selenium WebDriver
- Microsoft Edge e Edge WebDriver (compatível com a versão do navegador instalado)

## Estrutura do Código

### **`setUp`**
Configura o ambiente de teste, inicializando o navegador e acessando o site.

### **`login(username, password)`**
Realiza o login no site com as credenciais fornecidas.

### **Testes**
Cada teste é definido em um método separado:

- **`test_successful_login`**: Verifica se o login com credenciais válidas redireciona para a página de inventário.
- **`test_invalid_login`**: Testa o comportamento do sistema ao usar credenciais inválidas e verifica a mensagem de erro.
- **`test_add_to_cart`**: Testa se um produto pode ser adicionado ao carrinho.
- **`test_remove_from_cart`**: Verifica se um produto adicionado ao carrinho pode ser removido.
- **`test_checkout`**: Simula o processo de checkout, desde a adição de um item ao carrinho até a finalização do pedido.

### **`tearDown`**
Finaliza o navegador após a execução de cada teste.

---

## Exemplo de Saída

A execução do script gera uma saída no console que mostra os resultados dos testes. Exemplo:

```
DevTools listening on ws://127.0.0.1:57517/devtools/browser/ab17594f-1174-4b64-a3b0-cd9566b0d45a
.
DevTools listening on ws://127.0.0.1:57553/devtools/browser/0cb518fd-2982-43ca-8fde-ad74b336511e
.
DevTools listening on ws://127.0.0.1:57592/devtools/browser/28a8320c-ed07-42bd-a019-34220ea479b0
.
DevTools listening on ws://127.0.0.1:57621/devtools/browser/567a5d4a-17c5-412e-8a22-33891c73401c
.
DevTools listening on ws://127.0.0.1:57658/devtools/browser/efb869a4-e4c6-4690-a79f-3ae52c0f4678
.
----------------------------------------------------------------------
Ran 5 tests in 75.703s

OK
```

Cada ponto (`.`) indica que um teste foi executado com sucesso. No final, é exibido o total de testes executados e seu status (OK ou FAILED).

---

## Vantagens dos Testes Automatizados

- **Eficiência**: Testes repetitivos e demorados são executados de forma automática.
- **Confiabilidade**: Reduz o risco de erros humanos na execução dos testes.
- **Reprodutibilidade**: Os testes podem ser executados em diferentes máquinas ou ambientes com os mesmos resultados.
- **Manutenção**: Fácil atualização e inclusão de novos cenários de teste.

---

## Contribuições

Contribuições são bem-vindas! Siga os passos abaixo para colaborar:

1. Faça um fork do repositório.
2. Crie uma branch para sua contribuição:
   ```bash
   git checkout -b minha-contribuicao
   ```
3. Submeta um pull request com as alterações propostas.

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

